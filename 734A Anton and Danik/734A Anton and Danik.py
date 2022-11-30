import collections

int(input())
c = collections.Counter(input())
if c["A"] > c["D"]:
    print("Anton")
elif c["A"] < c["D"]:
    print("Danik")
else:
    print("Friendship")
