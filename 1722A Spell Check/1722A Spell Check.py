for i in range(int(input())):
    int(input())
    s = input()
    a = s.split("T")
    print(["NO", "YES"][len(s) == 5 and len(a) == 2 and set(s.replace("T", "")) == set("mriu")])
