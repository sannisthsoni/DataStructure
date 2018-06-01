#Problem Description:

#In a string S of lowercase letters, these letters form consecutive groups of the same character.
#For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".
#Call a group large if it has 3 or more characters.  
#We would like the starting and ending positions of every large group.
#The final answer should be in lexicographic order.

def LargeGroupPositions(S):
    start=0
    end=0
    op=[]
    length = len(S)
    for i in range(1,length):
        if S[i] != S[i-1]:
            if end-start>2:
                op.append([start,end])
            start,end=i,i
        else:
            end=i
            if i==length-1:
                op.append([start,end])
    return op
        

print(LargeGroupPositions("aaa"))


