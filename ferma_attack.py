import math
from decimal import Decimal
from progress.bar import IncrementalBar



with open('keys.txt', 'r') as keys:
    e = int(keys.readline().rstrip())
    n = int(keys.readline().rstrip())
sqrt_n = int(Decimal(str(n)).sqrt())
# print(sqrt_n)
bar = IncrementalBar('Countdown', max=n - sqrt_n)

for i in range(sqrt_n + 1, n):
    bar.next()
    B = i ** 2 - n
    if int(Decimal(str(B)).sqrt()) ** 2 == B:
        A = i
        break
B = int(B**0.5)
print(A, B)
p = A + B
q = A - B
print(p, q)
print('n', p * q)