# Given a binary matrix A, we want to flip the image horizontally, 
# then invert it, and return the resulting image.

# To flip an image horizontally means that each row of the image is reversed.  
# For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. 
# For example, inverting [0, 1, 1] results in [1, 0, 0].


def reverse(matrix):
    for matrix_col in matrix:
        length = len(matrix_col)
        #print(int((length/2)))
        for i in range(int(len(matrix_col)/2)):
            temp=matrix_col[i]
            matrix_col[i] = matrix_col[len(matrix_col)-i-1]
            matrix_col[len(matrix_col)-i-1] = temp
        
    return matrix

def inverse(matrix):
    for matrix_col in matrix:
        for i in range(len(matrix_col)):
            if matrix_col[i] == 1:
                matrix_col[i] = 0
            else:
                matrix_col[i] = 1
    return matrix

print(reverse([[1,1,0],[0,0,1]]))
print(inverse([[1,1,0],[0,0,1]]))


