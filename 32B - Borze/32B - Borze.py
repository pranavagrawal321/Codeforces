s = input()
ans = ""
i = 0
while i < len(s):
    if s[i] == "-" and s[i + 1] == ".":
        ans += "1"
        i += 2
    elif s[i] == "-" and s[i + 1] == "-":
        ans += "2"
        i += 2
    elif s[i] == ".":
        ans += "0"
        i += 1

print(ans)