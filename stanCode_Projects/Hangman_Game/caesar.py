"""
File: caesar.py
Name: Serena Liu
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    This program deciphers the ciphered string.
    """
    n = int(input("Secret Number: "))
    s = input("What's the ciphered string? ")
    string = s.upper()
    new_alphabet = cipher(n)
    d_string = replace(string, new_alphabet, ALPHABET)
    print("The deciphered string is: " + str(d_string))


def cipher(n):
    """
    :param n: int, the number of letters in alphabet will wrap around
    :return: str, letters in new alphabet order
    """
    ans = ''
    for i in range(n):
        ans += ALPHABET[i+26-n]
    ans += ALPHABET[:26-n]
    return ans


def replace(s, new_a, a):
    """
    :param s: str, ciphered string
    :param new_a: str, letters in the new alphabet order
    :param a: str, letters in the alphabet
    :return: str, deciphered string
    """
    ans = ''
    for i in range(len(s)):
        if s[i] in a:
            j = new_a.find(s[i])
            ans += a[j]
        else:
            ans += s[i]
    return ans




#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
