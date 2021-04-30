"""
File: anagram.py
Name: Serena Liu
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
dictionary = []


def main():
    print("Welcome to stanCode \"Anagram Generator\" (or -1 to quit)")
    global dictionary
    while True:
        word = str(input("Find anagrams for: "))
        word = word.lower()
        if word == EXIT:
            break
        else:
            letters = []
            dictionary = read_dictionary()
            for i in range(len(word)):
                if word[i] not in letters:
                    letters += word[i]
            sub_dict = []
            for w in dictionary:
                for letter in letters:
                    if w.startswith(letter) and len(w) == len(word):
                        sub_dict += [w]
            dictionary = sub_dict
            find_anagrams(word)


def find_anagrams(s):
    """
    :param s: str, the word input by user
    """
    anagrams = []
    num = [0]
    print('Searching...')
    helper(s, '', [], anagrams, num)
    print(str(num[0]) + ' anagrams: ' + str(anagrams))


def helper(s, current_lst, index_lst, anagrams, num):
    if len(current_lst) == len(s):
        if current_lst in dictionary and current_lst not in anagrams:
            anagrams += [current_lst]
            num[0] += 1
            print('Found: ' + current_lst)
            print('Searching...')
    else:
        for i in range(len(s)):
            if len(current_lst) >= 1 and has_prefix(current_lst) is False:
                break
            if i not in index_lst:
                index_lst.append(i)
                current_lst += s[i]

                helper(s, current_lst, index_lst, anagrams, num)

                index_lst.pop()
                current_lst = current_lst[:len(current_lst)-1]


def read_dictionary():
    d = []
    with open(FILE, 'r') as f:
        for line in f:
            d += [line.strip('\n')]
    return d


def has_prefix(sub_s):
    """
    :param sub_s: first letters of the word
    """
    for word in dictionary:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
