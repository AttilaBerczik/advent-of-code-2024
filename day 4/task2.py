def is_valid(matrix, x, y):
    return 0 <= x < len(matrix) and 0 <= y < len(matrix[0])

def check_diagonals(matrix, x, y):
    diag1 = False
    if is_valid(matrix, x-1, y+1) and is_valid(matrix, x+1, y-1):
        if matrix[x-1][y+1] == 'M' and matrix[x+1][y-1] == 'S':
            diag1 = True
        elif matrix[x-1][y+1] == 'S' and matrix[x+1][y-1] == 'M':
            diag1 = True
    diag2 = False
    if is_valid(matrix, x-1, y-1) and is_valid(matrix, x+1, y+1):
        if matrix[x-1][y-1] == 'M' and matrix[x+1][y+1] == 'S':
            diag2 = True
        elif matrix[x-1][y-1] == 'S' and matrix[x+1][y+1] == 'M':
            diag2 = True
    return diag1 and diag2

file1 = open('input', 'r')

matrix = []

for line in file1.readlines():
    array = list(line.strip())
    matrix.append(array)

count = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 'A':
            if check_diagonals(matrix, i, j):
                count += 1

print(count)