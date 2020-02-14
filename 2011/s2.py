def solve():
	return score


n = int(input())

responses = []

for _ in range(n):
	response = str(input())

	responses.append(response)

score = 0
for i in range(n):
	answer = str(input())

	if responses[i] == answer:
		score = score + 1


sol = solve()
print(sol)