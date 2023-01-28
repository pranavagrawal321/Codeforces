from math import gcd

a, b, n = map(int, input().split())

while n > 0:
    n -= gcd(a, n)
    if n == 0:
        print(0)
        break
    n -= gcd(b, n)
    if n == 0:
        print(1)
        break