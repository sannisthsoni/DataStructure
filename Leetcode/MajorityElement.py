#Problem Description:

#Given an array of size n, find the majority element. 
# The majority element is the element that appears more than ⌊ n/2 ⌋ times.

#You may assume that the array is non-empty and the majority element always exist in the array.

#Solution v1.0
def FindMajority(nums):
    dict = {}

    for num in nums:
        if num not in dict:
            dict[num]=1
        else:
            dict[num] = dict[num] + 1
    print(dict)

    return max(dict,key=dict.get)

print(FindMajority([2,2,1,1,1,2,2]))