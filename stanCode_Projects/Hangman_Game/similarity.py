"""
File: similarity.py
Name: Serena Liu
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    This program finds the sub sequence in a long dna sequence that has the best similarity with short dna sequence.
    """
    long_dna = input('Please give me a DNA sequence to search: ')
    short_dna = input('What DNA sequence would you like to match? ')
    s1 = long_dna.upper()
    s2 = short_dna.upper()
    match = check_similarity(s1, s2)
    print('The best match is ' + match)


def check_similarity(s1, s2):
    """
    :param s1: str, long DNA sequence
    :param s2: str, short DNA sequence
    :return: best match sequence
    """
    m = ''
    same = 0
    maximum = same
    for i in range(len(s1)-len(s2)+1):
        same = 0
        for j in range(len(s2)):
            if s2[j] == s1[j+i]:
                same += 1
        if same > maximum:
            maximum = same
            m = s1[i:(i+len(s2))]
    return m


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
