def solve():
    guests = []
    
    for i in range(n):
        guests.append(i + 1)
        
    for factor in factors:
        base = len(guests) // factor
        guest = factor * base
        
        while base > 0:
            guests.pop(guest - 1)
            
            base = base - 1
            guest = factor * base
            
    return guests
    

n = int(input())
m = int(input())

factors = []

for _ in range(m):
    factor = int(input())
    
    factors.append(factor)
    
    
sol = solve()
for invitee in sol:
    print(invitee)