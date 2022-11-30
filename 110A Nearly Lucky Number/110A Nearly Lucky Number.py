import collections

n = int(input())
c = collections.Counter(str(n))
print(["NO", "YES"][c["4"] + c["7"] == 4 or c["4"] + c["7"] == 7])
