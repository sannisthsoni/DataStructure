#Problem Description

#Given an array nums, write a function to move all 0's to the end of it while maintaining 
#the relative order of the non-zero elements.

#Solution v1.0
def moveZeros(nums):
    length = len(nums)
    for i in range(length):
        if nums[i] == 0:
            nums = nums[:i] + nums[i+1:] + [0]
    print( nums)

print(moveZeros([0,1,0,3,12]))

        