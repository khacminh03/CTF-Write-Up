r, c = input().split()
matrix = []
test = 0
for i in range (0, int(r)):
    temp = input().split()
    matrix.append(temp)
for i in range(0, int(r)):
    for j in range(0, int(c)):
        try:            
            if (matrix[i][j] == '.' and matrix[i][j + 1] == '.' and matrix[i][j + 2] == '.'):
                print(i + 1, j + 1)
                exit()
        except IndexError:
            test = test + 1