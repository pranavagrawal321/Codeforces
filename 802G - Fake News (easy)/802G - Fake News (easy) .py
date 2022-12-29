s = input()
ans = "heidi"
i, j = 0, 0
while i < len(s) and j < len(ans):
    if s[i] == ans[j]:
        j += 1
    i += 1
print(["NO", "YES"][j == len(ans)])
