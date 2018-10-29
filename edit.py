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

import time
from natlink import setMicState
from aenea import *

from lib.maps import (
    specialCharMap,
    letterMap,
    upperLetterMap,
    numberMap,
)

from lib import sound


def pause():
    time.sleep(1)


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
        "hop [<nav>]": Key("up:%(nav)d"),
        "dove [<nav>]": Key("down:%(nav)d"),
        "lore [<nav>]": Key("left:%(nav)d"),
        "role [<nav>]": Key("right:%(nav)d"),
        "lorex [<n>]": Key("c-left:%(n)d"),
        "rolex [<n>]": Key("c-right:%(n)d"),
        "pinch [<n>]": Key("pgup:%(n)d"),
        "punch [<n>]": Key("pgdown:%(n)d"),
        "stark": Key("home"),
        "lend": Key("end"),
        "lendit": Key("end, comma"),
        "dockit": Key("c-home"),
        "dockex": Key("c-end"),
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
        "(take|grab) all": Key("c-a"),

        ### Whitespace ###
        "space": Key("space"),
        "space [<n>]": Key("space:%(n)d"),
        "slap [<n>]": Key("enter:%(n)d"),
        "slide [<n>]": Key("end, enter:%(n)d"),
        "slip [<n>]": Key("home, enter:%(n)d, up:%(n)d"),
        "kite [<n>]": Function(pause) + Key("tab:%(n)d"),
        "tyke [<n>]": Key("s-tab:%(n)d"),

        ### Deletions ###
        "scratch [<n>]": Key("backspace:%(n)d"),
        "chuck [<n>]": Key("del:%(n)d"),
        "whack [<n>]": Key("c-backspace:%(n)d"),
        "bump [<n>]": Key("c-delete:%(n)d"),
        "scratch line": Key("home, s-end, del"),
        "chuck line": Key("home:2, s-end, backspace:2"),

        ### Functions ###
        "paste": Key("c-v"),
        "copy": Key("c-c"),
        "cut": Key("c-x"),
        "undo [<n>]": Key("c-z:%(n)d"),
        "redo [<n>]": Key("c-y:%(n)d"),
        "stamp": Key("c-s"),

        ### Closures ###
        "angles": Key("langle, rangle, left"),
        "squares": Key("lbracket, rbracket, left"),
        "braces": Key("lbrace, rbrace, left"),
        "graces": Key("lbrace, space:2, rbrace, left:2"),
        "parens": Key("lparen, rparen, left"),
        "quotes": Key("dquote, dquote, left"),
        "smotes": Key("squote, squote, left"),
        "ticks": Key("backtick:2, left"),
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
        "open folder": Key("c-k, c-o"),
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
        "doopit": Key("c-c, cs-enter, c-v, backspace"),
        "doopex": Key("c-c, c-enter, c-v, backspace"),
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
        "cursit": Key("a-t"),
        "cursex": Key("a-b"),
        "blockit": Key("a-home"),
        "blockex": Key("a-end"),
        "take block": Key("end, sa-home"),
        "grab block": Key("home, sa-end"),

        ### Window ###
        "code zen": Key("c-k, z"),
        "code center": Key("c-k, c-l"),
        "code bar": Key("c-b"),
        "code files": Key("cs-j"),
        "code outline": Key("cs-o"),
        "code source": Key("cs-g"),
        "code debug": Key("cs-d"),
        "code extensions": Key("cs-x"),
        "code settings": Key("c-comma"),
        "code shortcuts": Key("c-k, c-s"),
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
        IntegerRef("nav", 1, 40),
        IntegerRef("num", 0, 10000),
        Dictation("text"),
        Dictation("text2"),
        Choice("char", specialCharMap),
        Choice("letters", letterMap),
    ]
    defaults = {
        "n": 1,
    }
