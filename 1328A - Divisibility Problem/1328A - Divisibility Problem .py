for i in range(int(input())):
    a, b = map(int, input().split())
    print(b - (a % b) if a % b else 0)
