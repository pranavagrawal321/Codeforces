s = input()
s = s.lower()
s = list(s)
i = 0
while i < len(s):
    if s[i] in "aoyeui":
        s.pop(i)
    else:
        s[i] = "." + s[i]
        i += 1
s = "".join(s)
print(s)
