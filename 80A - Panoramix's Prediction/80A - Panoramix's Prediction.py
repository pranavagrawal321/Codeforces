l = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
a, b = map(int, input().split())
print(["NO", "YES"][a in l and b == l[l.index(a) + 1]])