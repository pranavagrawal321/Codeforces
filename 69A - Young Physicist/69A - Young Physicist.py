s1, s2, s3 = 0, 0, 0
for i in range(int(input())):
    a, b, c = map(int, input().split())
    s1 += a
    s2 += b
    s3 += c

if s1 == 0 and s2 == 0 and s3 == 0:
    print("YES")
else:
    print("NO")