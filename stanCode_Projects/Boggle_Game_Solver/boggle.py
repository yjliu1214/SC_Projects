"""
File: boggle.py
Name: Serena Liu
----------------------------------------
The program prints all words within a 4x4 boggle gird entered by user.
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
dictionary = []


def main():
	"""
	The program prints all words within a 4x4 boggle gird entered by user.
	"""
	letters =[]
	for roll in ['1', '2', '3', '4']:
		rows = str(input(roll+' row of letters: '))
		if rows[1] != ' ' or rows[3] != ' ' or rows[5] != ' ':
			print('Illegal input!')
			break
		else:
			rows.lower()
			letters += rows.split(' ')
	if len(letters) == 16:
		global dictionary
		dictionary = read_dictionary()
		sub_dict = []
		for letter in letters:
			for word in dictionary:
				if word.startswith(letter):
					sub_dict += [word]
		dictionary = sub_dict
		words = []
		for i in range(len(letters)):
			boggle(letters, letters[i], [i], words, i)
		print('There is', str(len(words)), 'words in total.')


def boggle(letters, current_str, index_lst, words, i):
	if len(current_str) >= 4:
		if current_str in dictionary and current_str not in words:
			words += [current_str]
			print('Found: '+current_str)
			if has_prefix(current_str):
				for j in range(-4, 5, 4):
					for k in range(-1, 2, 1):
						index = i + j + k
						if (i % 4 == 0 and k == -1) or (i % 4 == 3 and k == 1):
							pass
						else:
							if index not in index_lst and 0 <= index <= 15:
								index_lst.append(index)
								current_str += letters[index]
								i = index
								boggle(letters, current_str, index_lst, words, i)

								index_lst.pop()
								i = index_lst.pop()
								index_lst.append(i)
								current_str = current_str[:len(current_str) - 1]
	else:
		if has_prefix(current_str) is False:
			pass
		else:
			for j in range(-4, 5, 4):
				for k in range(-1, 2, 1):
					index = i + j + k
					if (i % 4 == 0 and k == -1) or (i % 4 == 3 and k == 1):
						pass
					else:
						if index not in index_lst and 0 <= index <= 15:
							index_lst.append(index)
							current_str += letters[index]
							i = index
							boggle(letters, current_str, index_lst, words, i)

							index_lst.pop()
							i = index_lst.pop()
							index_lst.append(i)
							current_str = current_str[:len(current_str) - 1]


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	d = []
	with open(FILE, 'r') as f:
		for line in f:
			d += [line.strip('\n')]
	return d


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dictionary:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
