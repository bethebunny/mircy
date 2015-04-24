#!/usr/bin/env python3
# Copyright © 2015 Andrew Wilcox and Elizabeth Myers.
# All rights reserved.
# This file is part of the PyIRC 3 project. See LICENSE in the root directory
# for licensing information.


"""A basic easy-to-use API

This provides simple interfaces to messaging, responses, topic setting, and
basic channel access control.
"""


from logging import getLogger

from PyIRC.auxparse import prefix_parse, status_prefix_parse
from PyIRC.extension import BaseExtension
from PyIRC.event import LineEvent
from PyIRC.line import Hostmask
from PyIRC.hook import hook
from PyIRC.numerics import Numerics


logger = getLogger(__name__)


class UserScopeEvent(LineEvent):

    """User scope event, when a user goes in or out of view

    .. warning::
        This event is for mostly internal use at the moment and should only be
        used if you know what you're doing.
    """

    CHANNEL = 0
    """Channel level scope"""

    GLOBAL = 1
    """Global level scope"""

    MESSAGE = 2
    """PRIVMSG scope (may be transient and exit may be unknown)"""

    MONITOR = 3
    """Monitor level scope (server notification)"""

    def __init__(self, event, line, hostmask, scope, location, entering,
                 data=None):
        """Initialise the event.

        :param hostmask:
            :py:class:`~PyIRC.line.Hostmask` of user changing scope.

        :param scope:
            The scope of the user.

        :param location:
            Location of scope, may be None for PRIVMSG or MONITOR

        :param entering:
            Whether or not the user is entering scope.

        :param data:
            Extra data, usually prefixes or such
        """
        super().__init__(event, line)

        self.hostmask = hostmask
        self.entering = entering
        self.data = data


class BasicAPI(BaseExtension):

    """Basic API functions, designed to make things easier to use"""

    requires = ["BasicRFC", "ISupport"]

    hook_classes = {
        "userscope" : UserScopeEvent,
    }

    @hook("commands", Numerics.RPL_NAMREPLY)
    def event_names(self, event):
        line = event.line
        params = line.params

        location = params[2]

        isupport = self.get_extension("ISupport")
        prefix = prefix_parse(isupport.get("PREFIX"))

        for userhost in params[-1].split(' '):
            if not userhost:
                return

            modes, userhost = status_prefix_parse(userhost, prefix)
            userhost = Hostmask.parse(userhost)

            self.call_event("userscope", "enter", line, userhost,
                            UserScopeEvent.CHANNEL, location, True, modes)

    @hook("commands", "JOIN")
    def event_join(self, event):
        line = event.line
        params = line.params

        location = params[0]

        cap_negotiate = self.get_extension("CapNegotiate")
        if cap_negotiate and 'extended-join' in cap_negotiate.local:
            account = params[1] if params[1] != '*' else ''
            gecos = params[2]
            data = (account, gecos)
        else:
            data = None

        self.call_event("userscope", "enter", line, line.hostmask,
                        UserScopeEvent.CHANNEL, location, True, data)

    @hook("commands", "PART")
    @hook("commands", "KICK")
    def event_leave_channel(self, event):
        line = event.line
        params = line.params

        location = params[0]
        reason = params[1]

        if line.command.upper() == "KICK":
            victim = Hostmask(nick=params[2])
            reason = params[3] if len(line.params) > 3 else None
        else:
            victim = line.hostmask
            reason = params[2] if len(line.params) > 2 else None

        self.call_event("userscope", "exit", line, victim,
                        UserScopeEvent.CHANNEL, location, False, reason)

    @hook("commands", "QUIT")
    def event_quit(self, event):
        line = event.line
        params = line.params

        data = params[0] if params else None

        self.call_event("userscope", "exit", line, line.hostmask,
                        UserScopeEvent.GLOBAL, None, False, data)

    @hook("commands", "PRIVMSG")
    @hook("commands", "NOTICE")
    def event_message(self, event):
        line = event.line
        params = line.params

        basicrfc = self.get_extension("BasicRFC")
        if not self.casecmp(basicrfc.nick, params[0]):
            return

        data = params[1] if len(params) > 1 else None
        self.call_event("userscope", "enter", line, line.hostmask,
                        UserScopeEvent.MESSAGE, None, True, data)

    def message(self, target, message, notice=False):
        """Send a message to a target.

        :param target:
            Where to send the message, This may be a
            :py:class:`~PyIRC.extensions.channeltrack.Channel` instance,
            :py:class:`~PyIRC.extensions.usertrack.User` instance, or a
            string.

        :param message:
            Message to send

        :param notice:
            Send the message as a notice

        .. warning::
            Use notice judiciously, as many users find them irritating!
        """
        if hasattr(target, "name"):
            # channel
            target = target.name
        elif hasattr(target, "nick"):
            # user
            target = target.nick

        self.send("NOTICE" if notice else "PRIVMSG", [target, message])

    def reply_target(self, line):
        """Get the appropriate target to reply to a given line.

        :param line:
            :py:class:`~PyIRC.base.line.Line` instance of the message to get
            the reply target of. This is needed due to the limitations of the
            IRC framing format.

        :returns:
            Target to reply to
        """
        isupport = self.get_extension("ISupport")

        # Check for STATUSMSG
        statusmsg = tuple(isupport.get("STATUSMSG"))
        if statusmsg and line.params[0].startswith(statusmsg):
            return line.params[0]

        # Channel?
        channels = tuple(isupport.get("CHANTYPES"))
        if line.params[0].startswith(channels):
            return line.params[0]

        # User?
        if line.hostmask.nick:
            return line.hostmask.nick

        # Sod's law.
        return None

    def topic(self, channel, topic):
        """Set the topic in a channel.

        .. note::
            You usually must be opped to set the topic in a channel. This
            command may fail, and this function cannot tell you due to IRC's
            asynchronous nature.

        :param channel:
            Channel to set the topic in. This can be either a
            :py:class:`~PyIRC.extensions.channeltrack.Channel` instance or a
            string.

        :param topic:
            Topic to set in channel. Will unset the topic if set to None or
            the empty string.
        """
        if hasattr(channel, "name"):
            channel = channel.name

        if topic is None:
            topic = ''

        self.send("TOPIC", [channel, topic])

    def mode_params(self, add, mode, target, *args):
        """Set modes on a channel with a given target list.

        This is suitable for mass bans/unbans, special status modes, and more.

        :param add:
            Whether or not mode is being added or removed

        :param mode:
            Mode to apply to channel.

        :param target:
            Channel to apply the modes in. This can be a
            :py:class:`~PyIRC.extensions.channeltrack.Channel` instance,
            :py:class:`~PyIRC.extensions.usertrack.User` instance, or a
            string.

        :param \*args:
            Targets or params for modes. Can be either
            :py:class:`~PyIRC.extensions.usertrack.User` instances or strings.
        """
        if not args:
            raise ValueError("args are needed for this function")

        if len(mode) > 1:
            raise ValueError("Only one mode may be set by this function")

        if hasattr(target, "name"):
            target = target.name
        elif hasattr(target, "nick"):
            target = target.nick

        params = []
        for param in args:
            if hasattr(target, "nick"):
                # Map User instances into nicks
                param = param.nick

            params.append(param)

        isupport = self.get_extension("ISupport")
        if isupport:
            modes = isupport.get("MODES")
            if modes:
                modes = int(modes)
            else:
                # Be conservative
                modes = 4

            if modes > 8:
                # Insanity...
                modes = 8

        groups = (params[n:n + modes] for n in range(0, len(params), modes))
        flag = '+' if add else '-'
        for group in groups:
            modes = flag + (mode * len(group))
            params = [channel, flag + (mode * len(group))]
            params.extend(group)
            self.send("MODE", params)

    def op(self, channel, *args):
        """Op a user (or users) on a given channel.

        :param channel:
            Channel to op the user or users in. This can be a
            :py:class:`~PyIRC.extensions.channeltrack.Channel` instance, or a
            string.

        :param \*args:
            Users to op. Can be
            :py:class:`~PyIRC.extensions.usertrack.User` instances or strings.
        """
        if not args:
            raise ValueError("args are needed for this function")

        self.mode_params(True, 'o', channel, *args)

    def deop(self, channel, *args):
        """Deop a user (or users) on a given channel.

        :param channel:
            Channel to deopop the user or users in. This can be a
            :py:class:`~PyIRC.extensions.channeltrack.Channel` instance, or a
            string.

        :param \*args:
            Users to deop. Can be
            :py:class:`~PyIRC.extensions.usertrack.User` instances or strings.
        """
        if not args:
            raise ValueError("args are needed for this function")

        self.mode_params(False, 'o', channel, *args)

    def voice(self, channel, *args):
        """Voice a user (or users) on a given channel.

        :param channel:
            Channel to voice the user or users in. This can be a
            :py:class:`~PyIRC.extensions.channeltrack.Channel` instance, or a
            string.

        :param \*args:
            Users to voice. Can be
            :py:class:`~PyIRC.extensions.usertrack.User` instances or strings.
        """
        if not args:
            raise ValueError("args are needed for this function")

        self.mode_params(True, 'v', channel, *args)

    def devoice(self, channel, *args):
        """Devoice a user (or users) on a given channel.

        :param channel:
            Channel to devoice the user or users in. This can be a
            :py:class:`~PyIRC.extensions.channeltrack.Channel` instance, or a
            string.

        :param \*args:
            Users to devoice. Can be
            :py:class:`~PyIRC.extensions.usertrack.User` instances or strings.
        """
        if not args:
            raise ValueError("args are needed for this function")

        self.mode_params(False, 'v', channel, *args)

    def halfop(self, channel, *args):
        """Halfop a user (or users) on a given channel.

        This may not be supported by your IRC server. Notably, FreeNode,
        EfNet, and IRCNet do not support this.

        :param channel:
            Channel to halfop the user or users in. This can be a
            :py:class:`~PyIRC.extensions.channeltrack.Channel` instance, or a
            string.

        :param \*args:
            Users to halfop. Can be
            :py:class:`~PyIRC.extensions.usertrack.User` instances or strings.
        """
        if not args:
            raise ValueError("args are needed for this function")

        self.mode_params(True, 'h', channel, *args)

    def dehalfop(self, channel, *args):
        """Dehalfop a user (or users) on a given channel.

        This may not be supported by your IRC server. Notably, FreeNode,
        EfNet, and IRCNet do not support this.

        :param channel:
            Channel to dehalfop the user or users in. This can be a
            :py:class:`~PyIRC.extensions.channeltrack.Channel` instance, or a
            string.

        :param \*args:
            Users to dehalfop. Can be
            :py:class:`~PyIRC.extensions.usertrack.User` instances or strings.
        """
        if not args:
            raise ValueError("args are needed for this function")

        self.mode_params(False, 'h', channel, *args)

    def process_bantargs(self, *args):
        """Process ban targets (as used by ban modes).

        .. note::
            The default mask format is $a:account if an account is available
            for the user. This only works on servers that support extended
            bans. The fallback is ``*!*@host``. This may not be suitable for
            all uses. It is recommended more advanced users use strings
            instead of User instances.
        """
        if not args:
            raise ValueError("args are needed for this function")

        isupport = self.get_extension("ISupport")
        if not isupport:
            extbans = False
        else:
            extban = isupport.get("EXTBAN")
            if extban[0] != '$' or 'a' not in extban[1]:
                extbans = False
            else:
                extbans = True

        # Preprocess strings
        params = []
        for param in args:
            if not hasattr(param, "nick"):
                params.append(param)
                continue

            if extbans and param.account:
                param = "$a:{}".format(param.account)
            else:
                param = "*!*@{}".format(param.host)

            params.append(param)

        return params

    def ban(self, channel, *args):
        """Ban a user (or users) on a given channel.

        :param channel:
            Channel to ban the user or users in. This can be a
            :py:class:`~PyIRC.extensions.channeltrack.Channel` instance, or a
            string.

        :param \*args:
            Users to ban. Can be
            :py:class:`~PyIRC.extensions.usertrack.User` instances or strings.

        .. note::
            All items are passed through :meth:`process_bantargs`.
        """
        self.mode_params(True, 'b', channel, *self.process_bantargs(*args))

    def unban(self, channel, *args):
        """Unban a user (or users) on a given channel.

        Note at present this is not reliable if User instances are passed in.
        This is an unfortunate side effect of the way IRC works (ban masks may
        be freeform). Another extension may provide enhanced capability to
        do this in the future.

        :param channel:
            Channel to unban the user or users in. This can be a
            :py:class:`~PyIRC.extensions.channeltrack.Channel` instance, or a
            string.

        :param \*args:
            Users to unban. Can be
            :py:class:`~PyIRC.extensions.usertrack.User` instances or strings.

        .. note::
            All items are passed through :meth:`process_bantargs`.
        """
        self.mode_params(False, 'b', channel, *self.process_bantargs(*args))

    def banexempt(self, channel, *args):
        """Exempt a user (or users) from being banned on a given channel.

        Most (but not all) servers support this. IRCNet notably does not.

        :param channel:
            Channel to ban exempt the user or users in. This can be a
            :py:class:`~PyIRC.extensions.channeltrack.Channel` instance, or a
            string.

        :param \*args:
            Users to ban exempt. Can be
            :py:class:`~PyIRC.extensions.usertrack.User` instances or strings.

        .. note::
            All items are passed through :meth:`process_bantargs`.
        """
        isupport = self.get_extension("ISupport")
        if isupport and not (isupport.get("EXCEPTS") or 'e' in
                             isupport.get("CHANMODES")[0]):
            return False

        self.mode_params(True, 'e', channel, *self.process_bantargs(*args))

    def unbanexempt(self, channel, *args):
        """Un-exempt a user (or users) from being banned on a given channel.

        Most (but not all) servers support this. IRCNet notably does not.

        Note at present this is not reliable if User instances are passed in.
        This is an unfortunate side effect of the way IRC works (ban masks may
        be freeform). Another extension may provide enhanced capability to
        do this in the future.

        :param channel:
            Channel to un-ban exempt the user or users in. This can be a
            :py:class:`~PyIRC.extensions.channeltrack.Channel` instance, or a
            string.

        :param \*args:
            Users to un-ban exempt. Can be
            :py:class:`~PyIRC.extensions.usertrack.User` instances or strings.

        .. note::
            All items are passed through :meth:`process_bantargs`.
        """
        isupport = self.get_extension("ISupport")
        if isupport and not (isupport.get("EXCEPTS") or 'e' in
                             isupport.get("CHANMODES")[0]):
            return False

        self.mode_params(False, 'e', channel, *self.process_bantargs(*args))

    def inviteexempt(self, channel, *args):
        """Invite exempt a user (or users) on a given channel.

        Most (but not all) servers support this. IRCNet notably does not.

        :param channel:
            Channel to ban exempt the user or users in. This can be a
            :py:class:`~PyIRC.extensions.channeltrack.Channel` instance, or a
            string.

        :param \*args:
            Users to invite exempt. Can be
            :py:class:`~PyIRC.extensions.usertrack.User` instances or strings.

        .. note::
            All items are passed through :meth:`process_bantargs`.
        """
        isupport = self.get_extension("ISupport")
        if isupport and not (isupport.get("EXCEPTS") or 'I' in
                             isupport.get("CHANMODES")[0]):
            return False

        self.mode_params(True, 'I', channel, *self.process_bantargs(*args))

    def uninviteexempt(self, channel, *args):
        """Un-invite exempt a user (or users) on a given channel.

        Most (but not all) servers support this. IRCNet notably does not.

        Note at present this is not reliable if User instances are passed in.
        This is an unfortunate side effect of the way IRC works (masks may be
        freeform). Another extension may provide enhanced capability to do this
        in the future.

        :param channel:
            Channel to un-invite exempt the user or users in. This can be a
            :py:class:`~PyIRC.extensions.channeltrack.Channel` instance, or a
            string.

        :param \*args:
            Users to un-invite exempt. Can be
            :py:class:`~PyIRC.extensions.usertrack.User` instances or strings.

        .. note::
            All items are passed through :meth:`process_bantargs`.
        """
        isupport = self.get_extension("ISupport")
        if isupport and not (isupport.get("EXCEPTS") or 'I' in
                             isupport.get("CHANMODES")[0]):
            return False

        self.mode_params(False, 'I', channel, *self.process_bantargs(*args))

    def quiet(self, channel, *args):
        """Quiet a user (or users) on a given channel.

        Many servers do not support this. This supports the charybdis-derived
        variant. This means it will work on Charybdis and ircd-seven networks
        (notably FreeNode) but few others.

        InspIRCd and (UnrealIRCd) support will come eventually.

        This **requires** :py:class:`~PyIRC.extensions.isupport.ISupport` be
        enabled, to disambiguate quiet from owner on UnrealIRCd and InspIRCd.

        :param channel:
            Channel to quiet the user or users in. This can be a
            :py:class:`~PyIRC.extensions.channeltrack.Channel` instance, or a
            string.

        :param \*args:
            Users to quiet. Can be
            :py:class:`~PyIRC.extensions.usertrack.User` instances or strings.

        .. note::
            All items are passed through :meth:`process_bantargs`.
        """
        isupport = self.get_extension("ISupport")
        if not isupport:
            return False

        if 'q' not in isupport.get("CHANMODES")[0]:
            return False

        if 'q' in isupport.get('PREFIX'):
            # Nope! It's owner here! RUN AWAY!!!
            return False

        self.mode_params(True, 'q', channel, *self.process_bantargs(*args))

    def unquiet(self, channel, *args):
        """Unquiet a user (or users) on a given channel.

        Many servers do not support this. This supports the charybdis-derived
        variant. This means it will work on Charybdis and ircd-seven networks
        (notably FreeNode) but few others.

        InspIRCd and (UnrealIRCd) support will come eventually.

        This **requires** :py:class:`~PyIRC.extensions.isupport.ISupport` be
        enabled, to disambiguate quiet from owner on UnrealIRCd and InspIRCd.

        Note at present this is not reliable if
        :py:class:`~PyIRC.extensions.usertrack.User` instances are passed in.
        This is an unfortunate side effect of the way IRC works (masks may be
        freeform). Another extension may provide enhanced capability to do this
        in the future.

        :param channel:
            Channel to unquiet the user or users in. This can be a
            :py:class:`~PyIRC.extensions.channeltrack.Channel` instance, or a
            string.

        :param \*args:
            Users to unquiet. Can be
            :py:class:`~PyIRC.extensions.usertrack.User` instances or strings.

        .. note::
            All items are passed through :meth:`process_bantargs`.
        """
        isupport = self.get_extension("ISupport")
        if not isupport:
            return False

        if 'q' not in isupport.get("CHANMODES")[0]:
            return False

        if 'q' in isupport.get('PREFIX'):
            # Nope! It's owner here! RUN AWAY!!!
            return False

        self.mode_params(False, 'q', channel, *self.process_bantargs(*args))

