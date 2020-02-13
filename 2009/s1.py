def solve():
	cool_numbers = [0]

	cool_seed = 1
	while cool_numbers[-1] < 10 ** 8 + 1:
		cool_number = cool_seed ** 6
		cool_numbers.append(cool_number)

		cool_seed = cool_seed + 1

	counter = 0

	for cool_number in cool_numbers:
		if lower_bound <= cool_number and cool_number <= upper_bound:
			counter = counter + 1

	return counter


lower_bound = int(input())
upper_bound = int(input())

sol = solve()
print(sol)