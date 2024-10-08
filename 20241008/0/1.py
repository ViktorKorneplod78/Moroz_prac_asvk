import fractions
import decimal

def multiplier(x, y, Type):
    return Type(x) * Type(y)

print(f"{multiplier("1.1", "2.2", float) = }")
print(f"{multiplier("1.1", "2.2", decimal.Decimal) = }")
print(f"{multiplier("1.1", "2.2", fractions.Fraction) = }")
