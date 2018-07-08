#We have two special characters. The first character can be represented by one bit 0. 
#The second character can be represented by two bits (10 or 11).
#Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.


#SOlution from solutions/leetcode
def isOneBitCharacter(bits):
    i = 0

    while i< len(bits):
        i += bits[i] + 1
    return i == len(bits)-1

print(isOneBitCharacter( [1,0,0]))