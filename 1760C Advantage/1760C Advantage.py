for _ in range(int(input())):
    int(input())
    l = list(map(int, input().split()))
    a = sorted(l, reverse=True)
    for i in l:
        if a[0] == i:
            print(i - a[1], end=' ')
        else:
            print(i - a[0], end=' ')
    print()
