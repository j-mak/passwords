import unittest
import re

import password.rules as rules
from password.generator import Generator


class ValidGeneratorTestCase(unittest.TestCase):
    def setUp(self):
        self.ESCAPED_SYMBOLS = re.escape("".join(rules.SYMBOLS))

    def test_generate_password_with_length_8_should_pass(self):
        generator = Generator(length=8)
        password = generator.generate()
        self.assertEqual(len(password), 8)

    def test_generate_password_that_contain_lowercase_only_should_pass(self):
        generator = Generator(length=64,
                              rules=[rules.WITH_LOWERCASE])
        password = generator.generate()

        self.assertRegex(password, r'[{}]+'.format("".join(rules.LOWER_ALPHA)))
        self.assertNotRegex(password, r'[{}]+'.format("".join(rules.UPPER_ALPHA)))
        self.assertNotRegex(password, r'[{}]+'.format(self.ESCAPED_SYMBOLS))
        self.assertNotRegex(password, r'[{}]+'.format("".join(rules.NUMBERS)))

    def test_generate_password_that_contain_uppercase_only_should_pass(self):
        generator = Generator(length=64,
                              rules=[rules.WITH_UPPERCASE])
        password = generator.generate()

        self.assertRegex(password, r'[{}]+'.format("".join(rules.UPPER_ALPHA)))
        self.assertNotRegex(password, r'[{}]+'.format("".join(rules.LOWER_ALPHA)))
        self.assertNotRegex(password, r'[{}]+'.format(self.ESCAPED_SYMBOLS))
        self.assertNotRegex(password, r'[{}]+'.format("".join(rules.NUMBERS)))

    def test_generate_password_that_contain_numbers_only_should_pass(self):
        generator = Generator(length=64,
                              rules=[rules.WITH_NUMBERS])
        password = generator.generate()

        self.assertRegex(password, r'[{}]+'.format("".join(rules.NUMBERS)))
        self.assertNotRegex(password, r'[{}]+'.format("".join(rules.LOWER_ALPHA)))
        self.assertNotRegex(password, r'[{}]+'.format(self.ESCAPED_SYMBOLS))
        self.assertNotRegex(password, r'[{}]+'.format("".join(rules.UPPER_ALPHA)))

    def test_generate_password_that_contain_symbols_only_should_pass(self):
        generator = Generator(length=64,
                              rules=[rules.WITH_SYMBOLS])
        password = generator.generate()

        self.assertRegex(password, r'[{}]+'.format(self.ESCAPED_SYMBOLS))
        self.assertNotRegex(password, r'[{}]+'.format("".join(rules.LOWER_ALPHA)))
        self.assertNotRegex(password, r'[{}]+'.format("".join(rules.UPPER_ALPHA)))
        self.assertNotRegex(password, r'[{}]+'.format("".join(rules.NUMBERS)))

    def test_generate_password_that_contain_only_lower_and_upper_chars_should_pass(self):
        generator = Generator(length=64,
                              rules=[rules.WITH_LOWERCASE,
                                     rules.WITH_UPPERCASE])
        password = generator.generate()

        charset = []
        charset.extend(rules.UPPER_ALPHA)
        charset.extend(rules.LOWER_ALPHA)

        self.assertRegex(password, r'[{}]+'.format("".join(charset)))
        self.assertNotRegex(password, r'[{}]+'.format("".join(self.ESCAPED_SYMBOLS)))
        self.assertNotRegex(password, r'[{}]+'.format("".join(rules.NUMBERS)))

    def test_generate_password_that_contain_only_lower_and_number_chars_should_pass(self):
        generator = Generator(length=64,
                              rules=[rules.WITH_LOWERCASE,
                                     rules.WITH_NUMBERS])
        password = generator.generate()

        charset = []
        charset.extend(rules.NUMBERS)
        charset.extend(rules.LOWER_ALPHA)

        self.assertRegex(password, r'[{}]+'.format("".join(charset)))
        self.assertNotRegex(password, r'[{}]+'.format("".join(self.ESCAPED_SYMBOLS)))
        self.assertNotRegex(password, r'[{}]+'.format("".join(rules.UPPER_ALPHA)))

    def test_generate_password_that_contain_only_lower_and_symbols_chars_should_pass(self):
        generator = Generator(length=64,
                              rules=[rules.WITH_LOWERCASE,
                                     rules.WITH_SYMBOLS])
        password = generator.generate()

        charset = []
        charset.extend(self.ESCAPED_SYMBOLS)
        charset.extend(rules.LOWER_ALPHA)

        self.assertRegex(password, r'[{}]+'.format("".join(charset)))
        self.assertNotRegex(password, r'[{}]+'.format("".join(rules.UPPER_ALPHA)))
        self.assertNotRegex(password, r'[{}]+'.format("".join(rules.NUMBERS)))

    def test_generate_password_that_contain_only_upper_and_numbers_chars_should_pass(self):
        generator = Generator(length=64,
                              rules=[rules.WITH_NUMBERS,
                                     rules.WITH_UPPERCASE])
        password = generator.generate()

        charset = []
        charset.extend(rules.UPPER_ALPHA)
        charset.extend(rules.NUMBERS)

        self.assertRegex(password, r'[{}]+'.format("".join(charset)))
        self.assertNotRegex(password, r'[{}]+'.format("".join(self.ESCAPED_SYMBOLS)))
        self.assertNotRegex(password, r'[{}]+'.format("".join(rules.LOWER_ALPHA)))

    def test_generate_password_that_contain_only_upper_and_symbols_chars_should_pass(self):
        generator = Generator(length=64,
                              rules=[rules.WITH_SYMBOLS,
                                     rules.WITH_UPPERCASE])
        password = generator.generate()

        charset = []
        charset.extend(self.ESCAPED_SYMBOLS)
        charset.extend(rules.UPPER_ALPHA)

        self.assertRegex(password, r'[{}]+'.format("".join(charset)))
        self.assertNotRegex(password, r'[{}]+'.format("".join(rules.LOWER_ALPHA)))
        self.assertNotRegex(password, r'[{}]+'.format("".join(rules.NUMBERS)))

    def test_generate_password_that_contain_only_numbers_and_symbols_chars_should_pass(self):
        generator = Generator(length=64,
                              rules=[rules.WITH_NUMBERS,
                                     rules.WITH_SYMBOLS])
        password = generator.generate()

        charset = []
        charset.extend(self.ESCAPED_SYMBOLS)
        charset.extend(rules.NUMBERS)

        self.assertRegex(password, r'[{}]+'.format("".join(charset)))
        self.assertNotRegex(password, r'[{}]+'.format("".join(rules.LOWER_ALPHA)))
        self.assertNotRegex(password, r'[{}]+'.format("".join(rules.UPPER_ALPHA)))

    def test_generate_password_that_contain_all_rules_and_without_ambiguous_should_pass(self):
        generator = Generator(length=64,
                              rules=[rules.WITH_LOWERCASE,
                                     rules.WITH_UPPERCASE,
                                     rules.WITH_NUMBERS,
                                     rules.WITH_SYMBOLS],
                              restrictions=[
                                  rules.WITHOUT_AMBIGUOUS
                              ])
        password = generator.generate()

        charset = []
        charset.extend(self.ESCAPED_SYMBOLS)
        charset.extend(rules.LOWER_ALPHA)
        charset.extend(rules.UPPER_ALPHA)
        charset.extend(rules.NUMBERS)

        self.assertRegex(password, r'[{}]+'.format("".join(charset)))
        self.assertNotRegex(password, r'[{}]+'.format("".join(rules.AMBIGUOUS)))

    def test_generate_password_that_contain_all_rules_and_without_medium_similar_should_pass(self):
        generator = Generator(length=64,
                              rules=[rules.WITH_LOWERCASE,
                                     rules.WITH_UPPERCASE,
                                     rules.WITH_NUMBERS,
                                     rules.WITH_SYMBOLS],
                              restrictions=[
                                  rules.WITHOUT_MEDIUM_SIMILAR
                              ])
        password = generator.generate()

        charset = []
        charset.extend(self.ESCAPED_SYMBOLS)
        charset.extend(rules.LOWER_ALPHA)
        charset.extend(rules.UPPER_ALPHA)
        charset.extend(rules.NUMBERS)

        self.assertRegex(password, r'[{}]+'.format("".join(charset)))
        self.assertNotRegex(password, r'[{}]+'.format("".join(rules.MEDIUM_SIMILAR)))

    def test_generate_password_that_contain_all_rules_and_without_very_similar_should_pass(self):
        generator = Generator(length=64,
                              rules=[rules.WITH_LOWERCASE,
                                     rules.WITH_UPPERCASE,
                                     rules.WITH_NUMBERS,
                                     rules.WITH_SYMBOLS],
                              restrictions=[
                                  rules.WITHOUT_VERY_SIMILAR
                              ])
        password = generator.generate()

        charset = []
        charset.extend(self.ESCAPED_SYMBOLS)
        charset.extend(rules.LOWER_ALPHA)
        charset.extend(rules.UPPER_ALPHA)
        charset.extend(rules.NUMBERS)

        self.assertRegex(password, r'[{}]+'.format("".join(charset)))
        self.assertNotRegex(password, r'[{}]+'.format("".join(rules.VERY_SIMILAR)))

    def test_generate_password_that_contain_all_rules_and_all_restrictions_should_pass(self):
        generator = Generator(length=64,
                              rules=[rules.WITH_LOWERCASE,
                                     rules.WITH_UPPERCASE,
                                     rules.WITH_NUMBERS,
                                     rules.WITH_SYMBOLS],
                              restrictions=[
                                  rules.WITHOUT_AMBIGUOUS,
                                  rules.WITHOUT_MEDIUM_SIMILAR,
                                  rules.WITHOUT_VERY_SIMILAR
                              ])
        password = generator.generate()

        charset = []
        charset.extend(self.ESCAPED_SYMBOLS)
        charset.extend(rules.LOWER_ALPHA)
        charset.extend(rules.UPPER_ALPHA)
        charset.extend(rules.NUMBERS)

        limitations = []
        limitations.extend(rules.AMBIGUOUS)
        limitations.extend(rules.MEDIUM_SIMILAR)
        limitations.extend(rules.VERY_SIMILAR)

        self.assertRegex(password, r'[{}]+'.format("".join(charset)))
        self.assertNotRegex(password, r'[{}]+'.format("".join(limitations)))
