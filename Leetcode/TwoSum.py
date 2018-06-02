#Problem Description:

#Given an array of integers that is already sorted in ascending order, 
# find two numbers such that they add up to a specific target number.

#The function twoSum should return indices of the two numbers such that they add up to the target, 
#where index1 must be less than index2.

def TwoSum(nums,target):
    length = len(nums)
    index = 0
    for i in range(length):
        if nums[i]>target:
            index = i-1
    for i in range(index):
        for j in range(i+1,index):
            if nums[i] + nums[j] == target:
                return [i+1,j+1]

        
print(TwoSum([2,7,11,15],9))
