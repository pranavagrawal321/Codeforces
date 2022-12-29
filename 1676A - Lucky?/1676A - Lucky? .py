for i in range(int(input())):
    n = input()
    a, b = 0, 0
    for j in range(3):
        # print(int(n[j]))
        a += int(n[j])
    for j in range(3, 6):
        # print(int(n[j]))
        b += int(n[j])
    print(["NO", "YES"][a == b])
