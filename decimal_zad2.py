import decimal

decimal.getcontext().prec = 2

a = decimal.Decimal('1.2345')
b = decimal.Decimal('2.3456')
c = a + b
print(c)
