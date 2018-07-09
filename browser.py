# Contextual grammar for web browser control

from lib.maps import letterMap

from aenea import (
    Key,
    Mouse,
    MappingRule,
    IntegerRef,
    Grammar,
    ProxyAppContext,
    Choice
)


class BrowserRule(MappingRule):
    mapping = {
        "jump tab [<n>]": Key("a-%(n)d"),  # Not supported by Opera.
        "restore window": Key("cs-n"),
        "restore tab": Key("cs-t"),
        "open private window": Key("cs-p"),
        "address bar": Key("c-l"),
        "copy address": Key("c-l/10, c-c/10"),
        "paste address": Key("c-l/10, c-v/10"),
        "go home": Key("a-home"),
        "stop loading": Key("escape"),
        "reload [page]": Key("f5"),
        "bookmark [this] page": Key("c-d"),

        "dev toolbox": Key("cs-i"),
        "dev console": Key("cs-k"),
        "dev inspector": Key("cs-c"),
        "dev debugger": Key("cs-s"),
        "dev responsive":  Key("cs-m"),
        "dev scratchpad": Key("s-f4"),

        "dev inspect element": Mouse("right") + Key("q"),

        "reset zoom": Key("c-0"),

        # vimium
        "hyper fox": Key("escape, f"),
        "hypo fox": Key("escape, s-f"),
        "last tab": Key("g, dollar"),
    }

    extras = [
        IntegerRef("n", 1, 10),
        Choice("letters", letterMap),
    ]
    defaults = {
        "n": 1
    }
