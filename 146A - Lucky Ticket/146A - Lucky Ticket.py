int(input())
n = input()
print(["NO", "YES"][sum(map(lambda x: int(x), n[:len(n) // 2])) == sum(map(lambda x: int(x), n[len(n) // 2:])) and (
            set(n) == {"4", "7"} or set(n) == {"4"} or set(n) == {"7"})])
