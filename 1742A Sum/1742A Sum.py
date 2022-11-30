for i in range(int(input())):
    a, b, c = map(int, input().split())
    print(["NO", "YES"][a+b == c or b+c == a or a+c == b])
