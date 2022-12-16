n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(n*(n+1)//2 - sum(set(a[1:]+b[1:])) == 0 and 'I become the guy.' or 'Oh, my keyboard!')
