# Flyweight
# Space optimization technique
# - Motivation
#   - Avoid redundancy when sorting data
#   - E.G MMORPG Plenty of users with identical first/last names
#   - No sense in storing same first/last name over and over again
#   - Store a list of names and references to them


# User Names
import string
import random


class User:
    def __init__(self, name):
        self.name = name


class User2:
    """This class allows us to store all the possible strings just once
    in the class definition, and each of the users will have the index
    of those strings, so instead of storing thousands of strings
    it will keep each letter just once and the names will keep the index

    Returns:
        _type_: _description_
    """

    strings = []

    def __init__(self, full_name):
        def get_or_add(s):
            if s in self.strings:
                return self.strings.index(s)
            else:
                self.strings.append(s)
                return len(self.strings) - 1

        self.names = [get_or_add(x) for x in full_name.split(" ")]

    def __str__(self):
        return " ".join([self.strings[x] for x in self.names])


def random_string():
    chars = string.ascii_lowercase
    return "".join([random.choice(chars) for _ in range(8)])


if __name__ == "__main__":
    users = []
    first_names = [random_string() for _ in range(100)]
    last_names = [random_string() for _ in range(100)]

    for first in first_names:
        for last in last_names:
            users.append(User2(f"{first} {last}"))
    print(users[0])


# Text Formatting


class FormattedText:
    def __init__(self, plain_text):
        self.plain_text = plain_text
        self.caps = [False] * len(plain_text)

    def capitalize(self, start, end):
        for i in range(start, end):
            self.caps[i] = True

    def __str__(self):
        result = []
        for i in range(len(self.plain_text)):
            c = self.plain_text[i]
            result.append(c.upper() if self.caps[i] else c)
        return "".join(result)


class BetterFormattedText:
    def __init__(self, plain_text):
        self.plain_text = plain_text
        self.formatting = []

    class TextRange:
        def __init__(self, start, end, capitalize=False):
            self.start = start
            self.end = end
            self.capitalize = capitalize

        def covers(self, position):
            return self.start <= position <= self.end

    def get_range(self, start, end):
        text_range = self.TextRange(start, end)
        self.formatting.append(text_range)
        return text_range

    def __str__(self):
        result = []
        for i in range(len(self.plain_text)):
            c = self.plain_text[i]
            for r in self.formatting:
                if r.covers(i) and r.capitalize:
                    c = c.upper()
            result.append(c)
        return "".join(result)


if __name__ == "__main__":
    text = "This is a brave new world"
    ft = FormattedText(text)
    ft.capitalize(10, 15)
    print(ft)

    bft = BetterFormattedText(text)
    bft.get_range(16, 19).capitalize = True
    print(bft)


# Exercise


class Sentence:
    def __init__(self, plain_text):
        self.plain_text = plain_text
        self.words = [self.Word(text) for text in self.plain_text.split(" ")]

    class Word:
        def __init__(self, text):
            self.text = text
            self.capitalize = False

        def __str__(self):
            if self.capitalize:
                return self.text.upper()
            else:
                return self.text

    def __getitem__(self, key):
        return self.words[key]

    def __str__(self):
        return " ".join(str(i) for i in self.words)


if __name__ == "__main__":
    sentence = Sentence("hello world")
    sentence[1].capitalize = True
    print(sentence)
