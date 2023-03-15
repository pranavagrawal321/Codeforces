pi = "314159265358979323846264338327"

for _ in range(int(input())):
    s = input()
    c = 0
    for i in range(len(s)):
        if s[i] == pi[i]:
            c += 1
        else:
            break
    print(c)