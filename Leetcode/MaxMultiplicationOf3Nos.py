#Problem Description

#Given an integer array, find three numbers whose product is maximum and output the maximum product.

#Solution v1.0
def MaximumProduct(nums):
    nums.sort()
    return max([nums[0]*nums[1]*nums[-1],nums[-1]*nums[-2]*nums[-3]])


print(MaximumProduct([4,2,3,1]))