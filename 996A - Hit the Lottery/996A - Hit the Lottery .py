n = int(input())
c = 0
while n > 0:
    c += n//100
    n = n%100
    c += n//20
    n = n%20
    c += n//10
    n = n%10
    c += n//5
    n = n%5
    c += n
    n = 0
print(c)
