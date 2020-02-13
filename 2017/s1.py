def solve():
	sum_swifts = 0
	sum_semaphores = 0

	counter = 0

	for i in range(n):
		sum_swifts = sum_swifts + scores_swifts[i]
		sum_semaphores = sum_semaphores + scores_semaphores[i]

		if sum_swifts == sum_semaphores:
			counter = i + 1

	return counter


n = int(input())
scores_swifts = [int(s) for s in input().split(' ')]
scores_semaphores = [int(s) for s in input().split(' ')]

sol = solve()
print(sol)