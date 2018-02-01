from .rules import SYMBOLS


class StrengthMeter:
    def __init__(self, password=None):
        self.__password = password if password else ''
        self.__length = self.__calculate_length()
        self.__uniqueness = self.__calculate_uniqueness()
        self.__score = self.__calculate_score()

    def __calculate_length(self):
        return len(self.__password)

    def __calculate_uniqueness(self):
        return len(set(self.__password))

    @property
    def __lowercase_only(self):
        for char in self.__password:
            if not char.islower():
                return False
        return True

    @property
    def __uppercase_only(self):
        for char in self.__password:
            if not char.isupper():
                return False
        return True

    @property
    def __numbers_only(self):
        for char in self.__password:
            if not char.isdigit():
                return False
        return True

    def __contain_lowercase(self):
        for char in self.__password:
            if char.islower():
                return True
        return False

    def __contain_uppercase(self):
        for char in self.__password:
            if char.isupper():
                return True
        return False

    def __contain_number(self):
        for char in self.__password:
            if char.isdigit():
                return True
        return False

    def __contain_symbol(self):
        for char in self.__password:
            if char in SYMBOLS:
                return True
        return False

    def __calculate_score(self):
        score = 0
        try:
            score += self.__uniqueness / self.__length * 28
        except ZeroDivisionError:
            pass

        if self.__contain_lowercase():
            score += 10
        if self.__contain_uppercase():
            score += 10
        if self.__contain_number():
            score += 10
        if self.__contain_symbol():
            score += 10

        if self.__lowercase_only \
                or self.__uppercase_only \
                or self.__numbers_only:
            score = 0

        score += self.__calculate_length_score()

        if score < 0:
            score = 0
        return round(score, 2)

    def __calculate_length_score(self):
        if self.__length < 8:
            return 0
        elif self.__length > 32:
            return 32
        else:
            return self.__length

    @property
    def score(self):
        return self.__score

    @property
    def strength(self):
        if self.__score < 33:
            return "Weak password"
        elif 33.3 < self.__score < 66:
            return "Medium password"
        else:
            return "Strong password"

    def visualize_strength(self, width=10):
        num = round(self.__score / 100 * width)
        return "[{0: <{width}}]".format("#" * num, width=width)

    def print_stats(self):
        print("Password: '{}'".format(self.__password))
        print("Score: {}%".format(self.score))
        print("Result: {}".format(self.strength))
        print("Visual: {}".format(self.visualize_strength()))
