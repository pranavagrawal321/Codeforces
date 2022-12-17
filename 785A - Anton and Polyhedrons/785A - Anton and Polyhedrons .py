d = {"Tetrahedron": 4, "Cube": 6, "Octahedron": 8, "Dodecahedron": 12, "Icosahedron": 20}
c = 0
for i in range(int(input())):
    c += d[input()]
print(c)
