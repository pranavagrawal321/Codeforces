import string

int(input())
s = input()
s = s.upper()
print(["NO", "YES"][set(s) == set(string.ascii_uppercase)])
