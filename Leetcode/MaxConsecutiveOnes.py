#Problem Description
#Given a binary array, find the maximum number of consecutive 1s in this array.

#Solution v1.0

def MaxConsecutiveOnes(nums):
    sum = 0
    temp=0
    length = len(nums)
    i = 0
    for i in range(length):
        if nums[i] == 1:
            temp +=1
        if nums[i] == 0 or length==(i+1):
            if temp > sum:
                sum=temp
            temp=0

    return sum

print(MaxConsecutiveOnes([1,1,0,1,1,1]))
