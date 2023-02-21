for _ in range(int(input())):
    int(input())
    s = input()
    start = [0, 0]
    for i in s:
        if i == "L":
            start[0] -= 1
        elif i == "R":
            start[0] += 1
        elif i == "U":
            start[1] += 1
        elif i == "D":
            start[1] -= 1
        if start == [1, 1]:
            print("YES")
            break
    else:
        print("NO")