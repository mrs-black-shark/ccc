def solve():
	villages.sort()

	boundaries = []

	for i in range(n - 1):
		village_left = villages[i]
		village_right = villages[i + 1]

		boundary = (village_left + village_right) / 2
		boundaries.append(boundary)

	min_neighborhood = float("inf")

	for i in range(n - 2):
		neighborhood = boundaries[i + 1] - boundaries[i]

		if neighborhood < min_neighborhood:
			min_neighborhood = neighborhood

	return


n = int(input())

villages = []

for _ in range(n):
	position = int(input())

	villages.append(position)

sol = solve()
print(sol)