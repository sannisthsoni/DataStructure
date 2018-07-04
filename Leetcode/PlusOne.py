#Problem Description

#Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

#The digits are stored such that the most significant digit is at the head of the list, 
#and each element in the array contain a single digit.

#You may assume the integer does not contain any leading zero, except the number 0 itself.

def plusOne(digits):
    num = 0
    length = len(digits)
    ten = 1
    for i in range(length-1,-1,-1):
        num = digits[i]*ten + num
        ten *= 10
    num = num + 1
    
    temp = [0]*(length+1)
    ten = 1
    for i in range(length-1,-1,-1):
        print(num%10)
        temp[i] = num%10
        num = int(num/10)
    return temp
    
            

print(plusOne([9]))