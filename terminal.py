# Contextual grammar for web browser control

from lib.maps import letterMap

from aenea import *


class TerminalRule(MappingRule):
    mapping = {
        "term kill": Key("c-c"),
        "term clear": Key("c-l"),
        "term close": Key("c-d"),
        "term switch": Key("control:down, x:2, control:up"),
        "term copy": Key("cs-c"),
        "term paste": Key("cs-v"),
        "term revert": Key("a-r"),

        "sudo": Text("sudo "),
        "m k dir": Text("mkdir "),
        "h top": Text("htop"),
        "beats": Text("beets"),
        "beer me some tunes": Text("ncmpcpp") + Key("enter"),

        "npm": Text("npm "),
        "npm run": Text("npm run "),

        "git status": Text("git status"),
        "git add": Text("git add "),
        "git commit": Text('git commit -m ""') + Key("left"),
        "git push": Text("git push "),
        "git push origin master": Text("git push origin master"),
        "git push origin": Text("git push origin "),
        "git push upstream": Text("git push -u "),
        "git pull": Text("git pull"),
        "git log": Text("git log"),
        "git log one line": Text("git log --oneline"),
        "git diff": Text("git diff"),
        "git clone": Text("git clone "),
        "git create": Text("git create"),
        "git init": Text("git init"),
        "git remote add": Text("git remote add "),
        "git remote remove": Text("git remote remove "),
        "git remote list": Text("git remote -v"),
        "git checkout branch": Text("git checkout -b "),
        "git checkout": Text("git checkout "),
        "git branch": Text("git branch"),
        "git branch delete": Text("git branch -d "),
        "git merge": Text("git merge "),

        "R D B schema load": Text("rails db:schema:load"),

        "four zeros": Text("0.0.0.0")
    }
    extras = []
    defaults = {}
