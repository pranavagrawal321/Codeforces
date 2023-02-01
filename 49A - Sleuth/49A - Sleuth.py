s = input()
print(["NO", "YES"][s[:-1].split()[-1][-1].upper() in "AEIOUY"])