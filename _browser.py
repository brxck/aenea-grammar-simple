# Contextual grammar for web browser control

from aenea import (
    Key,
    MappingRule,
    IntegerRef,
    Grammar,
    ProxyAppContext
)


mapping = {
   "go back [<n>]": Key("a-left/15:%(n)d"),
   "go forward [<n>]": Key("a-right/15:%(n)d"),
   "[open] new window": Key("c-n"),
   "close window": Key("cs-w"),
   "undo close window": Key("cs-n"),
   "[open] new tab": Key("c-t"),
   "close tab": Key("c-w"),
   "close <n> tabs": Key("c-w/20:%(n)d"),
   "[go to] next tab [<n>]": Key("c-tab:%(n)d"),
   "[go to] previous tab [<n>]": Key("cs-tab:%(n)d"),
   "(restore|undo close) tab": Key("cs-t"),
   "go to search [bar]": Key("c-k"),
   "go to address [bar]": Key("a-d"),
   "go to top": Key("home"),
   "go to bottom": Key("end"),
   "copy address": Key("a-d/10, c-c/10"),
   "paste address": Key("a-d/10, c-v/10"),
   "go home": Key("a-home"),
   "stop loading": Key("escape"),
   "reload [page]": Key("f5"),

   "bookmark [this] page": Key("c-d"),

   "normal text size": Key("c-0"),
   "decrease text size [<n>]": Key("c-minus:%(n)d"),
   "increase text size [<n>]": Key("cs-plus:%(n)d"),

   "find in page": Key("c-f"),
   "close find": Key("escape"),
   "find previous [<n>]": Key("s-f3/10:%(n)d"),
   "find next [<n>]": Key("f3/10:%(n)d"),

   # "go to tab [<n>]": DynamicAction(Key("c-%(n)d"), Key("a-%(n)d")) # Not supported by Opera.
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
