m = []
for i in range(3):
    l = list(map(int, input().split()))
    l.sort(reverse=True)
    m.append(l[1])

print(sorted(m)[1])