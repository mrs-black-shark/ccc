def solve():
	data.sort()

	slicing_point = n // 2 if n % 2 == 0 else n // 2 + 1

	low_tides = data[:slicing_point]
	high_tides = data[slicing_point:]

	res = []
	for i in range(n // 2):
		low_tide = low_tides[len(low_tides) - 1 - i]
		high_tide = high_tides[i]

		res.append(str(low_tide))
		res.append(str(high_tide))

	if n % 2 == 1:
		res.append(str(low_tides[0]))

	return ' '.join(res)


n = int(input())
data = [int(s) for s in input().split(' ')]

sol = solve()
print(sol)