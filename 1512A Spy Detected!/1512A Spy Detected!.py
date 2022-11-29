import collections

for i in range(int(input())):
    int(input())
    l = list(map(int, input().split()))
    c = collections.Counter(l)
    for i in c:
        if c[i] == 1:
            print(l.index(i)+1)
