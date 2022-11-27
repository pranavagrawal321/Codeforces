n = int(input())
c = 0
while n > 4:
    c += n // 5
    n = n%5
while n > 3:
    c += n // 4
    n = n%4
while n > 2:
    c += n // 3
    n = n%3
while n > 1:
    c += n // 2
    n = n%2
c += n
print(c)
