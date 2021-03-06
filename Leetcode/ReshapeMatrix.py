#Problem Description:

#In MATLAB, there is a very useful function called 'reshape', 
# which can reshape a matrix into a new one with different size but keep its original data.

#You're given a matrix represented by a two-dimensional array, 
#and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

#The reshaped matrix need to be filled with all the elements 
#of the original matrix in the same row-traversing order as they were.

#If the 'reshape' operation with given parameters is possible and legal, 
# output the new reshaped matrix; Otherwise, output the original matrix. 

#Solution v1.1 (From Leetcode comment by 'liaowy') https://leetcode.com/articles/reshape-the-matrix/#
def matrixReshape(self, nums, r, c):
    matrix=[]
    one_row=[]
    for i in nums:
        for j in i:
            one_row.append(j)
    if r*c == len(one_row):
        for i in range(0,len(one_row),c):
            matrix.append(one_row[i:i+c])
        return matrix
    else:
        return nums

#Solution v1.0
# def MatrixToList(matrix):
#     l = []
#     for row in matrix:
#         for element in row:
#             l.append(element)
#     return l

# def ListToMatrix(l,r,c):
#     length = len(l)
#     matrix = []
#     temp=[]
#     for i in range(length):
#         temp.append(l[i])
#         if (i+1)%c == 0:
#             matrix.append(temp)
#             temp = []
#     return matrix
# #print(MatrixToList([[1,2],[3,4]]))
# print(ListToMatrix([1,2,3,4,5,6,7,8,9,10],5,2))


#Lessons:
#Exploit the use of range(0,limit,step_size) & slicing of array in
#if r*c == len(one_row):
#            for i in range(0,len(one_row),c):
#                matrix.append(one_row[i:i+c])