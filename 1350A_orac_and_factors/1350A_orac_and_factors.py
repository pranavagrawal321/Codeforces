for _ in range(int(input())):
    a, b = map(int, input().split())

    if a % 2 == 0:
        print(a + 2*b)
    else:
        for i in range(3, a+1):
            if a % i == 0:
                a += i
                break
        print(a + 2*(b-1))