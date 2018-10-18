# Low-level keyboard input module
#
# Based on the work done by the creators of the Dictation Toolbox
# https://github.com/dictation-toolbox/dragonfly-scripts
#
# and _multiedit-en.py found at:
# http://dragonfly-modules.googlecode.com/svn/trunk/command-modules/documentation/mod-_multiedit.html
#
# Modifications by: Tony Grosinger
#
# Licensed under LGPL

from natlink import setMicState
from aenea import *

from lib.maps import (
    specialCharMap,
    letterMap,
    upperLetterMap,
    numberMap,
)

from lib import sound


def cancel_and_sleep(text=None, text2=None):
    """Used to cancel an ongoing dictation and puts microphone to sleep.

    This method notifies the user that the dictation was in fact canceled,
     a message in the Natlink feedback window.
    Then the the microphone is put to sleep.
    Example:
    "'random mumbling go to sleep'" => Microphone sleep.

    """
    sound.play(sound.SND_DEACTIVATE)
    print("* Dictation canceled. Going to sleep. *")
    setMicState("sleeping")


letterMap.update(upperLetterMap)


def test():
    sound.play(sound.SND_MESSAGE)


grammarCfg = Config("multi edit")
grammarCfg.cmd = Section("Language section")
grammarCfg.cmd.map = Item(
    {
        ### Mouse ###
        "quiz [<n>]": Mouse("left:%(n)d"),
        "quiz it": Mouse("left:2"),
        "quiz down": Mouse("left:down"),
        "quiz up": Mouse("left:up"),
        "quill": Mouse("right"),
        "quill down": Mouse("right:down"),
        "quill up": Mouse("right:up"),
        "quad": Mouse("middle"),
        "quad down": Mouse("middle:down"),
        "quad up": Mouse("middle:up"),

        ### Navigation ###
        "hop [<n>]": Key("up:%(n)d"),
        "dove [<n>]": Key("down:%(n)d"),
        "lore [<n>]": Key("left:%(n)d"),
        "role [<n>]": Key("right:%(n)d"),
        "lorex [<n>]": Key("c-left/3:%(n)d/10"),
        "rolex [<n>]": Key("c-right/3:%(n)d/10"),
        "pinch [<n>]": Key("pgup:%(n)d"),
        "punch [<n>]": Key("pgdown:%(n)d"),
        "stark": Key("home"),
        "lend": Key("end"),
        "lendit": Key("end, comma"),
        "dockit": Key("c-home/3"),
        "dockex": Key("c-end/3"),
        "cape": Key("escape"),

        ### Selections ###
        "grab <n>": Key("shift:down, right:%(n)d, shift:up"),
        "take <n>": Key("shift:down, left:%(n)d, shift:up"),
        "take <n> (line|lines)": Key("end, shift:down, home, up:%(n)d, shift:up"),
        "grab <n> (line|lines)": Key("home, shift:down, down:%(n)d, shift:up"),
        "grab <n> words": Key("shift:down, c-right:%(n)d, shift:up"),
        "take <n> words": Key("shift:down, c-left:%(n)d, shift:up"),
        "(take|grab) word": Key("c-left, sc-right"),
        "(take|grab) home": Key("shift:down, home, shift:up"),
        "(take|grab) end": Key("shift:down, end, shift:up"),
        "(take|grab) line": Key("home, s-end"),
        "(take|grab) all": Key("c-a/3"),

        ### Whitespace ###
        "space": Key("space"),
        "space [<n>]": Key("space:%(n)d"),
        "slap [<n>]": Key("enter:%(n)d"),
        "slide [<n>]": Key("end, enter:%(n)d"),
        "slip [<n>]": Key("home, enter:%(n)d, up:%(n)d"),
        "kite [<n>]": Key("tab:%(n)d"),
        "tyke [<n>]": Key("s-tab:%(n)d"),

        ### Deletions ###
        "scratch [<n>]": Key("backspace:%(n)d"),
        "chuck [<n>]": Key("del/3:%(n)d"),
        "whack [<n>]": Key("c-backspace:%(n)d"),
        "bump [<n>]": Key("c-delete:%(n)d"),
        "scratch line": Key("home, s-end, del"),
        "chuck line": Key("home:2, s-end, backspace:2"),

        ### Functions ###
        "paste": Key("c-v/3"),
        "copy": Key("c-c/3"),
        "cut": Key("c-x/3"),
        "undo [<n>]": Key("c-z/3:%(n)d"),
        "redo [<n>]": Key("c-y/3:%(n)d"),
        "stamp": Key("c-s"),

        ### Closures ###
        "angles": Key("langle, rangle, left/3"),
        "squares": Key("lbracket, rbracket, left/3"),
        "braces": Key("lbrace, rbrace, left/3"),
        "graces": Key("lbrace, space:2, rbrace, left:2/3"),
        "parens": Key("lparen, rparen, left/3"),
        "quotes": Key("dquote/3, dquote/3, left/3"),
        "smotes": Key("squote, squote, left/3"),
        "ticks": Key("backtick:2, left/3"),
        "pipes": Key("bar:2, left"),

        ### Punctuation ###
        "coy": Key("colon, space"),
        "drip": Key("comma, space"),
        "drip slap": Key("comma, enter"),
        "dot [<n>]": Key("dot:%(n)d"),
        "dash [<n>]": Key("hyphen:%(n)d"),
        "cat [<n>]": Key("colon:%(n)d"),
        "slash [<n>]": Key("slash:%(n)d"),
        "equit [<n>]": Key("equal:%(n)d"),

        ### Maps ###
        "<letters>": Text("%(letters)s"),
        "<char>": Text("%(char)s"),
        "num <num>": Text("%(num)d"),

        ### Misc ###
        "[<text>] go to sleep [<text2>]": Function(cancel_and_sleep),
        "check one two": Function(test),

        ##########################
        ### Visual Studio Code ###
        ##########################

        ### Files ###
        "code command [<text>]": Key("cs-p") + Text("%(text)s"),
        "dig [<text>]": Key("c-p") + Text("%(text)s"),
        "open folder": Key("c-k/3, c-o"),
        "new window": Key("cs-n"),
        "save new": Key("ca-n"),
        "save plain": Key("c-k, s"),
        "code preview": Key("cs-v"),
        "close saved tabs": Key("c-k, u"),
        "close all tabs": Key("c-k, w"),
        "code commit": Key("c-enter"),

        ### Search ###
        "code search": Key("cs-f"),
        "code replace": Key("ca-f"),
        "code replace all": Key("cs-h"),
        "consult docs": Key("c-h"),

        ### Navigation ###
        "jump <num>": Key("c-g") + Text("%(num)d") + Key("enter"),
        "code def": Key("f12"),
        "code peek": Key("cs-f10"),

        ### Editing ###
        "intel": Key("c-space"),
        "block comment": Key("sa-a"),
        "code comment": Key("c-slash"),
        "moovit [<n>]": Key("a-up:%(n)d"),
        "moovex [<n>]": Key("a-down:%(n)d"),
        "shiftit [<n>]": Key("c-rbracket:%(n)d"),
        "shiftex [<n>]": Key("c-lbracket:%(n)d"),
        "doopit": Key("c-c/3, cs-enter, c-v/3, backspace"),
        "doopex": Key("c-c/3, c-enter, c-v/3, backspace"),
        "take others": Key("cs-l"),
        "take next [<n>]": Key("c-d:%(n)d"),
        "(take|grab) close": Key("cs-squote"),
        "peck [<n>]": Key("a-pgup:%(n)d"),
        "peek [<n>]": Key("a-pgdown:%(n)d"),
        "line cursors": Key("sa-i"),
        "code last edit": Key("c-k, c-q"),

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

        ### Window ###
        "code zen": Key("c-k/3, z"),
        "code center": Key("c-k/3, c-l"),
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
        "code wrap": Key("a-z"),
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
        "step out": Key("s-f11"),
        "resume debug": Key("f5"),

    },
    namespace={
        "Key": Key,
        "Text": Text,
    }
)


class KeystrokeRule(MappingRule):
    exported = False
    mapping = grammarCfg.cmd.map
    extras = [
        IntegerRef("n", 1, 11),
        IntegerRef("num", 0, 10000),
        Dictation("text"),
        Dictation("text2"),
        Choice("char", specialCharMap),
        Choice("letters", letterMap),
    ]
    defaults = {
        "n": 1,
    }
