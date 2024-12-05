def is_valid(matrix, x, y):
    return 0 <= x < len(matrix) and 0 <= y < len(matrix[0])

def check_word(matrix, x, y, dx, dy, word):
    for k in range(len(word)):
        nx, ny = x + k * dx, y + k * dy
        if not is_valid(matrix, nx, ny) or matrix[nx][ny] != word[k]:
            return False
    return True

file1 = open('input', 'r')

matrix = []

for line in file1.readlines():
    array = list(line.strip())
    matrix.append(array)

word = "XMAS"
directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
count = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 'X':
            for dx, dy in directions:
                if check_word(matrix, i, j, dx, dy, word):
                    count += 1

print(count)