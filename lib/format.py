# This file is part of Aenea
#
# Aenea is free software: you can redistribute it and/or modify it under
# the terms of version 3 of the GNU Lesser General Public License as
# published by the Free Software Foundation.
#
# Aenea is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public
# License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with Aenea.  If not, see <http://www.gnu.org/licenses/>.
#
# Copyright (2014) Alex Roper
# Alex Roper <alex@aroper.net>

import string


def format_snakeword(text):
    formatted = text[0][0].upper()
    formatted += text[0][1:]
    formatted += ('_' if len(text) > 1 else '')
    formatted += format_score(text[1:])
    return formatted


def format_score(text):
    return '_'.join(text)


def format_camel(text):
    groups = split_dots(text)
    formatted = ''
    for group in groups:
        formatted += camelize(group)
    return formatted


def format_proper(text):
    return ''.join(word.capitalize() for word in text)


def format_relpath(text):
    return '/'.join(text)


def format_abspath(text):
    return '/' + format_relpath(text)


def format_scoperesolve(text):
    return '::'.join(text)


def format_jumble(text):
    return ''.join(text)


def format_dotword(text):
    return '.'.join(text)


def format_dashword(text):
    return '-'.join(text)


def format_natword(text):
    return ''.join([('' if c in string.punctuation else ' ')+c for c in text])


def format_sentence(text):
    groups = split_dots(text)
    for group in groups:
        group = group[0].capitalize() + group[1:]
        group = ' '.join(group)
    return ' '.join(groups)


def split_dots(text):
    if '.' in text:
        split_point = text.index('.')
        return [text[:split_point + 1]] + split_dots(text[split_point + 1:])
    else:
        return [text]


def camelize(text):
    return text[0] + ''.join([word[0].upper() + word[1:] for word in text[1:]])
