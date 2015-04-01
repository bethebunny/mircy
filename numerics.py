# Copyright © 2013-2015 Elizabeth Myers.  All rights reserved.
# This file is part of the PyIRC3 project. See LICENSE in the root directory
# for licensing information.

"""IRC numerics derived from Inspircd, Charybdis, Bahamut, and any others.

This file has been automatically generated with conflicts manually sorted out

Conflicts should be handled by using the number directly, not the name.
Comments will be added for conflicts.
"""

try:
    import enum
except ImportError:
    from .util import enum # Not available in Python 3.3 and below

class Numerics(enum.Enum):
    RPL_WELCOME = "001" # bahamut charybdis hybrid inspircd irc2.11.2 ircd-seven ircu plexus ratbox rfc2812 snircd unreal
    RPL_YOURHOST = "002" # bahamut charybdis hybrid inspircd irc2.11.2 ircd-seven ircu plexus ratbox rfc2812 snircd unreal
    RPL_YOURHOSTIS = "002" # inspircd
    RPL_CREATED = "003" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc2812 snircd unreal
    RPL_SERVERCREATED = "003" # inspircd
    RPL_MYINFO = "004" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc2812 snircd unreal
    RPL_SERVERVERSION = "004" # inspircd
    RPL_BOUNCE_RFC2812 = "005" # rfc2812
    RPL_ISUPPORT = "005" # bahamut charybdis hybrid inspircd irc2.11.2 ircd-seven ircu plexus ratbox snircd unreal
    RPL_MAP_UNREAL = "006" # inspircd unreal
    RPL_ENDMAP_UNREAL = "007" # inspircd
    RPL_MAPEND_UNREAL = "007" # unreal
    RPL_SNOMASK = "008" # charybdis inspircd ircd-seven ircu snircd unreal
    RPL_SNOMASKIS = "008" # inspircd
    RPL_BOUNCE = "010" # irc2.11.2
    RPL_REDIR = "010" # charybdis hybrid ircd-seven plexus ratbox unreal
    RPL_MAP = "015" # charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox snircd
    RPL_MAPMORE = "016" # charybdis hybrid ircd-seven ircu plexus ratbox snircd
    RPL_MAPEND = "017" # charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox snircd
    RPL_MAPSTART = "018" # irc2.11.2
    RPL_HELLO = "020" # irc2.11.2
    RPL_APASSWARN_SET = "030" # ircu snircd
    RPL_APASSWARN_SECRET = "031" # ircu snircd
    RPL_APASSWARN_CLEAR = "032" # ircu snircd
    RPL_YOURID = "042" # hybrid irc2.11.2 plexus
    RPL_YOURUUID = "042" # inspircd
    RPL_SAVENICK = "043" # charybdis irc2.11.2 ircd-seven ratbox
    RPL_REMOTEISUPPORT = "105" # unreal
    RPL_TRACELINK = "200" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_TRACECONNECTING = "201" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_TRACEHANDSHAKE = "202" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_TRACEUNKNOWN = "203" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_TRACEOPERATOR = "204" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_TRACEUSER = "205" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_TRACESERVER = "206" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_TRACECAPTURED = "207" # plexus
    RPL_TRACESERVICE = "207" # irc2.11.2 rfc2812 unreal
    RPL_TRACENEWTYPE = "208" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_TRACECLASS = "209" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_STATSHELP = "210" # unreal
    RPL_TRACERECONNECT = "210" # rfc2812
    RPL_STATSLINKINFO = "211" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_STATSCOMMANDS = "212" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_STATSCLINE = "213" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_STATSNLINE = "214" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd
    RPL_STATSOLDNLINE = "214" # unreal
    RPL_STATSILINE = "215" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_STATSKLINE = "216" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_STATSPLINE_IRCU = "217" # ircu snircd
    RPL_STATSQLINE = "217" # bahamut charybdis hybrid irc2.11.2 ircd-seven plexus ratbox rfc1459 rfc2812 unreal
    RPL_STATSYLINE = "218" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_ENDOFSTATS = "219" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_STATSBLINE_UNREAL = "220" # unreal
    RPL_STATSPLINE = "220" # charybdis hybrid ircd-seven plexus ratbox
    RPL_UMODEIS = "221" # bahamut charybdis hybrid inspircd irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_SQLINE_NICK = "222" # unreal
    RPL_STATSBLINE_BAHAMUT = "222" # bahamut
    RPL_STATSJLINE = "222" # ircu snircd
    RPL_STATSELINE_BAHAMUT = "223" # bahamut
    RPL_STATSGLINE_UNREAL = "223" # unreal
    RPL_STATSFLINE = "224" # charybdis hybrid ircd-seven plexus ratbox
    RPL_STATSTLINE_UNREAL = "224" # unreal
    RPL_STATSCLONE = "225" # bahamut
    RPL_STATSDLINE = "225" # charybdis hybrid ircd-seven plexus ratbox
    RPL_STATSELINE_UNREAL = "225" # unreal
    RPL_STATSALINE = "226" # hybrid ircu plexus snircd
    RPL_STATSCOUNT = "226" # bahamut
    RPL_STATSNLINE_UNREAL = "226" # unreal
    RPL_STATSBLINE_PLEXUS = "227" # plexus
    RPL_STATSGLINE_BAHAMUT = "227" # bahamut
    RPL_STATSVLINE_UNREAL = "227" # unreal
    RPL_STATSBANVER = "228" # unreal
    RPL_STATSQLINE_IRCU = "228" # ircu snircd
    RPL_STATSSPAMF = "229" # unreal
    RPL_STATSEXCEPTTKL = "230" # unreal
    RPL_SERVICEINFO = "231" # irc2.11.2 rfc1459 rfc2812 unreal
    RPL_ENDOFSERVICES = "232" # irc2.11.2 rfc1459 rfc2812
    RPL_RULES = "232" # inspircd unreal
    RPL_SERVICE = "233" # irc2.11.2 rfc1459 rfc2812 unreal
    RPL_SERVLIST = "234" # bahamut charybdis irc2.11.2 ircd-seven ratbox rfc1459 rfc2812 unreal
    RPL_SERVLISTEND = "235" # bahamut charybdis irc2.11.2 ircd-seven ratbox rfc1459 rfc2812 unreal
    RPL_STATSVERBOSE = "236" # ircu snircd
    RPL_STATSENGINE = "237" # ircu snircd
    RPL_STATSFLINE_IRCU = "238" # ircu snircd
    RPL_STATSIAUTH = "239" # irc2.11.2
    RPL_STATSVLINE = "240" # irc2.11.2 rfc2812
    RPL_STATSLLINE = "241" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_STATSUPTIME = "242" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_STATSOLINE = "243" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_STATSHLINE = "244" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_STATSSLINE_RFC2812 = "244" # rfc2812
    RPL_STATSSLINE = "245" # bahamut charybdis irc2.11.2 ircd-seven plexus ratbox unreal
    RPL_STATSTLINE_HYBRID = "245" # hybrid
    RPL_STATSPING = "246" # irc2.11.2 rfc2812
    RPL_STATSSERVICE = "246" # hybrid
    RPL_STATSTLINE_IRCU = "246" # ircu snircd
    RPL_STATSULINE_BAHAMUT = "246" # bahamut
    RPL_STATSBLINE_RFC2812 = "247" # irc2.11.2 rfc2812
    RPL_STATSGLINE_IRCU = "247" # ircu snircd
    RPL_STATSXLINE = "247" # charybdis hybrid ircd-seven plexus ratbox unreal
    RPL_STATSDEFINE = "248" # irc2.11.2
    RPL_STATSULINE = "248" # charybdis hybrid ircd-seven ircu plexus ratbox snircd unreal
    RPL_STATSDEBUG = "249" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox snircd unreal
    RPL_STATSCONN = "250" # charybdis hybrid ircd-seven ircu plexus ratbox snircd unreal
    RPL_STATSDLINE_RFC2812 = "250" # irc2.11.2 rfc2812
    RPL_LUSERCLIENT = "251" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_LUSEROP = "252" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_LUSERUNKNOWN = "253" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_LUSERCHANNELS = "254" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_LUSERME = "255" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_ADMINME = "256" # bahamut charybdis hybrid inspircd irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_ADMINLOC1 = "257" # bahamut charybdis hybrid inspircd irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_ADMINLOC2 = "258" # bahamut charybdis hybrid inspircd irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_ADMINEMAIL = "259" # bahamut charybdis hybrid inspircd irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_TRACELOG = "261" # bahamut charybdis ircd-seven ratbox rfc1459 rfc2812 unreal
    RPL_ENDOFTRACE = "262" # bahamut charybdis hybrid ircd-seven plexus ratbox
    RPL_TRACEEND = "262" # irc2.11.2 ircu rfc2812 snircd
    RPL_LOAD2HI = "263" # bahamut charybdis hybrid ircd-seven plexus ratbox
    RPL_TRYAGAIN = "263" # irc2.11.2 rfc2812
    RPL_LOCALUSERS = "265" # bahamut charybdis hybrid irc2.11.2 ircd-seven plexus ratbox unreal
    RPL_GLOBALUSERS = "266" # bahamut charybdis hybrid irc2.11.2 ircd-seven plexus ratbox unreal
    RPL_MAPUSERS = "270" # inspircd
    RPL_PRIVS = "270" # charybdis ircd-seven ircu snircd
    RPL_SILELIST = "271" # bahamut ircu snircd unreal
    RPL_ENDOFSILELIST = "272" # bahamut ircu snircd unreal
    RPL_STATSDLINE_IRCU = "275" # ircu snircd unreal
    RPL_USINGSSL = "275" # bahamut
    RPL_STATSRLINE = "276" # ircu snircd
    RPL_WHOISCERTFP = "276" # charybdis hybrid ircd-seven plexus
    RPL_GLIST = "280" # ircu snircd
    RPL_ACCEPTLIST = "281" # charybdis hybrid ircd-seven plexus ratbox
    RPL_ENDOFGLIST = "281" # ircu snircd
    RPL_ENDOFACCEPT = "282" # charybdis hybrid ircd-seven plexus ratbox
    RPL_JUPELIST = "282" # ircu snircd
    RPL_ENDOFJUPELIST = "283" # ircu snircd
    RPL_FEATURE = "284" # ircu snircd
    RPL_NEWHOSTIS = "285" # hybrid snircd
    RPL_CHKHEAD = "286" # snircd
    RPL_CHANUSER = "287" # snircd
    RPL_PATCHHEAD = "288" # snircd
    RPL_PATCHCON = "289" # snircd
    RPL_DATASTR = "290" # snircd
    RPL_HELPHDR = "290" # unreal
    RPL_ENDOFCHECK = "291" # snircd
    RPL_HELPOP = "291" # unreal
    RPL_HELPTLR = "292" # unreal
    RPL_HELPHLP = "293" # unreal
    RPL_HELPFWD = "294" # unreal
    RPL_HELPIGN = "295" # unreal
    RPL_NONE = "300" # bahamut charybdis irc2.11.2 ircd-seven ratbox rfc1459 rfc2812 unreal
    RPL_AWAY = "301" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_USERHOST = "302" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_ISON = "303" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_SYNTAX = "304" # inspircd
    RPL_TEXT = "304" # bahamut charybdis irc2.11.2 ircd-seven plexus ratbox snircd unreal
    RPL_UNAWAY = "305" # bahamut charybdis hybrid inspircd irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_NOWAWAY = "306" # bahamut charybdis hybrid inspircd irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_WHOISREGNICK = "307" # bahamut hybrid plexus unreal
    RPL_RULESSTART = "308" # unreal
    RPL_RULESTART = "308" # inspircd
    RPL_WHOISADMIN = "308" # bahamut hybrid
    RPL_ENDOFRULES = "309" # unreal
    RPL_RULESEND = "309" # inspircd
    RPL_WHOISSADMIN = "309" # bahamut
    RPL_WHOISHELPOP = "310" # unreal
    RPL_WHOISMODES = "310" # hybrid plexus
    RPL_WHOISSVCMSG = "310" # bahamut
    RPL_WHOISUSER = "311" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_WHOISSERVER = "312" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_WHOISOPERATOR = "313" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_WHOWASUSER = "314" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_ENDOFWHO = "315" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_WHOISCHANOP = "316" # bahamut charybdis hybrid irc2.11.2 ircd-seven plexus ratbox rfc1459 rfc2812 unreal
    RPL_WHOISIDLE = "317" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_ENDOFWHOIS = "318" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_WHOISCHANNELS = "319" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_WHOISSPECIAL = "320" # ircd-seven unreal
    RPL_LISTSTART = "321" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_LIST = "322" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_LISTEND = "323" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_CHANNELMODEIS = "324" # bahamut charybdis hybrid inspircd irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_CHANNELMLOCK = "325" # charybdis ircd-seven
    RPL_UNIQOPIS = "325" # irc2.11.2 rfc2812
    RPL_CHANNELURL = "328" # charybdis ircd-seven
    RPL_CHANNELCREATED = "329" # inspircd
    RPL_CREATIONTIME = "329" # bahamut charybdis hybrid ircd-seven ircu plexus ratbox snircd unreal
    RPL_WHOISACCOUNT = "330" # hybrid ircu snircd
    RPL_WHOISLOGGEDIN = "330" # charybdis ircd-seven ratbox unreal
    RPL_NOTOPIC = "331" # bahamut charybdis hybrid inspircd irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_NOTOPICSET = "331" # inspircd
    RPL_TOPIC = "332" # bahamut charybdis hybrid inspircd irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_TOPICTIME = "333" # inspircd
    RPL_TOPICWHOTIME = "333" # bahamut charybdis hybrid ircd-seven ircu plexus ratbox snircd unreal
    RPL_TOPIC_WHO_TIME = "333" # irc2.11.2
    RPL_COMMANDSYNTAX = "334" # bahamut
    RPL_LISTSYNTAX = "334" # unreal
    RPL_LISTUSAGE = "334" # ircu snircd
    RPL_WHOISBOT = "335" # unreal
    RPL_INVITELIST_UNREAL_OLD = "336" # unreal
    RPL_ENDOFINVITELIST_UNREAL_OLD = "337" # unreal
    RPL_WHOISTEXT = "337" # bahamut charybdis hybrid ircd-seven
    RPL_WHOISACTUALLY = "338" # bahamut charybdis hybrid ircd-seven ircu plexus ratbox snircd
    RPL_USERIP = "340" # ircu snircd unreal
    RPL_INVITING = "341" # bahamut charybdis hybrid inspircd irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_SUMMONING = "342" # bahamut charybdis irc2.11.2 ircd-seven ratbox rfc1459 rfc2812 unreal
    RPL_WHOISOPERNAME = "343" # snircd
    RPL_REOPLIST = "344" # irc2.11.2
    RPL_ENDOFREOPLIST = "345" # irc2.11.2
    RPL_INVITED = "345" # inspircd
    RPL_ISSUEDINVITE = "345" # ircu snircd
    RPL_INVEXLIST = "346" # unreal
    RPL_INVITELIST = "346" # bahamut charybdis hybrid inspircd irc2.11.2 ircd-seven ircu plexus ratbox rfc2812 snircd
    RPL_ENDOFINVEXLIST = "347" # unreal
    RPL_ENDOFINVITELIST = "347" # bahamut charybdis hybrid inspircd irc2.11.2 ircd-seven ircu plexus ratbox rfc2812 snircd
    RPL_EXCEPTLIST = "348" # charybdis hybrid irc2.11.2 ircd-seven plexus ratbox rfc2812
    RPL_EXEMPTLIST = "348" # bahamut
    RPL_EXLIST = "348" # unreal
    RPL_ENDOFEXCEPTLIST = "349" # charybdis hybrid irc2.11.2 ircd-seven plexus ratbox rfc2812
    RPL_ENDOFEXEMPTLIST = "349" # bahamut
    RPL_ENDOFEXLIST = "349" # unreal
    RPL_VERSION = "351" # bahamut charybdis hybrid inspircd irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_WHOREPLY = "352" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_NAMREPLY = "353" # bahamut charybdis hybrid inspircd irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_RWHOREPLY = "354" # bahamut
    RPL_WHOSPCRPL = "354" # charybdis ircd-seven ircu snircd
    RPL_DELNAMREPLY = "355" # ircu snircd
    RPL_WHOWASREAL = "360" # charybdis ircd-seven
    RPL_KILLDONE = "361" # bahamut charybdis irc2.11.2 ircd-seven ratbox rfc1459 rfc2812 unreal
    RPL_CLOSING = "362" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_CLOSEEND = "363" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_LINKS = "364" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_ENDOFLINKS = "365" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_ENDOFNAMES = "366" # bahamut charybdis hybrid inspircd irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_BANLIST = "367" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_ENDOFBANLIST = "368" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_ENDOFWHOWAS = "369" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_INFO = "371" # bahamut charybdis hybrid inspircd irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_MOTD = "372" # bahamut charybdis hybrid inspircd irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_INFOSTART = "373" # bahamut charybdis hybrid irc2.11.2 ircd-seven plexus ratbox rfc1459 rfc2812 unreal
    RPL_ENDOFINFO = "374" # bahamut charybdis hybrid inspircd irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_MOTDSTART = "375" # bahamut charybdis hybrid inspircd irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_ENDOFMOTD = "376" # bahamut charybdis hybrid inspircd irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_WHOISHOST = "378" # charybdis ircd-seven unreal
    RPL_WHOISMODES_UNREAL = "379" # unreal
    RPL_YOUAREOPER = "381" # inspircd
    RPL_YOUREOPER = "381" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_REHASHING = "382" # bahamut charybdis hybrid inspircd irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_YOURESERVICE = "383" # irc2.11.2 rfc2812 unreal
    RPL_MYPORTIS = "384" # bahamut charybdis irc2.11.2 ircd-seven ratbox rfc1459 rfc2812 unreal
    RPL_NOTOPERANYMORE = "385" # bahamut charybdis irc2.11.2 ircd-seven ratbox unreal
    RPL_QLIST = "386" # unreal
    RPL_RSACHALLENGE = "386" # charybdis hybrid ircd-seven plexus ratbox
    RPL_ENDOFQLIST = "387" # unreal
    RPL_ALIST = "388" # unreal
    RPL_ENDOFALIST = "389" # unreal
    RPL_TIME = "391" # bahamut charybdis hybrid inspircd irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    RPL_USERSSTART = "392" # bahamut charybdis hybrid irc2.11.2 ircd-seven plexus ratbox rfc1459 rfc2812 unreal
    RPL_USERS = "393" # bahamut charybdis hybrid irc2.11.2 ircd-seven plexus ratbox rfc1459 rfc2812 unreal
    RPL_ENDOFUSERS = "394" # bahamut charybdis hybrid irc2.11.2 ircd-seven plexus ratbox rfc1459 rfc2812 unreal
    RPL_NOUSERS = "395" # bahamut charybdis hybrid irc2.11.2 ircd-seven plexus ratbox rfc1459 rfc2812 unreal
    RPL_HOSTHIDDEN = "396" # charybdis hybrid ircd-seven ircu snircd
    RPL_VISIBLEHOST = "396" # plexus
    RPL_YOURDISPLAYEDHOST = "396" # inspircd
    RPL_STATSSLINE_SNIRCD = "398" # snircd
    RPL_USINGSLINE = "399" # snircd
    ERR_NOSUCHNICK = "401" # bahamut charybdis hybrid inspircd irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    ERR_NOSUCHSERVER = "402" # bahamut charybdis hybrid inspircd irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    ERR_NOSUCHCHANNEL = "403" # bahamut charybdis hybrid inspircd irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    ERR_CANNOTSENDTOCHAN = "404" # bahamut charybdis hybrid inspircd irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    ERR_TOOMANYCHANNELS = "405" # bahamut charybdis hybrid inspircd irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    ERR_WASNOSUCHNICK = "406" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    ERR_TOOMANYTARGETS = "407" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    ERR_NOCTRLSONCHAN = "408" # bahamut hybrid plexus
    ERR_NOSUCHSERVICE = "408" # irc2.11.2 rfc2812 unreal
    ERR_SEARCHNOMATCH = "408" # snircd
    ERR_NOORIGIN = "409" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    ERR_INVALIDCAPCMD = "410" # charybdis hybrid ircd-seven plexus ratbox unreal
    ERR_INVALIDCAPSUBCOMMAND = "410" # inspircd
    ERR_UNKNOWNCAPCMD = "410" # ircu snircd
    ERR_NORECIPIENT = "411" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    ERR_NOTEXTTOSEND = "412" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    ERR_NOTOPLEVEL = "413" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    ERR_WILDTOPLEVEL = "414" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    ERR_BADMASK = "415" # irc2.11.2 rfc2812
    ERR_QUERYTOOLONG = "416" # ircu snircd
    ERR_TOOMANYMATCHES = "416" # charybdis irc2.11.2 ircd-seven ratbox
    ERR_INPUTTOOLONG = "417" # ircu snircd
    ERR_UNKNOWNCOMMAND = "421" # bahamut charybdis hybrid inspircd irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    ERR_NOMOTD = "422" # bahamut charybdis hybrid inspircd irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    ERR_NOADMININFO = "423" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    ERR_FILEERROR = "424" # bahamut charybdis irc2.11.2 ircd-seven ratbox rfc1459 rfc2812 unreal
    ERR_NOOPERMOTD = "425" # unreal
    ERR_TOOMANYAWAY = "429" # bahamut unreal
    ERR_NONICKNAMEGIVEN = "431" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    ERR_ERRONEOUSNICKNAME = "432" # irc2.11.2
    ERR_ERRONEUSNICKNAME = "432" # bahamut charybdis hybrid ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    ERR_NICKNAMEINUSE = "433" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    ERR_NORULES = "434" # inspircd unreal
    ERR_SERVICENAMEINUSE = "434" # irc2.11.2
    ERR_BANNICKCHANGE_CHARYBDIS = "435" # charybdis ircd-seven
    ERR_BANONCHAN = "435" # bahamut
    ERR_SERVICECONFUSED = "435" # irc2.11.2 unreal
    ERR_NICKCOLLISION = "436" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    ERR_BANNICKCHANGE = "437" # bahamut ircu plexus snircd unreal
    ERR_UNAVAILRESOURCE = "437" # charybdis hybrid irc2.11.2 ircd-seven ratbox rfc2812
    ERR_NCHANGETOOFAST = "438" # unreal
    ERR_NICKTOOFAST = "438" # charybdis hybrid ircd-seven ircu plexus ratbox snircd
    ERR_TARGETTOFAST = "439" # bahamut
    ERR_TARGETTOOFAST = "439" # ircu plexus snircd unreal
    ERR_SERVICESDOWN = "440" # bahamut charybdis hybrid ircd-seven ircu plexus snircd unreal
    ERR_USERNOTINCHANNEL = "441" # bahamut charybdis hybrid inspircd irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    ERR_NOTONCHANNEL = "442" # bahamut charybdis hybrid inspircd irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    ERR_USERONCHANNEL = "443" # bahamut charybdis hybrid inspircd irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    ERR_NOLOGIN = "444" # bahamut charybdis irc2.11.2 ircd-seven ratbox rfc1459 rfc2812 unreal
    ERR_SUMMONDISABLED = "445" # bahamut charybdis irc2.11.2 ircd-seven ratbox rfc1459 rfc2812 unreal
    ERR_USERSDISABLED = "446" # bahamut charybdis irc2.11.2 ircd-seven ratbox rfc1459 rfc2812 unreal
    ERR_CANTCHANGENICK = "447" # inspircd
    ERR_NONICKCHANGE = "447" # unreal
    ERR_NOTREGISTERED = "451" # bahamut charybdis hybrid inspircd irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    ERR_HOSTILENAME = "455" # unreal
    ERR_ACCEPTFULL = "456" # charybdis hybrid ircd-seven plexus ratbox
    ERR_ACCEPTEXIST = "457" # charybdis hybrid ircd-seven plexus ratbox
    ERR_ACCEPTNOT = "458" # charybdis hybrid ircd-seven plexus ratbox
    ERR_NOHIDING = "459" # unreal
    ERR_NOTFORHALFOPS = "460" # unreal
    ERR_NEEDMOREPARAMS = "461" # bahamut charybdis hybrid inspircd irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    ERR_ALREADYREGISTERED = "462" # inspircd
    ERR_ALREADYREGISTRED = "462" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    ERR_NOPERMFORHOST = "463" # bahamut charybdis irc2.11.2 ircd-seven ircu ratbox rfc1459 rfc2812 snircd unreal
    ERR_PASSWDMISMATCH = "464" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    ERR_YOUREBANNEDCREEP = "465" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    ERR_YOUWILLBEBANNED = "466" # bahamut charybdis irc2.11.2 ircd-seven ircu ratbox rfc1459 rfc2812 snircd unreal
    ERR_KEYSET = "467" # bahamut charybdis irc2.11.2 ircd-seven ircu ratbox rfc1459 rfc2812 snircd unreal
    ERR_INVALIDUSERNAME = "468" # ircu snircd
    ERR_ONLYSERVERSCANCHANGE = "468" # bahamut hybrid unreal
    ERR_LINKSET = "469" # unreal
    ERR_LINKCHANNEL = "470" # charybdis ircd-seven unreal
    ERR_OPERONLYCHAN = "470" # hybrid
    ERR_CHANNELISFULL = "471" # bahamut charybdis hybrid inspircd irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    ERR_UNKNOWNMODE = "472" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    ERR_INVITEONLYCHAN = "473" # bahamut charybdis hybrid inspircd irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    ERR_BANNEDFROMCHAN = "474" # bahamut charybdis hybrid inspircd irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    ERR_BADCHANNELKEY = "475" # bahamut charybdis hybrid inspircd irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    ERR_BADCHANMASK = "476" # bahamut charybdis irc2.11.2 ircd-seven ircu ratbox rfc1459 rfc2812 snircd unreal
    ERR_OPERONLYCHAN_PLEXUS = "476" # plexus
    ERR_NEEDREGGEDNICK = "477" # bahamut charybdis hybrid ircd-seven ircu plexus ratbox snircd unreal
    ERR_NOCHANMODES = "477" # irc2.11.2 rfc2812
    ERR_BANLISTFULL = "478" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc2812 snircd unreal
    ERR_BADCHANNAME = "479" # bahamut charybdis hybrid ircd-seven ircu plexus ratbox snircd
    ERR_LINKFAIL = "479" # unreal
    ERR_CANNOTKNOCK = "480" # unreal
    ERR_SSLONLYCHAN = "480" # hybrid ratbox
    ERR_THROTTLE = "480" # charybdis ircd-seven
    ERR_NOPRIVILEGES = "481" # bahamut charybdis hybrid inspircd irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    ERR_CHANOPRIVSNEEDED = "482" # bahamut charybdis hybrid inspircd irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    ERR_CANTKILLSERVER = "483" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    ERR_ATTACKDENY = "484" # unreal
    ERR_DESYNC = "484" # bahamut
    ERR_ISCHANSERVICE = "484" # charybdis ircd-seven ircu ratbox snircd
    ERR_RESTRICTED = "484" # hybrid irc2.11.2 rfc2812
    ERR_BANNEDNICK = "485" # charybdis ircd-seven ratbox
    ERR_CHANBANREASON = "485" # bahamut hybrid plexus
    ERR_ISREALSERVICE = "485" # snircd
    ERR_KILLDENY = "485" # unreal
    ERR_UNIQOPPRIVSNEEDED = "485" # rfc2812
    ERR_UNIQOPRIVSNEEDED = "485" # irc2.11.2
    ERR_ACCOUNTONLY = "486" # snircd
    ERR_NONONREG = "486" # bahamut charybdis hybrid ircd-seven plexus unreal
    ERR_MSGSERVICES = "487" # bahamut
    ERR_NOTFORUSERS = "487" # unreal
    ERR_HTMDISABLED = "488" # unreal
    ERR_NOSSL = "488" # bahamut
    ERR_SECUREONLYCHAN = "489" # unreal
    ERR_VOICENEEDED = "489" # charybdis ircd-seven ircu ratbox snircd
    ERR_ALLMUSTSSL = "490" # inspircd
    ERR_NOSWEAR = "490" # unreal
    ERR_NOOPERHOST = "491" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    ERR_NOCTCP = "492" # inspircd plexus unreal
    ERR_NOCTCPALLOWED = "492" # inspircd
    ERR_NOSERVICEHOST = "492" # irc2.11.2 rfc1459 rfc2812
    ERR_NOFEATURE = "493" # ircu snircd
    ERR_NOSHAREDCHAN = "493" # bahamut
    ERR_BADFEATVALUE = "494" # ircu snircd
    ERR_OWNMODE = "494" # bahamut charybdis ircd-seven
    ERR_BADLOGTYPE = "495" # ircu snircd
    ERR_DELAYREJOIN = "495" # inspircd
    ERR_BADLOGSYS = "496" # ircu snircd
    ERR_BADLOGVALUE = "497" # ircu snircd
    ERR_ISOPERLCHAN = "498" # ircu snircd
    ERR_CHANOWNPRIVNEEDED = "499" # plexus unreal
    ERR_STATSKLINE_RFC2812 = "499" # irc2.11.2
    ERR_TOOMANYJOINS = "500" # unreal
    ERR_UMODEUNKNOWNFLAG = "501" # bahamut charybdis hybrid irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    ERR_UNKNOWNSNOMASK = "501" # inspircd
    ERR_USERSDONTMATCH = "502" # bahamut charybdis hybrid inspircd irc2.11.2 ircd-seven ircu plexus ratbox rfc1459 rfc2812 snircd unreal
    ERR_GHOSTEDCLIENT = "503" # bahamut charybdis hybrid ircd-seven plexus ratbox
    ERR_LAST_ERR_MSG_BAHAMUT = "504" # bahamut
    ERR_USERNOTONSERV = "504" # charybdis hybrid ircd-seven plexus ratbox
    ERR_SILELISTFULL = "511" # bahamut ircu snircd unreal
    ERR_NOSUCHGLINE = "512" # ircu snircd
    ERR_TOOMANYWATCH = "512" # bahamut hybrid unreal
    ERR_BADPING = "513" # ircu snircd
    ERR_NEEDPONG = "513" # unreal
    ERR_WRONGPONG = "513" # charybdis hybrid ircd-seven plexus ratbox
    ERR_NOSUCHJUPE = "514" # ircu snircd
    ERR_TOOMANYDCC = "514" # bahamut unreal
    ERR_BADEXPIRE = "515" # ircu snircd
    ERR_DONTCHEAT = "516" # ircu snircd
    ERR_DISABLED = "517" # charybdis ircd-seven ircu snircd unreal
    ERR_LONGMASK = "518" # hybrid ircu plexus snircd
    ERR_NOINVITE = "518" # unreal
    ERR_ADMONLY = "519" # unreal
    ERR_TOOMANYUSERS = "519" # ircu snircd
    ERR_CANTJOINOPERSONLY = "520" # inspircd
    ERR_MASKTOOWIDE = "520" # ircu snircd
    ERR_OPERONLY = "520" # unreal
    ERR_LISTSYNTAX = "521" # bahamut hybrid plexus unreal
    ERR_WHOSYNTAX = "522" # bahamut unreal
    ERR_WHOLIMEXCEED = "523" # bahamut unreal
    ERR_HELPNOTFOUND = "524" # charybdis hybrid ircd-seven plexus ratbox
    ERR_OPERSPVERIFY = "524" # unreal
    ERR_QUARANTINED = "524" # ircu snircd
    ERR_INVALIDKEY = "525" # ircu
    ERR_BADHOSTMASK = "530" # snircd
    ERR_CANTSENDTOUSER = "531" # inspircd
    ERR_HOSTUNAVAIL = "531" # snircd
    ERR_NOTLOWEROPLEVEL = "560" # ircu snircd
    ERR_NOTMANAGER = "561" # ircu snircd
    ERR_CHANSECURED = "562" # ircu snircd
    ERR_UPASSSET = "563" # ircu snircd
    ERR_UPASSNOTSET = "564" # ircu snircd
    ERR_NOMANAGER = "566" # ircu snircd
    ERR_UPASS_SAME_APASS = "567" # ircu snircd
    ERR_LASTERROR = "568" # ircu snircd
    RPL_REAWAY = "597" # unreal
    RPL_GONEAWAY = "598" # unreal
    RPL_NOTAWAY = "599" # unreal
    RPL_LOGON = "600" # bahamut hybrid unreal
    RPL_LOGOFF = "601" # bahamut hybrid unreal
    RPL_WATCHOFF = "602" # bahamut hybrid unreal
    RPL_WATCHSTAT = "603" # bahamut hybrid unreal
    RPL_NOWON = "604" # bahamut hybrid unreal
    RPL_NOWOFF = "605" # bahamut hybrid unreal
    RPL_WATCHLIST = "606" # bahamut hybrid unreal
    RPL_ENDOFWATCHLIST = "607" # bahamut hybrid unreal
    RPL_CLEARWATCH = "608" # unreal
    RPL_NOWISAWAY = "609" # unreal
    RPL_MAPMORE_UNREAL = "610" # unreal
    RPL_DCCSTATUS = "617" # bahamut unreal
    RPL_DCCLIST = "618" # bahamut unreal
    RPL_ENDOFDCCLIST = "619" # bahamut unreal
    RPL_DCCINFO = "620" # bahamut unreal
    RPL_DUMPING = "640" # unreal
    RPL_DUMPRPL = "641" # unreal
    RPL_EODUMP = "642" # unreal
    RPL_SPAMCMDFWD = "659" # unreal
    RPL_STARTTLS = "670" # charybdis ircd-seven unreal
    RPL_WHOISSECURE = "671" # charybdis hybrid ircd-seven ratbox unreal
    RPL_WHOISSSL = "671" # plexus
    RPL_WHOISCGI = "672" # plexus
    ERR_STARTTLS = "691" # charybdis ircd-seven unreal
    RPL_COMMANDS = "702" # inspircd
    RPL_MODLIST = "702" # charybdis hybrid ircd-seven plexus ratbox
    RPL_COMMANDSEND = "703" # inspircd
    RPL_ENDOFMODLIST = "703" # charybdis hybrid ircd-seven plexus ratbox
    RPL_HELPSTART = "704" # charybdis hybrid ircd-seven plexus ratbox
    RPL_HELPTXT = "705" # charybdis hybrid ircd-seven plexus ratbox
    RPL_ENDOFHELP = "706" # charybdis hybrid ircd-seven plexus ratbox
    ERR_TARGCHANGE = "707" # charybdis ircd-seven ratbox
    RPL_ETRACEFULL = "708" # charybdis irc2.11.2 ircd-seven ratbox
    RPL_ETRACE = "709" # charybdis hybrid ircd-seven ratbox
    RPL_KNOCK = "710" # charybdis hybrid ircd-seven plexus ratbox
    RPL_KNOCKDLVR = "711" # charybdis hybrid ircd-seven plexus ratbox
    ERR_TOOMANYKNOCK = "712" # charybdis hybrid ircd-seven plexus ratbox
    ERR_CHANOPEN = "713" # charybdis hybrid ircd-seven plexus ratbox
    ERR_KNOCKONCHAN = "714" # charybdis hybrid ircd-seven plexus ratbox
    ERR_KNOCKDISABLED = "715" # charybdis ircd-seven plexus ratbox
    ERR_TARGUMODEG = "716" # charybdis ircd-seven ratbox
    RPL_TARGUMODEG = "716" # hybrid plexus
    RPL_TARGNOTIFY = "717" # charybdis hybrid ircd-seven plexus ratbox
    RPL_UMODEGMSG = "718" # charybdis hybrid ircd-seven plexus ratbox
    RPL_OMOTDSTART = "720" # charybdis ircd-seven plexus ratbox
    RPL_OMOTD = "721" # charybdis ircd-seven plexus ratbox
    RPL_ENDOFOMOTD = "722" # charybdis ircd-seven plexus ratbox
    ERR_NOPRIVS = "723" # charybdis hybrid ircd-seven plexus ratbox
    RPL_TESTMASK = "724" # charybdis ircd-seven plexus ratbox
    RPL_TESTLINE = "725" # charybdis ircd-seven plexus ratbox
    RPL_NOTESTLINE = "726" # charybdis ircd-seven plexus ratbox
    RPL_ISCAPTURED = "727" # plexus
    RPL_TESTMASKGECOS = "727" # charybdis ircd-seven ratbox
    RPL_ISUNCAPTURED = "728" # plexus
    RPL_QUIETLIST = "728" # charybdis ircd-seven
    RPL_ENDOFQUIETLIST = "729" # charybdis ircd-seven
    RPL_MONONLINE = "730" # charybdis ircd-seven ratbox
    RPL_MONOFFLINE = "731" # charybdis ircd-seven ratbox
    RPL_MONLIST = "732" # charybdis ircd-seven ratbox
    RPL_ENDOFMONLIST = "733" # charybdis ircd-seven ratbox
    ERR_MONLISTFULL = "734" # charybdis ircd-seven ratbox
    RPL_RSACHALLENGE2 = "740" # charybdis ircd-seven ratbox
    RPL_ENDOFRSACHALLENGE2 = "741" # charybdis ircd-seven ratbox
    ERR_MLOCKRESTRICTED = "742" # charybdis ircd-seven unreal
    ERR_INVALIDBAN = "743" # charybdis ircd-seven
    ERR_TOPICLOCK = "744" # charybdis ircd-seven
    RPL_SCANMATCHED = "750" # charybdis ircd-seven
    RPL_SCANUMODES = "751" # charybdis ircd-seven
    RPL_ETRACEEND = "759" # irc2.11.2
    RPL_LOGGEDIN = "900" # charybdis ircd-seven unreal
    RPL_LOGGEDOUT = "901" # charybdis ircd-seven unreal
    ERR_NICKLOCKED = "902" # charybdis ircd-seven unreal
    RPL_SASLSUCCESS = "903" # charybdis ircd-seven unreal
    ERR_SASLFAIL = "904" # charybdis ircd-seven unreal
    ERR_SASLTOOLONG = "905" # charybdis ircd-seven unreal
    ERR_SASLABORTED = "906" # charybdis ircd-seven unreal
    ERR_SASLALREADY = "907" # charybdis ircd-seven unreal
    RPL_SASLMECHS = "908" # charybdis ircd-seven
    ERR_WORDFILTERED = "936" # inspircd
    ERR_CANNOTDOCOMMAND = "972" # plexus unreal
    ERR_CANTUNLOADMODULE = "972" # inspircd
    RPL_UNLOADEDMODULE = "973" # inspircd
    ERR_CANNOTCHANGECHANMODE = "974" # plexus unreal
    ERR_CANTLOADMODULE = "974" # inspircd
    RPL_LOADEDMODULE = "975" # inspircd
    ERR_LAST_ERR_MSG = "999" # charybdis hybrid ircd-seven plexus ratbox
    ERR_NUMERICERR = "999" # unreal
    ERR_NUMERIC_ERR = "999" # bahamut

# All known numerics
known_numerics = frozenset(n.value for _, n in Numerics.__members__.items())

