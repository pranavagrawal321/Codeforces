s = input()
up, low, dig, char = False, False, False, False
for i in s:
    if i.isupper():
        up = True
    if i.islower():
        low = True
    if i.isdigit():
        dig = True
    if len(s) >= 10:
        length = True
    if i in {"!", "?", ".", ",", "_"}:
        char = True
if len(s) >= 5 and up and low and dig:
    print("Correct")
else:
    print("Too weak")
