# module for dictating words and basic sentences
#
# (based on the multiedit module from dragonfly-modules project)
# (heavily modified)
# (the original copyright notice is reproduced below)
#
# (c) Copyright 2008 by Christo Butcher
# Licensed under the LGPL, see <http://www.gnu.org/licenses/>
#

import aenea
import aenea.misc
import aenea.vocabulary
import aenea.configuration
import lib.format
import re

from aenea import *

formatList = {
    'pascal': 'proper',
    'camel': 'camel',
    'relpath': 'relpath',
    'abspath': 'abspath',
    'score': 'score',
    'speak': 'sentence',
    'scoperesolve': 'scoperesolve',
    'jumble': 'jumble',
    'dotword': 'dotword',
    'dashword': 'dashword',
    'say': 'natword',
    'snake': 'snakeword',
    'titlecase': 'title'
}

formatSpecs = "(%s)" % " | ".join(formatList.keys())

lastFormatRuleLength = 0
lastFormatRuleWords = []


class NopeFormatRule(CompoundRule):
    spec = ('nope')

    def value(self, node):
        global lastFormatRuleLength
        print "erasing previous format of length", lastFormatRuleLength
        return Key('backspace:' + str(lastFormatRuleLength))


class ReFormatRule(CompoundRule):
    spec = ('that was [upper | natural]' + formatSpecs)

    def value(self, node):
        global lastFormatRuleWords
        words = lastFormatRuleWords
        words = node.words()[2:] + lastFormatRuleWords
        print words

        uppercase = words[0] == 'upper'
        lowercase = words[0] != 'natural'

        if lowercase:
            words = [word.lower() for word in words]
        if uppercase:
            words = [word.upper() for word in words]

        words = [word.split('\\', 1)[0].replace(
            '-', '').replace(' ', '') for word in words]
        if words[0].lower() in ('upper', 'natural'):
            del words[0]

        function = getattr(lib.format, 'format_%s' %
                           formatList[words[0].lower()])
        formatted = function(words[1:])

        formatted = re.sub(u"\u2013", "-", formatted)

        global lastFormatRuleLength
        lastFormatRuleLength = len(formatted)
        return Text(formatted)


class FormatRule(CompoundRule):
    spec = '[upper | natural] ' + formatSpecs + ' [<dictation>] [bomb]'
    extras = [Dictation(name='dictation')]

    def value(self, node):
        words = node.words()
        print "format rule:", words

        uppercase = words[0] == 'upper'
        lowercase = words[0] != 'natural'

        if lowercase:
            words = [word.lower() for word in words]
        if uppercase:
            words = [word.upper() for word in words]

        words = [word.split('\\', 1)[0].replace(
            '-', '').replace(' ', '') for word in words]
        if words[0].lower() in ('upper', 'natural'):
            del words[0]

        bomb = None
        if 'bomb' in words:
            bomb_point = words.index('bomb')
            if bomb_point+1 < len(words):
                bomb = words[bomb_point+1:]
            words = words[: bomb_point]

        function = getattr(lib.format, 'format_%s' %
                           formatList[words[0].lower()])
        formatted = function(words[1:])
        global lastFormatRuleWords
        lastFormatRuleWords = words[1:]

        global lastFormatRuleLength
        lastFormatRuleLength = len(formatted)

        formatted = re.sub(u"\u2013", "-", formatted)

        # empty formatted causes problems here
        print "  ->", formatted
        if bomb != None:
            return Text(formatted) + Mimic(' '.join(bomb))
        else:
            return Text(formatted)
