a, b = map(int, input().split())
l = []
for i in range(b):
    l.append(input())
print(l[a%b-1])