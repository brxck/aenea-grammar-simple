# Contextual grammar for web browser control

from lib.maps import letterMap

from aenea import (
    Key,
    Text,
    Mouse,
    MappingRule,
    IntegerRef,
    Grammar,
    ProxyAppContext,
    Choice
)


class BrowserRule(MappingRule):
    mapping = {

        "dot com": Text(".com"),
        "dot org": Text(".org"),
        "dot net": Text(".net"),
        "dot I O": Text(".io"),

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
        "dev element": Mouse("right") + Key("q"),

        "dark fox": Key("sa-d"),

        # vimium
        "jump fox": Key("escape, f"),
        "leap fox": Key("escape, s-f"),
        "last tab": Key("g, dollar"),
        "first tab": Key("g, 0"),
        "down half": Key("d"),
        "up half": Key("u"),
        "copy url": Key("y, y"),
        "omni": Key("o"),
    }

    extras = [
        IntegerRef("n", 1, 10)
    ]
    defaults = {
        "n": 1
    }
