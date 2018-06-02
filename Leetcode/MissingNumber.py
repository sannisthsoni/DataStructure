#Problem Description

#Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, 
#find the one that is missing from the array.

#Solution v1.0
def MissingNumber(nums):
    length = len(nums)
    add=sum(nums)

    return int(((length)*(length+1))/2-add)

print(MissingNumber([9,6,4,2,3,5,7,0,1]))