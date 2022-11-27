k, n, w = map(int, input().split())
s = 0
for i in range(1, w+1):
    s += k*i
print(s - n if s > n else 0)
