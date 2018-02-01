from password.tools import StrengthMeter

StrengthMeter().print_stats()
print('-' * 80)
StrengthMeter("aaaaaaaa").print_stats()
print('-' * 80)
StrengthMeter("abcdefgh").print_stats()
print('-' * 80)
StrengthMeter("12345678").print_stats()
print('-' * 80)
StrengthMeter("HaX0r666").print_stats()
print('-' * 80)
StrengthMeter("ja-Skapem3!").print_stats()
print('-' * 80)
StrengthMeter("4%DHTMxYyyOc@F3p").print_stats()
print('-' * 80)
StrengthMeter("@d8l*7kUH5VtIt@V41v5NairgnOA#kKN").print_stats()
print('-' * 80)
StrengthMeter("@d8l*7kUH5VtIt@V41v5NairbceFGgnOA#KN").print_stats()


