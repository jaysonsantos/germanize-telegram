#!/usr/bin/env python3
# coding: utf-8
"""Spell a name in german.

Taken from http://www.buchstabieralphabet.org/
           (Das offizielle Buchstabieralphabet - deutsch und international)
"""
import sys

MAPPED = {
    'a': 'Anton',
    'b': 'Berta',
    'c': 'Cäsar',
    'ch': 'Charlotte',
    'd': 'Dora',
    'e': 'Emil',
    'f': 'Friedrich',
    'g': 'Gustav',
    'h': 'Heinrich',
    'i': 'Ida',
    'j': 'Julius',
    'k': 'Kaufmann',
    'l': 'Ludwig',
    'm': 'Martha',
    'n': 'Nordpol',
    'o': 'Otto',
    'p': 'Paula',
    'q': 'Quelle',
    'r': 'Richard',
    's': 'Samuel',
    'sch': 'Schule',
    't': 'Theodor',
    'u': 'Ulrich',
    'v': 'Viktor',
    'w': 'Wilhelm',
    'x': 'Xanthippe',
    'y': 'Ypsilon',
    'z': 'Zacharias',
    'ß': 'Eszett',
    'ä': 'Ärger',
    'ö': 'Ökonom',
    'ü': 'Übermut'
}


def find_key(name, i):
    """Find key trying with 3, 2 and the 1 characters."""
    for offset in (3, 2, 1):
        key = name[i:i + offset]
        if key in MAPPED:
            i += offset
            return i, '{} - {}'.format(key, MAPPED[key])

    return i + 1, None


def spell(name):
    """Spell a name."""
    if not name:
        print('No name provided')
        exit(1)

    print('Spelling {}'.format(name))
    buffer = []

    i = 0
    while i < len(name):
        if name[i] == ' ':
            i += 1
            print('')
            continue
        i, tmp = find_key(name, i)
        if tmp:
          buffer.append(tmp)
    return '\n'.join(buffer)

