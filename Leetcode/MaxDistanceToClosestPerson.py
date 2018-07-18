#In a row of seats, 1 represents a person sitting in that seat, 
# and 0 represents that the seat is empty. 

#There is at least one empty seat, and at least one person sitting.

#Return that maximum distance to closest person.

def solution(seats):
    global_counter = 0
    local_counter = 0

    for i in seats:
        if i == 0:
            local_counter += 1
        if i == 1:
            if local_counter > global_counter :
                global_counter = local_counter
            local_counter = 0

    return global_counter
            

    

print(solution([1,0,0,0,1,0,1]))