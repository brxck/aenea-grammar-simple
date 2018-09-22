# Generic desktop control

from aenea import *


class DesktopRule(MappingRule):
    mapping = {
        ### Windows ###
        "snap screen": Key("w-up"),
        "snap small": Key("w-down"),
        "snap left": Key("w-left"),
        "snap right": Key("w-right"),
        "snap close": Key("c-w"),
        "snap new": Key("c-n"),
        "snap quit": Key("c-q"),
        "snap full": Key("f11"),

        "snap in [<n>]": Key("alt:down, tab:%(n)d, alt:up"),
        "snap out [<n>]": Key("alt:down, s-tab:%(n)d, alt:up"),

        ### Common controls ###
        "stamp": Key("c-s"),
        "finna": Key("c-f"),
        "finna previous [<n>]": Key("s-f3/10:%(n)d"),
        "finna next [<n>]": Key("f3/10:%(n)d"),
        "open new": Key("c-n"),
        "new tab": Key("c-t"),
        "close tab [<n>]": Key("c-w/20:%(n)d"),
        "zoom in [<n>]": Key("c-plus:%(n)d"),
        "zoom out [<n>]": Key("cs-minus:%(n)d"),
        "zoom zero": Key("c-0"),
        "browse back [<n>]": Key("a-left/15:%(n)d"),
        "browse forward [<n>]": Key("a-right/15:%(n)d"),
        "nexta [<n>]": Key("c-pgdown:%(n)d"),
        "prexta [<n>]": Key("c-pgup:%(n)d"),
        "emote [<text>]": Key("scaw-j") + Text("%(text)s"),

        ### Workspaces ###
        "woke <n>": Key("caw-%(n)d"),
        "whip [<n>]": Key("ca-right:%(n)d"),
        "wox [<n>]": Key("ca-left:%(n)d"),
        "snap whip [<n>]": Key("sca-right:%(n)d"),
        "snap wox [<n>]": Key("sca-left:%(n)d"),
        "snap sling <n>": Key("scaw-%(n)d"),

        ### Albert ###
        "spot [<text>]": Key("scaw-space/10") + Text("%(text)s"),
        "spike [<text>]": Key("scaw-space/10") + Text("%(text)s") + Key("enter"),

        ### Launch ###
        "launch terminal": Key("scaw-e"),
        "launch files": Key("scaw-w"),
        "launch music": Key("scaw-t"),
        "launch browser": Key("scaw-r"),
        "launch monitor": Key("scaw-q"),
        "launch code": Key("scaw-d"),

        ### Media ###
        # "[toggle] mute": Key("w-"),
        "louder <n>": Key("w-pgup:%(n)d"),
        "softer <n>": Key("w-pgdown:%(n)d"),
        "next track": Key("sw-right"),
        "last track": Key("sw-left"),
        "tunic": Key("sw-up"),
    }

    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 10),
    ]
    defaults = {
        "n": 1,
    }
