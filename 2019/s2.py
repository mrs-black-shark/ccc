import math


def is_prime(n):
	if n == 1:
		return False

	if n == 2:
		return True

	for i in range(2, math.floor(math.sqrt(n)) + 1):
		if n % i == 0:
			return False

	return True

def solve(n):
	if is_prime(n):
		return "{} {}".format(n, n)

	for i in range(1, n):
		lower_half = i
		upper_half = 2 * n - i

		if is_prime(lower_half) and is_prime(upper_half):
			return "{} {}".format(lower_half, upper_half)

	return None


n = int(input())

for _ in range(n):
	average = int(input())

	sol = solve(average)
	print(sol)