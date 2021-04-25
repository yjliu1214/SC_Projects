"""
File: complement.py
Name: Serena Liu
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    This program finds complement strand of a DNA sequence.
    """
    d = input("Please give me a DNA strand and I'll find the complement: ")
    dna = d.upper()
    complement = build_complement(dna)
    print("The complement of " + dna + " is " + complement)


def build_complement(dna):
    """
    :param dna: str, a DNA stand
    :return: str, the complement of dna
    """
    ans = ''
    for i in range(len(dna)):
        if dna[i] == 'A':
            ans += 'T'
        elif dna[i] == 'T':
            ans += 'A'
        elif dna[i] == 'C':
            ans += 'G'
        elif dna[i] == 'G':
            ans += 'C'
    return ans



###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
