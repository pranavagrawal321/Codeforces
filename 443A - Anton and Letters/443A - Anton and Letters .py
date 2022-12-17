s = input()
if len(s) == 2:
    print(0)
else:
    s = s[1:-1].split(',')
    s = list(map(lambda x: x.strip(), s))
    print(len(set(s)))
