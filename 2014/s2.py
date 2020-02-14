def solve():
    if len(row1) != n or len(row2) != n:
        return "bad"
    
    book = dict()
    
    for i in range(n):
        student1 = row1[i]
        student2 = row2[i]
        
        if student1 == student2:
            return "bad"
          
        if book.get(student1) != None:
            return "bad"
            
        book[student1] = student2
        
    for i in range(n):
        student1 = row1[i]
        student2 = row2[i]

        if book.get(student2) != student1:
            return "bad"
            
    return "good"


n = int(input())

row1 = [str(s) for s in input().split(' ')]
row2 = [str(s) for s in input().split(' ')]

sol = solve()
print(sol)