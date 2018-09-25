#!/usr/bin/env python3
# coding: utf-8
"""Spell a name in german.

Taken from http://www.buchstabieralphabet.org/
           (Das offizielle Buchstabieralphabet - deutsch und international)
"""
MAPPED = {
    "0": (None, "null"),
    "1": (None, "eins"),
    "2": (None, "zwei"),
    "3": (None, "drei"),
    "4": (None, "vier"),
    "5": (None, "fünf"),
    "6": (None, "sechs"),
    "7": (None, "sieben"),
    "8": (None, "acht"),
    "9": (None, "neun"),
    "a": ("a", "Anton"),
    "ä": ("ae", "Ärger"),
    "b": ("bê", "Berta"),
    "c": ("tsê", "Cäsar"),
    "ch": (None, "Charlotte"),
    "d": ("dê", "Dora"),
    "e": ("e", "Emil"),
    "f": ("eff", "Friedrich"),
    "g": ("guê", "Gustav"),
    "h": ("rá", "Heinrich"),
    "i": ("i", "Ida"),
    "j": ("iot", "Julius"),
    "k": ("ká", "Kaufmann"),
    "l": ("el", "Ludwig"),
    "m": ("em", "Martha"),
    "n": ("en", "Nordpol"),
    "o": ("o", "Otto"),
    "ö": ("oe", "Ökonom"),
    "p": ("pê", "Paula"),
    "q": ("ku", "Quelle"),
    "r": ("arr", "Richard"),
    "s": ("és", "Samuel"),
    "sch": (None, "Schule"),
    "ß": (None, "Eszett"),
    "t": ("tê", "Theodor"),
    "u": ("u", "Ulrich"),
    "ü": ("ue", "Übermut"),
    "v": ("fau", "Viktor"),
    "w": ("vê", "Wilhelm"),
    "x": ("ics", "Xanthippe"),
    "y": ("úpsilon", "Ypsilon"),
    "z": ("tsét", "Zacharias"),
}


def find_key(name, i):
    """Find key trying with 3, 2 and the 1 characters."""
    for offset in (3, 2, 1):
        key = name[i : i + offset]
        if key in MAPPED:
            i += offset
            pronunciation, word = MAPPED[key]

            # For two or more letters, concat the individual pronunciation of each letter
            if not pronunciation and len(key) > 1:
                pronunciation = ", ".join([MAPPED.get(letter)[0] for letter in key])

            example = "'{}' von {}".format(pronunciation, word) if pronunciation else word
            return i, "{}: {}".format(key, example)

    return i + 1, None


def spell(name):
    """Spell a name."""
    if not name:
        print("No name provided")
        exit(1)

    print("Spelling {}:".format(name))
    buffer = []

    i = 0
    while i < len(name):
        if name[i] == " ":
            i += 1
            buffer.append("")
            continue
        i, tmp = find_key(name, i)
        if tmp:
            buffer.append(tmp)
    return "\n".join(buffer)
