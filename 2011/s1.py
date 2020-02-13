def solve():
	counter_s = 0
	counter_t = 0

	for sentence in sentences:
		for char in sentence:
			if char == 's' or char == 'S':
				counter_s = counter_s + 1
			if char == 't' or char == 'T':
				counter_t = counter_t + 1

	return 'English' if counter_t > counter_s else 'French'


n = int(input())

sentences = []
for _ in range(n):
	sentences.append(input())

sol = solve()
print(sol)