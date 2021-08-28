import random
from words import words
import string

def get_valid_word(words):
    word=random.choice(words)
    while '-' in word or ' ' in word:
        word=random.choice(words)

    return word.upper()


def hangman():
    word=get_valid_word(words)
    word_letters=set(word)
    alphabet=set(string.ascii_uppercase)
    used_letters=set()
    lives=6

    while len(word_letters)>0 and lives>0:
        print('You have' ,lives, 'lives left. You have used the letters',' '.join(used_letters))

        wordlist=[letter if letter in used_letters else '_' for letter in word]
        print('current word:',' '.join(wordlist))

        user_letter=input('Guess a letter:').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives=lives-1
                if lives!=0:
                    print("Wrong guess.Try again.")
        elif user_letter in used_letters:
                print("\nYou have already used this letter")
        else:
                print("\nInvalid character")
    if(lives==0):
        print("You died :(")
    else:
        print(f'\n Yes!!the word is {word}')

if __name__ == '__main__':
    hangman()


