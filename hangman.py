import random

from words import words

import string

def get_valid_word(words):

    word = random.choice(words) # randomly chooses something from the list

    while '-' in word or " " in word:

        word = random.choice(words)

    return word

def hangman():

    word = get_valid_word(words).upper()
    print(word)

    word_letters = list(word) # letters in the word

    alphabet = set(string.ascii_uppercase)
    
    used_letters = set() # keep track of what the user has guessed

    lives = 6

    #getting user input

    while (len(word_letters) > 0) and (lives > 0):

        #letters used

        #" ".join(['a', 'b', 'cd']) --> "a b cd"

        print("You have ", lives, "lives left and You have used these letters: ", " ".join(used_letters))

        # what current word is (that is W -R D)
        word_list = [] 
        for letter in word:
            if letter in used_letters:
                word_list.append(letter)
            else: 
                word_list.append("-")

        # word_list = [letter if letter in used_letters else "-" for letter in word_letters]
        print(word_list)

        print("current word: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            
            used_letters.add(user_letter)

            if user_letter in word_letters:

                word_letters.remove(user_letter)
            
            else:
                lives = lives - 1 # takes away a live when a wrong letter is guessed
                print("letter is not in word.")

        elif user_letter in used_letters:

            print("You have already used that character. Please try another one.")

        else:

            print("Invalid character. Please try again")

        for i in used_letters:
            if i in word:
                break

    # gets here when len(word_letters) == 0 or when lives == 0
    if lives == 0:
        print("You died, Sorry. The word was", word)
    else:
        print("Congratulation. You guessed the word", word, "!!!")


hangman()
