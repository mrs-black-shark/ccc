############################ notice #################################
################ this solution only passes 5/6 cases ################
### cannot process all inputs without getting an error for case 6 ###
### either getting RTE | unknown signal 0 or RTE | window changed ###
#####################################################################


import sys


def solve():
    queue_tall = []
    queue_short = []
    
    visited_tall = [False] * n
    visited_short = [False] * n
    visited_tall[p - 1] = True
    visited_short[p - 1] = True
    
    for i in range(n):
        if comparisons[p - 1][i] == True:
            queue_tall.append(i)
        if comparisons[p - 1][i] == False:
            queue_short.append(i)
            
    while len(queue_tall) > 0:
        student = queue_tall.pop(0)
        visited_tall[student] = True
        
        for i in range(n):
            if comparisons[student][i] == True:
                comparisons[p - 1][i] = True
                
                if visited_tall[i] == False:
                    queue_tall.append(i)
                    
    while len(queue_short) > 0:
        student = queue_short.pop(0)
        visited_short[student] = True
        
        for i in range(n):
            if comparisons[student][i] == False:
                comparisons[p - 1][i] = False
                
                if visited_short[i] == False:
                    queue_short.append(i)
            
    
    if comparisons[p - 1][q - 1] == True:
        return "yes"
    elif comparisons[p - 1][q - 1] == False:
        return "no"
    elif comparisons[p - 1][q - 1] == None:
        return "unknown"


[n, m] = [int(s) for s in input().split(' ')]
[p, q] = [-1, -1]

comparisons = []
    
for _ in range(n):
    comparisons.append([None] * n)
  
counter = -1
for line in sys.stdin.read().splitlines():
    counter = counter + 1

    if counter < m:
        [student_tall, student_short] = [int(s) for s in line.split(' ')]
        
        comparisons[student_tall - 1][student_short - 1] = True
        comparisons[student_short - 1][student_tall - 1] = False
    elif counter == m:
        [p, q] = [int(s) for s in line.split(' ')]
    else:
        break


sol = solve()
print(sol)