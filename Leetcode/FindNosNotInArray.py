#Problem Description

#Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), 
# some elements appear twice and others appear once.

#Find all the elements of [1, n] inclusive that do not appear in this array.

#Could you do it without extra space and in O(n) runtime? 
#You may assume the returned list does not count as extra space.





#Solution v1.0
def FindDisappeared(nums):
    length = len(nums)
    temp=[]
    isPresent = [False]*(length)
    
    for num in nums:
        isPresent[num-1] = True

    for i in range(len(isPresent)):
        if not isPresent[i]:
            temp.append(i+1)

    return temp

print(FindDisappeared([4,3,2,7,8,2,3,1]))
