# Generic desktop control

from aenea import *


class DesktopRule(MappingRule):
    mapping = {
        ### Basics ###
        "launch (terminal|term)": Key("w-enter"),
        "look left": Key("w-j"),
        "look down": Key("w-k"),
        "look up": Key("w-l"),
        "look right": Key("w-semicolon"),
        "look parent": Key("w-a"),
        "change look": Key("w-space"),

        ### Moving Windows ###
        "snap left": Key("ws-j"),
        "snap down": Key("ws-k"),
        "snap up": Key("ws-l"),
        "snap right": Key("ws-semicolon"),

        ### Modifying Windows ###
        "snap full": Key("w-f"),
        "snap lat": Key("w-v"),
        "snap long": Key("w-h"),
        "snap resize": Key("w-r"),

        ### Container Layout ###
        "snap default": Key("w-e"),
        "snap stack": Key("w-s"),
        "snap tab": Key("w-w"),

        ### Floating ###
        "snap float": Key("ws-space"),

        ### Using Workspaces ###
        "woke <n>": Key("w-:%(n)d"),
        "snap <n>": Key("w-:%(n)d"),

        ### Opening / Closing ###
        "launch": Key("w-d"),
        "snap kill": Key("ws-q"),

        ### Restart /Exit ###
        "I three reload": Key("ws-c"),
        "I three restart": Key("ws-r"),
        "I three exit": Key("ws-e"),


        ### Windows ###
        "snap close": Key("c-w"),
        "snap new": Key("c-n"),
        "snap quit": Key("c-q"),

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
