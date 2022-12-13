n = int(input())
c = 1
prev = int(input())
for i in range(n-1):
    curr = int(input())
    if curr != prev:
        c += 1
        prev = curr
print(c)
