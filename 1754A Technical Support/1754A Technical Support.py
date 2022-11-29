for i in range(int(input())):
    int(input())
    s = input()
    stack = []
    for i in s:
        if i == "Q":
            stack.append(i)
        elif i == "A":
            if len(stack) > 0:
                stack.pop()
    print(["NO", "YES"][len(stack) == 0])
