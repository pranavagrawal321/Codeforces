a, b = map(int, input().split())
l = list(map(int, input().split()))
print(len(list(filter(lambda x: x > b, l))))
