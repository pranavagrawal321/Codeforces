from math import sqrt

n = int(input())
ans = [(-1 + sqrt(1 + 8 * n)) / 2, (-1 - sqrt(1 + 8 * n)) / 2]
print(["NO", "YES"][max(ans) == int(max(ans))])
