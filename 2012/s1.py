def solve():
    if n < 4:
        return 0
        
    return round((n - 1) * (n - 2) * (n - 3) / 6)


n = int(input())

sol = solve()
print(sol)