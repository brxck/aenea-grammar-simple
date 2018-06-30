# Visual Studio Code grammar

from aenea import (
    Key,
    Text,
    Dictation,
    MappingRule,
    IntegerRef,
    Grammar,
    Choice
)

from lib.maps import letterMap


class CodeRule(MappingRule):
    mapping = {
        ### Files ###
        "code palette": Key("cs-p"),
        "code <text>": Key("c-p") + Text("%(text)s"),
        "open folder": Key("c-k/3, c-o"),
        "new window": Key("cs-n"),
        "preview": Key("cs-v"),
        # "open new"

        ### Search ###
        "code search": Key("cs-f"),
        "code replace": Key("ca-f"),
        "code replace all": Key("cs-h"),
        "consult docs": Key("c-h"),
        # "find"
        # "find next <n>"
        # "find previous <n>"

        ### Navigation ###
        "jump": Key("c-g"),
        "def": Key("f12"),
        # "nexta"
        # "prexta"

        ### MetaGo extension ###
        "hyper": Key("a-semicolon"),
        "hyper <letters>": Key("a-semicolon/5, %(letters)s"),
        "(take|grab) hyper": Key("sa-semicolon"),
        "(take|grab) hyper <letters>": Key("sa-semicolon") + Key("%(letters)s"),
        "focus cursor": Key("a-m"),
        "cursor top": Key("a-t"),
        "cursor bottom": Key("a-b"),
        "block up": Key("a-home"),
        "block down": Key("a-end"),
        "take block": Key("sa-home"),
        "grab block": Key("sa-end"),

        ### Subword Navigation extension ###
        # "left [<n>] sub": Key("a-left/3:%(n)d/10"),
        # "right [<n>] sub": Key("a-right/3:%(n)d/10"),
        # "take [<n>] sub": Key("sa-left/3:%(n)d/10"),
        # "grab [<n>] sub": Key("sa-right/3:%(n)d/10"),
        # "whack [<n>] sub": Key("a-backspace/3:%(n)d/10"),
        # "bump [<n>] sub": Key("a-delete/3:%(n)d/10"),

        ### Window ###
        "[(show|toggle)] Zen mode": Key("c-k/3, z"),
        "code bar": Key("c-b"),
        "code files": Key("cs-e"),
        "code source": Key("cs-g"),
        "code debug": Key("cs-d"),
        "code extensions": Key("cs-x"),
        "code settings": Key("c-comma"),
        "code split": Key("c-backslash"),
        "focus (term|terminal|one)": Key("c-1"),
        "focus two": Key("c-2"),
        "focus three": Key("c-3"),
        "focus four": Key("c-4"),
        "focus right": Key("cs-pagedown"),
        "focus left": Key("cs-pageup"),
        "[toggle] (term|terminal|one)": Key("a-1"),
        "new (term|terminal)": Key("cs-1"),
        "split (term|terminal)": Key("c-backslash"),
        "code shortcuts": Key("c-k/3, c-s"),
        "code theme": Key("c-k, c-t"),

        ### Debugging ###
        "[toggle] breakpoint": Key("f9"),
        "step over": Key("f10/50"),
        "step into": Key("f11"),
        "step out [of]": Key("s-f11"),
        "resume": Key("f5"),

    }

    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 50),
        Choice("letters", letterMap),
    ]
    defaults = {
        "n": 1,
    }
