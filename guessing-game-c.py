import  random

def guess(x):
    random_number = random.randint(1, x) #this returns a random number from 1 to x, that we need to guess. where x is the value of range
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        print(guess)
        if guess < random_number:
            print("Sorry, guess again. Too low.")
        elif guess > random_number:
            print("Sorry, guess again, Too high.")
    print(f"Hurray!!!!!, you entered the correct number which was <{random_number}>. Well Done.")
guess(10) 