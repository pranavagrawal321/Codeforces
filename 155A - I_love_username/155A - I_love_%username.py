int(input())
l = list(map(int, input().split()))
mini, maxi, c = l[0], l[0], 0
for i in l:
    if i > maxi:
        maxi = i
        c += 1
    elif i < mini:
        mini = i
        c += 1
print(c)