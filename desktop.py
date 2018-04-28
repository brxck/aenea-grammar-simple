# Generic desktop control

from aenea import *

class DesktopRule(MappingRule):
    mapping = {
        ### Windows ###
        "snap screen": Key("w-up"),
        "snap win": Key("w-down"),
        "snap left": Key("w-left"),
        "snap right": Key("w-right"),    
        "snap close": Key("c-w"),
        "snap new": Key("c-n"),        
        "snap quit": Key("c-q"),    
        "snap full": Key("f11"),
        "flip [<n>]": Key("a-escape:%(n)d"),
        "flop [<n>]": Key("sa-escape:%(n)d"),
        "flap [<n>]": Key("a-tab:%(n)d"),

        ### Common controls ###
        "save": Key("c-s"),
        "browse back [<n>]": Key("a-left/15:%(n)d"),
        "browse forward [<n>]": Key("a-right/15:%(n)d"),
        "find in page": Key("c-f"),
        "find previous [<n>]": Key("s-f3/10:%(n)d"),
        "find next [<n>]": Key("f3/10:%(n)d"),

        ### Workspaces ###
        "woke <n>": Key("caw-%(n)d"),
        "wix [<n>]": Key("ca-right:%(n)d"),
        "wox [<n>]": Key("ca-left:%(n)d"),
        "snap wix [<n>]": Key("sca-right:%(n)d"),
        "snap wox [<n>]": Key("sca-left:%(n)d"), 
        "snap woke <n>": Key("scaw-%(n)d"),

        ### Albert ###
        "spot [<text>]": Key("scaw-space/3") + Text("%(text)s"),
        "spike [<text>]": Key("scaw-space/3") + Text("%(text)s") + Key("enter"),

        ### Media ###
        # "[toggle] mute": Key("volmute"),
        # "louder": Key("volup"),
        # "softer": Key("voldown"),    
        # "next track": Key("tracknext"),
        # "last track": Key("trackprev"),
        # "(play|pause)": Key("playpause"),
    }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 100),
    ]
    defaults = {
        "n": 1,
    }
