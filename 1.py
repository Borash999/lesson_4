# Напишите функцию для транспонирования матрицы

Matrix = [[2,8,5], [3,9,4], [4,10,7],[4,1,2]]
def trans(Matrix):
    transpose = [[0 for j in range (len(Matrix))] for i in range (len(Matrix[0]))]
    for i in range (len(Matrix)):
        for j in range(len(Matrix[0])):
            transpose[j][i] = Matrix[i][j]
    return transpose
print(Matrix)
print(trans(Matrix))