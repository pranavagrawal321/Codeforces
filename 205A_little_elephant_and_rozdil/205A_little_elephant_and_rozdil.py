int(input())
l = list(map(int, input().split()))

print("Still Rozdil" if l.count(min(l)) > 1 else l.index(min(l))+1)