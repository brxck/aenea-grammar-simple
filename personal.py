# Personal commands, don't push to Github.

from aenea import (
    Key,
    Dictation,
    Text,
    MappingRule,
    IntegerRef,
    Grammar,
    Choice
)


class PersonalRule(MappingRule):
    mapping = {

        "Brock McElroy": Text("Brock McElroy"),
        "Brock": Text("Brock"),
        "McElroy": Text("McElroy"),

        "my protonmail": Text("brxck@protonmail.com"),
        "my short protonmail": Text("brxck@pm.me"),
        "my gmail": Text("tbrockmc@gmail.com"),

        "my address one": Text("4253 E. Flower St."),
        "my address two": Text("Apt. 12"),

        "my handle": Text("brxck"),

        "my website": Text("brockmcelroy.com"),
        "my github": Text("github.com/brxck"),
    }

    extras = []
