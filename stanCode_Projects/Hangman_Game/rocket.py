"""
File: rocket.py
Name: Serena Liu
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant determines rocket size.

SIZE = 3


def main():
	"""
	This program draws a rocket.
	"""
	draw_head()
	draw_belt()
	draw_upper()
	draw_lower()
	draw_belt()
	draw_head()


def draw_head():
	for i in range(SIZE):
		for j in range(SIZE-i):
			print(' ', end="")
		for j in range(i+1):
			print('/', end="")
		for j in range(i+1):
			print('\\', end="")
		print("")


def draw_belt():
	print('+', end="")
	for i in range(SIZE*2):
		print('=', end="")
	print('+')


def draw_upper():
	for i in range(SIZE):
		print('|', end="")
		for j in range(SIZE-i-1):
			print('.', end="")
		for j in range(i+1):
			print('/', end="")
			print('\\', end="")
		for j in range(SIZE - i - 1):
			print('.', end="")
		print('|', end="")
		print("")


def draw_lower():
	for i in range(SIZE):
		print('|', end="")
		for j in range(i):
			print('.', end="")
		for j in range(SIZE-i):
			print('\\', end="")
			print('/', end="")
		for j in range(i):
			print('.', end="")
		print('|', end="")
		print("")



###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()