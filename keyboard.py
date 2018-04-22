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
from aenea import (
    Grammar,
    MappingRule,
    Text,
    Key,
    Mimic,
    Function,
    Dictation,
    Choice,
    Window,
    Config,
    Section,
    Item,
    IntegerRef,
    Alternative,
    RuleRef,
    Repetition,
    CompoundRule,
    AppContext,
)

from dragonfly.actions.keyboard import keyboard
from dragonfly.actions.typeables import typeables
if 'semicolon' not in typeables:
    typeables["semicolon"] = keyboard.get_typeable(char=';')


release = Key("shift:up, ctrl:up, alt:up, win:up")


def cancel_and_sleep(text=None, text2=None):
    """Used to cancel an ongoing dictation and puts microphone to sleep.

    This method notifies the user that the dictation was in fact canceled,
     a message in the Natlink feedback window.
    Then the the microphone is put to sleep.
    Example:
    "'random mumbling go to sleep'" => Microphone sleep.

    """
    print("* Dictation canceled. Going to sleep. *")
    setMicState("sleeping")


# For repeating of characters.
specialCharMap = {
    "(bar|pipe)": "|",
    "(dash|minus|hyphen)": "-",
    "(dot|period)": ".",
    "dit": ",",
    "backslash": "\\",
    "rail": "_",
    "splat": "*",
    "colon": ":",
    "semi": ";",
    "at": "@",
    "hat": "^",    
    "[double] quote": '"',
    "smote": "'",
    "pound": "#",
    "cash": "$",
    "percy": "%",
    "amp": "&",
    "slash": "/",
    "equal": "=",
    "cross": "+",
    "bang": "!",
    "backtick": "`",
    "tilde": "~",
    "quest": "?",
    "left brace": "{",
    "right brace": "}",
    "bend": "(",
    "rend": ")",
    "ace": "[",
    "race": "]",
    "angle": "<",
    "rangle": ">",
}

# Modifiers for the press-command.
modifierMap = {
    "alt": "a",
    "control": "c",
    "shift": "s",
    "super": "w",
}

# Modifiers for the press-command, if only the modifier is pressed.
singleModifierMap = {
    "alt": "alt",
    "control": "ctrl",
    "shift": "shift",
    "super": "win",
}

letterMap = {
    "arch": "a",
    "brav": "b",
    "cork": "c",
    "delta": "d",
    "echo": "e",
    "fox": "f",
    "gang": "g",
    "hoop": "h",
    "ice": "i",
    "juice": "j",
    "kilo": "k",
    "lima": "l",
    "mike": "m",
    "nike": "n",
    "osh": "o",
    "pope": "p",
    "quack": "q",
    "rho": "r",
    "soy": "s",
    "tau": "t",
    "uni": "u",
    "van": "v",
    "whisk": "w",
    "rex": "x",
    "yoke": "y",
    "zed": "z",
}

# generate uppercase versions of every letter
upperLetterMap = {}
for letter in letterMap:
    upperLetterMap["(upper|sky) " + letter] = letterMap[letter].upper()
letterMap.update(upperLetterMap)

numberMap = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

controlKeyMap = {
    "left": "left",
    "right": "right",
    "up": "up",
    "down": "down",
    "page up": "pgup",
    "page down": "pgdown",
    "home": "home",
    "end": "end",
    "space": "space",
    "(enter|return)": "enter",
    "escape": "escape",
    "tab": "tab",
    "backspace": "backspace"
}

# F1 to F12. (do these actually work?)
functionKeyMap = {
    'F one': 'f1',
    'F two': 'f2',
    'F three': 'f3',
    'F four': 'f4',
    'F five': 'f5',
    'F six': 'f6',
    'F seven': 'f7',
    'F eight': 'f8',
    'F nine': 'f9',
    'F ten': 'f10',
    'F eleven': 'f11',
    'F twelve': 'f12',
}

pressKeyMap = {}
pressKeyMap.update(letterMap)
pressKeyMap.update(numberMap)
pressKeyMap.update(controlKeyMap)
pressKeyMap.update(functionKeyMap)


def handle_word(text):
    #words = map(list, text)
    #print text
    words = str(text).split()
    print 'word (', words, ')'
    if len(words) > 0:
        Text(words[0]).execute()
        if len(words) > 1:
            Mimic(' '.join(words[1:])).execute()


grammarCfg = Config("multi edit")
grammarCfg.cmd = Section("Language section")
grammarCfg.cmd.map = Item(
    {
        ### Navigation ###
        "up [<n>]": Key("up:%(n)d"),
        "down [<n>]": Key("down:%(n)d"),
        "left [<n>]": Key("left:%(n)d"),
        "right [<n>]": Key("right:%(n)d"),
        "pinch [<n>]": Key("pgup:%(n)d"),
        "page [<n>]": Key("pgdown:%(n)d"),
        "left [<n>] (word|words)": Key("c-left/3:%(n)d/10"),
        "right [<n>] (word|words)": Key("c-right/3:%(n)d/10"),
        "home": Key("home"),
        "lend": Key("end"),
        "lendit": Key("end, comma"),
        "doc home": Key("c-home/3"),
        "doc end": Key("c-end/3"),

        ### Selections ###
        "grab <n>": release + Key("shift:down, right:%(n)d, shift:up"),
        "take <n>": release + Key("shift:down, left:%(n)d, shift:up"),
        "take <n> (line|lines)": release + Key("end, shift:down, home, up:%(n)d, home, shift:up"),
        "grab <n> (line|lines)": release + Key("home, shift:down, down:%(n)d, end, shift:up"),
        "grab <n> (word|words)": release + Key("shift:down, c-right:%(n)d, shift:up"),
        "take <n> (word|words)": release + Key("shift:down, c-left:%(n)d, shift:up"),
        "(take|grab) word": Key("c-left, sc-right"),
        "(take|grab) home": release + Key("shift:down, home, shift:up"),
        "(take|grab) end": release + Key("shift:down, end, shift:up"),
        "(take|grab) line": release + Key("home, s-end"),
        "(take|grab) all": release + Key("c-a/3"),

        ### Functional keys ###
        "act": Key("escape"),
        "space": release + Key("space"),
        "space [<n>]": release + Key("space:%(n)d"),
        "slap [<n>]": release + Key("enter:%(n)d"),
        "slide [<n>]": release + Key("end, enter:%(n)d"),
        "tab [<n>]": Key("tab:%(n)d"),
    
         ### Deletions ###
        "scratch [<n>]": release + Key("backspace:%(n)d"),
        "chuck [<n>]": Key("del/3:%(n)d"),
        "whack [<n>]": Key("shift:down, c-left/3:%(n)d/10, del, shift:up"),
        "bump [<n>]": Key("shift:down, c-right/3:%(n)d/10, del, shift:up"),      
        "scratch [this] line": Key("home, s-end, del"),  # @IgnorePep8
        "chuck [this] line": Key("home:2, s-end, backspace:2"),

        ### Common functions ###
        "paste [that]": Key("c-v/3"),
        "copy [that]": Key("c-c/3"),
        "cut [that]": release + Key("c-x/3"),
        "undo": release + Key("c-z/3"),
        "undo <n> [times]": release + Key("c-z/3:%(n)d"),
        "redo": release + Key("c-y/3"),
        "redo <n> [times]": release + Key("c-y/3:%(n)d"),
        "save": release + Key("c-s"),

        ### Keypresses ###
        "[(hold|press)] meta": Key("win:down/3"),
        "release win": Key("win:up"),        
        "[(hold|press)] alt": Key("alt:down/3"),
        "release alt": Key("alt:up"),
        "[(hold|press)] shift": Key("shift:down/3"),
        "release shift": Key("shift:up"),
        "[(hold|press)] control": Key("ctrl:down/3"),
        "release control": Key("ctrl:up"),
        "release [all]": release,
        "press key <pressKey>": Key("%(pressKey)s"),

        ### Closures ###
        "angles": Key("langle, rangle, left/3"),
        "squares": Key("lbracket, rbracket, left/3"),
        "braces": Key("lbrace, rbrace, left/3"),
        "parens": Key("lparen, rparen, left/3"),
        "quotes": Key("dquote/3, dquote/3, left/3"),
        "single quotes": Key("squote, squote, left/3"),
        "backticks": Key("backtick:2, left/3"),
        "pipes": Key("bar:2, left"),

        ### Multiple characters ###
        "double <char>": Text("%(char)s%(char)s"),
        "triple <char>": Text("%(char)s%(char)s%(char)s"),
        "double escape": Key("escape, escape"),  # Exiting menus.
        
        ### Punctuation and separation ###
        "colon [<n>]": Key("colon/2:%(n)d"),
        "(semi-colon|semicolon|semi) [<n>]": Key("semicolon/2:%(n)d"),
        "dit [<n>]": Key("comma/2:%(n)d"),
        "drip": Key("comma, space"),
        "drip drop": Key("comma, enter"),
        "(dot|period) [<n>]": Key("dot/2:%(n)d"),
        "dash [<n>]": Key("hyphen/2:%(n)d"),
        "rail [<n>]": Key("underscore/2:%(n)d"),

        ### Letters, Numbers, and Words ###
        "<letters>": Text("%(letters)s"),
        "<char>": Text("%(char)s"),
        'word <text>': Function(handle_word),
        'number <num>': Text("%(num)d"),

        ### Misc ###
        # Text corrections.
        "(add|fix) missing space": Key("c-left/3, space, c-right/3"),
        "(delete|remove) (double|extra) (space|whitespace)": Key("c-left/3, backspace, c-right/3"),  # @IgnorePep8
        "(delete|remove) (double|extra) (type|char|character)": Key("c-left/3, del, c-right/3"),  # @IgnorePep8
        # Microphone sleep/cancel started dictation.
        "[<text>] snore [<text2>]": Function(cancel_and_sleep),  # @IgnorePep8
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
        IntegerRef("n", 1, 100),
        IntegerRef("num", 0, 1000000),
        Dictation("text"),
        Dictation("text2"),
        Choice("char", specialCharMap),
        Choice("letters", letterMap),
        Choice("modifier1", modifierMap),
        Choice("modifier2", modifierMap),
        Choice("modifierSingle", singleModifierMap),
        Choice("pressKey", pressKeyMap),
    ]
    defaults = {
        "n": 1,
    }


