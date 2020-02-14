def solve():
    data = []
    for i in range(n):
        reading = readings[i]
        
        if reading == 0:
            data.pop()
        if reading > 0:
            data.append(reading)
      
    total = 0

    for d in data:
        total = total + d

    return total
    

n = int(input())

readings = []

for _ in range(n):
    readings.append(int(input()))
    
sol = solve()
print(sol)