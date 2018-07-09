# Controls for ncmpcpp

from aenea import (
    Key,
    Dictation,
    Text,
    MappingRule,
    IntegerRef,
    Grammar,
    Choice,
    AppContext
)

mapping = {
    "list": Key("1"),
    "browse": Key("2"),
    "search": Key("3"),
    "library": Key("4"),
    "editor": Key("5"),
    "tags": Key("6"),
    "output": Key("7"),
    "visualizer": Key("8"),

    "play": Key("p"),
    "pause": Key("p"),
    "next": Key("rangle"),
    "back": Key("langle"),

    "add": Key("enter"),
    "push": Key("space"),
    "add random": Key("backtick"),

    "toggle repeat": Key("r"),
    "toggle random": Key("z"),
}


class CommandRule(MappingRule):
    mapping = mapping

    extras = []
    defaults = {
        "n": 1,
    }


context = AppContext(executable="gnome-terminal", title="ncmpcpp")

grammar = Grammar("ncmpcpp", context=context)
grammar.add_rule(CommandRule())
grammar.load()

# Unload function which will be called by natlink at unload time.


def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
