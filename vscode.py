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
        "code pallette [<text>]": Key("cs-p") + Text("%(text)s"),
        "dig [<text>]": Key("c-p") + Text("%(text)s"),
        "open folder": Key("c-k/3, c-o"),
        "new window": Key("cs-n"),
        "save new": Key("ca-n"),
        "preview": Key("cs-v"),
        "close saved tabs": Key("c-k, u"),
        "close all tabs": Key("c-k, w"),

        ### Search ###
        "code search": Key("cs-f"),
        "code replace": Key("ca-f"),
        "code replace all": Key("cs-h"),
        "consult docs": Key("c-h"),

        ### Navigation ###
        "jump code": Key("c-g"),
        "find def": Key("f12"),

        ### Editing ###
        "code comment": Key("c-slash"),
        # releasing a key which is not being held down harmlessly does nothing.
        "kite": Key("a:up/5000") + Key("tab"),

        ### MetaGo extension ###
        "hyper [<letters>]": Key("a-semicolon/5, %(letters)s"),
        "grab hyper [<letters>]": Key("sa-semicolon") + Key("%(letters)s"),
        "focus cursor": Key("a-m"),
        "cursor top": Key("a-t"),
        "cursor bottom": Key("a-b"),
        "block up": Key("a-home"),
        "block down": Key("a-end"),
        "take block": Key("end, sa-home"),
        "grab block": Key("home, sa-end"),

        ### Subword Navigation extension ###
        # "left [<n>] sub": Key("a-left/3:%(n)d/10"),
        # "right [<n>] sub": Key("a-right/3:%(n)d/10"),
        # "take [<n>] sub": Key("sa-left/3:%(n)d/10"),
        # "grab [<n>] sub": Key("sa-right/3:%(n)d/10"),
        # "whack [<n>] sub": Key("a-backspace/3:%(n)d/10"),
        # "bump [<n>] sub": Key("a-delete/3:%(n)d/10"),

        ### Window ###
        "Zen mode": Key("c-k/3, z"),
        "code bar": Key("c-b"),
        "code files": Key("cs-j"),
        "code outline": Key("cs-o"),
        "code source": Key("cs-g"),
        "code debug": Key("cs-d"),
        "code extensions": Key("cs-x"),
        "code settings": Key("c-comma"),
        "code shortcuts": Key("c-k/3, c-s"),
        "code theme": Key("c-k, c-t"),
        "code split": Key("c-backslash"),
        "code (term|terminal|one)": Key("a-1"),
        "focus (term|terminal|one)": Key("c-1"),
        "focus two": Key("c-2"),
        "focus three": Key("c-3"),
        "focus four": Key("c-4"),
        "focus right": Key("cs-pagedown"),
        "focus left": Key("cs-pageup"),
        "throw right": Key("cs-pagedown"),
        "throw left": Key("cs-pageup"),

        ### Terminal ###
        "right (term|terminal)": Key("a-right"),
        "left (term|terminal)": Key("a-left"),
        "nexterm": Key("cs-0"),
        "prexterm": Key("cs-9"),
        "new (term|terminal)": Key("cs-1"),
        "split (term|terminal)": Key("c-backslash"),

        ### Debugging ###
        "breakpoint": Key("f9"),
        "step over": Key("f10/50"),
        "step into": Key("f11"),
        "step out [of]": Key("s-f11"),
        "resume": Key("f5"),

    }

    extras = [
        Dictation("text"),
        Choice("letters", letterMap),
    ]
    defaults = {
        "n": 1,
    }
