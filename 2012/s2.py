def convert_to_arabic(char):
	if char == 'M':
		return 1000
	if char == 'D':
		return 500
	if char == 'C':
		return 100
	if char == 'L':
		return 50
	if char == 'X':
		return 10
	if char == 'V':
		return 5
	if char == 'I':
		return 1

	return 0

def solve():
	res = 0

	for i in range(len(string) // 2):
		char_numeric = string[2 * i]
		char_romantic = string[2 * i + 1]

		base = convert_to_arabic(char_romantic)
		multiplier = int(char_numeric)

		if i != len(string) // 2 - 1:
			char_romantic_next = string[2 * i + 3]
			base_next = convert_to_arabic(char_romantic_next)

			if base_next > base:
				res = res - base * multiplier
			else:
				res = res + base * multiplier
		else:
			res = res + base * multiplier

	return res


string = str(input())

sol = solve()
print(sol)