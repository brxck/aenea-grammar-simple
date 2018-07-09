# Generic desktop control

from aenea import *


class DesktopRule(MappingRule):
    mapping = {
        ### Windows ###
        "snap screen": Key("w-up"),
        "snap win": Key("w-down"),
        "snap left": Key("w-left"),
        "snap right": Key("w-right"),
        "snap close": Key("c-w"),
        "snap new": Key("c-n"),
        "snap quit": Key("c-q"),
        "snap full": Key("f11"),
        "flip [<n>]": Key("a-escape:%(n)d"),
        "flop [<n>]": Key("sa-escape:%(n)d"),
        "flap [<n>]": Key("a-tab:%(n)d"),

        ### Common controls ###
        "stamp": Key("c-s"),
        "find": Key("c-f"),
        "open new": Key("c-n"),
        "new tab": Key("c-t"),
        "close tab": Key("c-w"),
        "close <n> tabs": Key("c-w/20:%(n)d"),
        "zoom in [<n>]": Key("c-minus:%(n)d"),
        "zoom out [<n>]": Key("cs-plus:%(n)d"),
        "browse back [<n>]": Key("a-left/15:%(n)d"),
        "browse forward [<n>]": Key("a-right/15:%(n)d"),
        "find in page": Key("c-f"),
        "find previous [<n>]": Key("s-f3/10:%(n)d"),
        "find next [<n>]": Key("f3/10:%(n)d"),
        "nexta [<n>]": Key("c-pgdown:%(n)d"),
        "prexta [<n>]": Key("c-pgup:%(n)d"),

        ### Workspaces ###
        "woke <n>": Key("caw-%(n)d"),
        "wim [<n>]": Key("ca-right:%(n)d"),
        "wox [<n>]": Key("ca-left:%(n)d"),
        "snap wits [<n>]": Key("sca-right:%(n)d"),
        "snap wox [<n>]": Key("sca-left:%(n)d"),
        "snap woke <n>": Key("scaw-%(n)d"),

        ### Albert ###
        "spot [<text>]": Key("scaw-space/3") + Text("%(text)s"),
        "spike [<text>]": Key("scaw-space/3") + Text("%(text)s/10") + Key("enter"),

        ### Media ###
        # "[toggle] mute": Key("w-"),
        "louder <n>": Key("w-pgup%(n)d"),
        "softer <n>": Key("w-pgdown:%(n)d"),
        "next track": Key("sw-right"),
        "last track": Key("sw-left"),
        "(play|pause) music": Key("sw-up"),
    }

    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 10),
    ]
    defaults = {
        "n": 1,
    }
