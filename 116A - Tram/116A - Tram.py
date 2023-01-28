current = 0
max_capacity = 0
for i in range(int(input())):
    a, b = map(int, input().split())
    current -= a
    current += b
    max_capacity = max(max_capacity, current)
print(max_capacity)