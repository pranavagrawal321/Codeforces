a, b = map(int, input().split())
l = list(map(int, input().split()))
c = 0
i, j = 0, 0
while i < len(l):
    if abs(l[i] - l[j]) <= b:
        if i != j:
            c += 1
            # print(l[i], l[j])
    j += 1
    if j == len(l):
        i += 1
        j = 0
print(c)