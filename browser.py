# Contextual grammar for web browser control

from lib.maps import letterMap

from aenea import (
    Key,
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
        "address bar": Key("c-l"),
        "copy address": Key("c-l/10, c-c/10"),
        "paste address": Key("c-l/10, c-v/10"),
        "go home": Key("a-home"),
        "stop loading": Key("escape"),
        "reload [page]": Key("f5"),
        "bookmark [this] page": Key("c-d"),
        # "back"
        # "forward"
        # "new tab"
        # "close <n> tab[s]"

        "dev tools": Key("cs-i"),
        "dev console": Key("cs-k"),
        "dev inspector": Key("cs-c"),
        "dev debugger": Key("cs-s"),

        "reset zoom": Key("c-0"),
        # "zoom in [<n>]": Key("c-minus:%(n)d"),
        # "zoom out [<n>]": Key("cs-plus:%(n)d"),

        # vim extension
        "hyper": Key("escape, f"),
    }

    extras = [
        IntegerRef("n", 1, 100),
        Choice("letters", letterMap),
    ]
    defaults = {
        "n": 1
    }
