# Contextual grammar for web browser control

from aenea import (
    Key,
    MappingRule,
    IntegerRef,
    Grammar,
    ProxyAppContext
)


mapping = {
   "back [<n>]": Key("a-left/15:%(n)d"),
   "forward [<n>]": Key("a-right/15:%(n)d"),
   "restore window": Key("cs-n"),
   "new tab": Key("c-t"),
   "close tab": Key("c-w"),
   "close <n> tabs": Key("c-w/20:%(n)d"),
   "nexta [<n>]": Key("c-pgup:%(n)d"),
   "prexta [<n>]": Key("c-pgdown:%(n)d"),
   "restore tab": Key("cs-t"),
   "search": Key("c-k"),
   "address": Key("a-d"),
   "copy address": Key("a-d/10, c-c/10"),
   "paste address": Key("a-d/10, c-v/10"),
   "go home": Key("a-home"),
   "stop loading": Key("escape"),
   "reload [page]": Key("f5"),

   "bookmark [this] page": Key("c-d"),

   "reset zoom": Key("c-0"),
   "zoom in [<n>]": Key("c-minus:%(n)d"),
   "zoom out [<n>]": Key("cs-plus:%(n)d"),

   "find in page": Key("c-f"),
   "close find": Key("escape"),
   "find previous [<n>]": Key("s-f3/10:%(n)d"),
   "find next [<n>]": Key("f3/10:%(n)d"),

   "go to tab [<n>]": Key("a-%(n)d") # Not supported by Opera.

}


rules = MappingRule(
    mapping=mapping,
    extras=[
        IntegerRef("n", 1, 100),
    ],
    defaults={
        "n": 1
    }
)


nixContext1 = ProxyAppContext(executable="firefox", title="Firefox")
nixContext2 = ProxyAppContext(executable="chrome", title="Chrome")
nixContext3 = ProxyAppContext(executable="chrome", title="Chromium")
nixContext4 = ProxyAppContext(executable="opera", title="Opera")
nixContext = nixContext1 | nixContext2 | nixContext3 | nixContext4

grammar = Grammar("FF, Chrome, and Opera", context=nixContext)
grammar.add_rule(rules)
grammar.load()


def unload():
    """Unload function which will be called at unload time."""
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
