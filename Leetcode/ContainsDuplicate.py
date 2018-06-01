#Problem Description:

#Given an array of integers, find if the array contains any duplicates.

#Your function should return true if any value appears at least twice in the array, 
#and it should return false if every element is distinct.

#Solution v1.0
def ContainsDuplicate(nums):
    dict={}

    for num in nums:
        if num in dict:
            dict[num] = dict[num] + 1
        else:
            dict[num] = 1
    if list(dict.values()) == [1]*len(dict):
        
        return False
    else:
        return True

print(ContainsDuplicate([1,2,3,1]))