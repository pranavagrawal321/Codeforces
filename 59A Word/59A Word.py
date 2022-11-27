s = input()
u = list(filter(lambda x: x.isupper(), s))
l = list(filter(lambda x: x.islower(), s))
print(s.lower() if len(u) <= len(l) else s.upper())
