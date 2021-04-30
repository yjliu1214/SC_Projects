"""
File: largest_digit.py
Name: Serena Liu
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: int, an integer
	:return: int, the biggest digit in the integer.
	"""
	if 0 <= n <= 9:
		return n
	else:
		if n < 0:
			n = -n
		if n % 10 > (n % 100 - n % 10) // 10:
			n = (n - n % 100 + n % 10 * 10) // 10
			return find_largest_digit(n)
		else:
			n = n//10
			return find_largest_digit(n)


if __name__ == '__main__':
	main()
