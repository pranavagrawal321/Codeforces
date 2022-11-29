  for i in range(int(input())):
      int(input())
      l = list(map(int, input().split()))
      r = l[0]
      for j in l[1:-1]:
          r = r^j
      print(r)
