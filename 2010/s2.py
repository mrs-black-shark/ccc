def solve():
    p = 0
    res = ""
    while p < len(codes):
        code = ""
        counter = 0
        
        while encodings.get(code) == None:
            bit = codes[p + counter]
            code = code + bit
            
            counter = counter + 1
            
        char = encodings.get(code)
        
        res = res + char
        p = p + counter
        
    return res
    

n = int(input())

encodings = dict()
for _ in range(n):
    [val, key] = [str(s) for s in input().split(' ')]
    
    encodings[key] = val
    
codes = str(input())

sol = solve()
print(sol)