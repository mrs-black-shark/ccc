def solve():
    if len(scores) == 0:
        return []
        
    max_score_1 = -1
    max_score_2 = -2
    
    for score in scores:
        if score >= max_score_1:
            max_score_2 = max_score_1
            max_score_1 = score
        elif score >= max_score_2:
            max_score_2 = score

    computers_tier_1 = computers.get(max_score_1)
    computers_tier_2 = computers.get(max_score_2)
    
    if computers_tier_1 != None:
        computers_tier_1.sort()
    if computers_tier_2 != None:
        computers_tier_2.sort()
    
    if len(computers_tier_1) == 2:
        return computers_tier_1
    if len(computers_tier_1) == 1 and computers_tier_2 == None:
        return computers_tier_1
            
    computer_1 = computers_tier_1[0]
    computer_2 = computers_tier_2[0]
    
    return [computer_1, computer_2]
    

n = int(input())

scores = dict()
computers = dict()

for _ in range(n):
    [name, r, s, d] = [str(s) for s in input().split(' ')]
    
    score = 2 * int(r) + 3 * int(s) + int(d)
    if scores.get(score) == None:
        scores[score] = True

    if computers.get(score) == None:
        computers[score] = [name]
    else:
        computers[score].append(name)
        
sol = solve()
for computer in sol:
    print(computer)