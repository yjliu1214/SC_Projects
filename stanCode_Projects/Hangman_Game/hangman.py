"""
File: hangman.py
Name: Serena Liu
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random

# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This program plays hangman game.
    """
    number = N_TURNS
    word = random_word()
    hint = dashed(word)
    print('The word looks like: ' + hint)
    while hint != word:
        guess = input('Your guess: ')
        guess = guess.upper()
        if guess.isalpha() and len(guess) == 1:
            if guess in word:
                new_hint = ''
                for i in range(len(word)):
                    if word[i] == guess:
                        new_hint += guess
                    else:
                        new_hint += hint[i]
                hint = new_hint
                if hint != word:
                    print('You are correct!')
                    print('The word looks like: ' + hint)
                    print('Yoe have ' + str(number) + ' guesses left.')
                else:
                    print('You are correct!')
                    print('You win!!')
                    print('The word was: ' + word)
                    break
            else:
                number -= 1
                if number != 0:
                    print('There is no ' + guess + "'s in the word.")
                    print('The word looks like: ' + hint)
                    print('Yoe have ' + str(number) + ' guesses left.')
                else:
                    print('There is no ' + guess + "'s in the word.")
                    print('You are completely hung :( ')
                    print('The word was: ' + word)
                    break
        else:
            print('illegal format.')


def dashed(word):
    letters = ''
    for i in range(len(word)):
        letters += '_'
    return letters


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
