import sys


def smaller_or_equal(s1, s2):
    if s2 == None:
        return True
        
    if (s1 == 'S') or (s1 == 'M' and s2 != 'S') or (s1 == 'L' and s2 == 'L'):
        return True
        
    return False

def solve():
    counter = 0       
    
    for i in range(n_jerseys):
        number = i + 1
        size = jerseys[i]
        
        min_athlete_size = athlete_info.get(number)
        
        if smaller_or_equal(min_athlete_size, size):
            counter = counter + 1
            
    return counter


n_jerseys = int(input())
n_athletes = int(input())

jerseys = []
athlete_info = dict()

counter = -1
for line in sys.stdin.read().splitlines():
    counter = counter + 1

    if counter < n_jerseys:
        jersey = str(line)
        jerseys.append(jersey)
    elif counter < n_jerseys + n_athletes:
        info = [str(s) for s in line.split(' ')]
        
        size = info[0]
        number = int(info[1])
        
        if smaller_or_equal(size, athlete_info.get(number)):    
            athlete_info[number] = size
    else:
        break
    
    
sol = solve()
print(sol)