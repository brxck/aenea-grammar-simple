specialCharMap = {
    "(bar|pipe)": "|",
    "(dash|minus|hyphen)": "-",
    "(dot|period)": ".",
    "dit": ",",
    "backslash": "\\",
    "rail": "_",
    "splat": "*",
    "cat": ":",
    "semi": ";",
    "abby": "@",
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
    "burl": "{",
    "curl": "}",
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
    "beer": "b",
    "cork": "c",
    "dealt": "d",
    "echo": "e",
    "fox": "f",
    "gang": "g",
    "heart": "h",
    "ice": "i",
    "juke": "j",
    "kilo": "k",
    "luck": "l",
    "mike": "m",
    "nike": "n",
    "osh": "o",
    "pope": "p",
    "quack": "q",
    "ram": "r",
    "soy": "s",
    "torque": "t",
    "uncle": "u",
    "van": "v",
    "whisk": "w",
    "rex": "x",
    "yam": "y",
    "zed": "z",
}

# generate uppercase versions of every letter
upperLetterMap = {}
for letter in letterMap:
    upperLetterMap["(upper|sky) " + letter] = letterMap[letter].upper()

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
# (no, I don't think so!)
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
