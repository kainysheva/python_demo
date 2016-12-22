import random

def mult(matrix1, matrix2):
    sum = 0
    temp_matrix = []
    res_matrix = []
    if len(matrix1)!=len(matrix2):
        print("Error")
    else:
        row1 = len(matrix1)
        col1 = len(matrix1[0])
        row2 = col1
        col2 = len(matrix2[0])
        for z in range(0, row1):
            for j in range(0,col2):
                for i in range(0,col1):
                    sum = sum + matrix1[z][i]*matrix2[i][j]
                temp_matrix.append(sum)
                sum=0
            res_matrix.append(temp_matrix)
            temp_matrix = []
    return res_matrix

def create(row, col):
    temp_matrix = []
    matrix = []
    for i in range(0,row):
        for j in range(0, col):
            temp_matrix.append(random.randint(1,9))
        matrix.append(temp_matrix)
        temp_matrix=[]
    return matrix

print('Matrx 1: ')
col1=int(input('n = '))
row1=int(input('m = '))
matrix1 = create(row1,col1)
print(matrix1)

print('Matrx 2: ')
col2=int(input('n = '))
row2=int(input('m = '))
matrix2 = create(row2,col2)
print(matrix2)

print('Multiplication: ')
res_matrix = mult(matrix1, matrix2)
print(res_matrix)

def sum(matrix1, matrix2):
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    return result

print('Sum: ')
res = sum(matrix1, matrix2)
print(res)