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
    Mouse,
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

from lib.maps import (
    specialCharMap,
    # modifierMap,
    # singleModifierMap,
    letterMap,
    upperLetterMap,
    numberMap,
    # controlKeyMap,
    # functionKeyMap,
)

from lib import sound

release = Key("shift:up, ctrl:up, alt:up, win:up")


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
# pressKeyMap = {}
# pressKeyMap.update(letterMap)
# pressKeyMap.update(numberMap)
# pressKeyMap.update(controlKeyMap)
# pressKeyMap.update(functionKeyMap)


def handle_word(text):
    #words = map(list, text)
    #print text
    words = str(text).split()
    print 'word (', words, ')'
    if len(words) > 0:
        Text(words[0]).execute()
        if len(words) > 1:
            Mimic(' '.join(words[1:])).execute()


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

        ### Selections ###
        "grab <n>": release + Key("shift:down, right:%(n)d, shift:up"),
        "take <n>": release + Key("shift:down, left:%(n)d, shift:up"),
        "take <n> (line|lines)": release + Key("end, shift:down, home, up:%(n)d, shift:up"),
        "grab <n> (line|lines)": release + Key("home, shift:down, down:%(n)d, shift:up"),
        "grab <n> words": release + Key("shift:down, c-right:%(n)d, shift:up"),
        "take <n> words": release + Key("shift:down, c-left:%(n)d, shift:up"),
        "(take|grab) word": Key("c-left, sc-right"),
        "(take|grab) home": release + Key("shift:down, home, shift:up"),
        "(take|grab) end": release + Key("shift:down, end, shift:up"),
        "(take|grab) line": release + Key("home, s-end"),
        "(take|grab) all": release + Key("c-a/3"),

        ### Functional keys ###
        "cape": Key("escape"),
        "space": release + Key("space"),
        "space [<n>]": release + Key("space:%(n)d"),
        "slap [<n>]": release + Key("enter:%(n)d"),
        "slide [<n>]": release + Key("end, enter:%(n)d"),
        "slip [<n>]": release + Key("home, enter:%(n)d, up:%(n)d"),
        "tim [<n>]": Key("tab:%(n)d"),
        "mitt [<n>]": Key("s-tab:%(n)d"),

        ### Deletions ###
        "scratch [<n>]": release + Key("backspace:%(n)d"),
        "chuck [<n>]": Key("del/3:%(n)d"),
        "whack [<n>]": Key("c-backspace:%(n)d"),
        "bump [<n>]": Key("c-delete:%(n)d"),
        "scratch line": Key("home, s-end, del"),  # @IgnorePep8
        "chuck line": Key("home:2, s-end, backspace:2"),

        ### Common functions ###
        "paste": Key("c-v/3"),
        "copy": Key("c-c/3"),
        "cut": release + Key("c-x/3"),
        "undo [<n>]": release + Key("c-z/3:%(n)d"),
        "redo [<n>]": release + Key("c-y/3:%(n)d"),
        "stamp": release + Key("c-s"),

        ### Keypresses ###
        # "[(hold|press)] meta": Key("win:down/3"),
        # "release win": Key("win:up"),
        # "[(hold|press)] alt": Key("alt:down/3"),
        # "release alt": Key("alt:up"),
        # "[(hold|press)] shift": Key("shift:down/3"),
        # "release shift": Key("shift:up"),
        # "[(hold|press)] control": Key("ctrl:down/3"),
        # "release control": Key("ctrl:up"),
        # "release [all]": release,
        # "press key <pressKey>": Key("%(pressKey)s"),

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

        ### Punctuation and separation ###
        "coy": Key("colon, space"),
        "drip": Key("comma, space"),
        "dot [<n>]": Key("dot/2:%(n)d"),
        "dash [<n>]": Key("hyphen/2:%(n)d"),
        "cat [<n>]": Key("colon:%(n)d"),
        "slash [<n>]": Key("slash:%(n)d"),
        "equit [<n>]": Key("equal:%(n)d"),

        ### Letters, Numbers, and Words ###
        "<letters>": Text("%(letters)s"),
        "<char>": Text("%(char)s"),
        'num <num>': Text("%(num)d"),
        # 'word <text>': Function(handle_word),

        ### Misc ###
        # Text corrections.
        # "(add|fix) missing space": Key("c-left/3, space, c-right/3"),
        # @IgnorePep8
        # "(delete|remove) (double|extra) (space|whitespace)": Key("c-left/3, backspace, c-right/3"),
        # @IgnorePep8
        # "(delete|remove) (double|extra) (type|char|character)": Key("c-left/3, del, c-right/3"),
        # Microphone sleep/cancel started dictation.
        # @IgnorePep8
        "[<text>] go to sleep [<text2>]": Function(cancel_and_sleep),
        "check one two": Function(test),

        ##########################
        ### Visual Studio Code ###
        ##########################

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
        "jump <num>": Key("c-g") + Text("%(num)d") + Key("enter"),
        "find def": Key("f12"),

        ### Editing ###
        "block comment": Key("sa-a"),
        "code comment": Key("c-slash"),
        "kite": Key("a:up/7000") + Key("tab"),
        "move higher [<n>]": Key("a-up:%(n)d"),
        "move lower [<n>]": Key("a-down:%(n)d"),
        "move in [<n>]": Key("c-rbracket:%(n)d"),
        "move out [<n>]": Key("c-lbracket:%(n)d"),
        "dupe it": Key("c-c/3, cs-enter, c-v/3, backspace"),
        "dupe ex": Key("c-c/3, c-enter, c-v/3, backspace"),
        "take others": Key("cs-l"),
        "take next [<n>]": Key("c-d:%(n)d"),
        "(take|grab) close": Key("cs-squote"),
        "peck [<n>]": Key("a-pgup:%(n)d"),
        "peek [<n>]": Key("a-pgdown:%(n)d"),

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
        # Choice("modifier1", modifierMap),
        # Choice("modifier2", modifierMap),
        # Choice("modifierSingle", singleModifierMap),
        # Choice("pressKey", pressKeyMap),
    ]
    defaults = {
        "n": 1,
    }
