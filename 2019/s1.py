def solve():
	counter_h = 0
	counter_v = 0

	for op in operations:
		if op == 'H':
			counter_h = counter_h + 1
		if op == 'V':
			counter_v = counter_v + 1

	if counter_h % 2 == 0 and counter_v % 2 == 0:
		return ["1 2", "3 4"]
	if counter_h % 2 == 0 and counter_v % 2 == 1:
		return ["2 1", "4 3"]
	if counter_h % 2 == 1 and counter_v % 2 == 0:
		return ["3 4", "1 2"]
	if counter_h % 2 == 1 and counter_v % 2 == 1:
		return ["4 3", "2 1"]


operations = [str(s) for s in input()]

sol = solve()
for row in sol:
	print(row)