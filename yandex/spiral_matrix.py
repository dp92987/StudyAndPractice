"""
Print spiral matrix n**2.
"""

def spiral_matrix(n):
    matrix = []
    for i in range(0, n):
        row = []
        for j in range(0, n):
            row.append(None)
        matrix.append(row)

    r, c = 0, 0
    move = ''
    for i in range(1, n**2+1):
        if move == '':
            move = 'right'
        elif move == 'right':
            if c+1 >= n or matrix[r][c+1] is not None:
                move = 'down'
                r += 1
            else:
                c += 1
        elif move == 'down':
            if r+1 >= n or matrix[r+1][c] is not None:
                move = 'left'
                c -= 1
            else:
                r += 1
                matrix[r][c] = i
        elif move == 'left':
            if c-1 < 0 or matrix[r][c-1] is not None:
                move = 'up'
                r -= 1
            else:
                c -= 1
                matrix[r][c] = i
        elif move == 'up':
            if r-1 < 0 or matrix[r-1][c] is not None:
                move = 'right'
                c += 1
            else:
                r -= 1
        matrix[r][c] = i

    return matrix


num = int(input('num: '))
for row in spiral_matrix(num):
    print(*row)
