matrix = []

for i in range(int(input())):
    matrix.append(list(map(int, input().split())))

s = 0

for i in range(len(matrix)):
    for j in range(len(matrix)):
        if i == j:
            s += matrix[i][j]
        elif i + j == len(matrix) - 1:
            s += matrix[i][j]
        elif i == len(matrix) // 2:
            s += matrix[i][j]
        elif j == len(matrix) // 2:
            s += matrix[i][j]

print(s)
