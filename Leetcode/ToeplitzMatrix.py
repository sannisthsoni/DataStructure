#Problem Description:
#A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.
#Now given an M x N matrix, return True if and only if the matrix is Toeplitz.

#Solution v1.0
def ToeplitzMatrix(matrix):
    isToeplitz = True
    cols = len(matrix)
    rows = len(matrix[0])
    for i in range(cols-1):
        for j in range(rows-1):
            if matrix[i][j] != matrix[i+1][j+1]:
                isToeplitz = False
    return isToeplitz
print(ToeplitzMatrix([[1,2],[2,2]]))

