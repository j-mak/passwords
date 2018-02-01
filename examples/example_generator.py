from password.generator import Generator
import password.rules as rules

generator = Generator(length=12,
                      rules=[
                          rules.WITH_LOWERCASE,
                          rules.WITH_SYMBOLS,
                          rules.WITH_NUMBERS,
                          rules.WITH_UPPERCASE
                      ],
                      restrictions=[
                          rules.WITHOUT_AMBIGUOUS,
                          rules.WITHOUT_MEDIUM_SIMILAR,
                          rules.WITHOUT_VERY_SIMILAR
                      ])

print(generator.generate())
