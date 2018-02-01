import random

from .rules import *


class Generator:
    def __init__(self, length=8, rules=None, restrictions=None):
        self.length = length

        if not rules:
            self.rules = [WITH_LOWERCASE]
        else:
            if not isinstance(rules, list):
                self.rules = [rules]
            else:
                self.rules = rules

        if not restrictions:
            self.restrictions = []
        else:
            if not isinstance(restrictions, list):
                self.restrictions = [restrictions]
            else:
                self.restrictions = restrictions

    def __generate_password_proto(self):
        pw = []
        for i in range(0, self.length, len(self.rules)):
            random.shuffle(self.rules)
            pw.extend(self.rules)
        return "".join([str(i) for i in pw])

    def generate(self):
        password = ""
        for i in self.__generate_password_proto():
            if i == '0':
                table = LOWER_ALPHA
            elif i == '1':
                table = UPPER_ALPHA
            elif i == '2':
                table = NUMBERS
            else:
                table = SYMBOLS

            # print("Before restrictions: {}".format(table))
            if 11 in self.restrictions:
                table = sorted(list(set(table) - set(MEDIUM_SIMILAR)))
            if 12 in self.restrictions:
                table = sorted(list(set(table) - set(VERY_SIMILAR)))
            if 13 in self.restrictions:
                table = sorted(list(set(table) - set(AMBIGUOUS)))
            # print("After restrictions: {}".format(table))
            rand_char = table[random.randint(0, len(table) - 1)]
            password += rand_char
        return password
