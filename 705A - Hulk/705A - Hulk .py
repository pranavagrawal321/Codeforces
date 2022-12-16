l = ["I hate", "I love"]
n = int(input())
s = ""
for i in range(n):
    if i % 2 == 0:
        s += l[0] + " that "
    else:
        s += l[1] + " that "
print(s[:-5] + "it")
