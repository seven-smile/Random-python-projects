import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low #this could also be high,since low = 
        feedback = input(f"Is {guess} too high (H)?, too low (L)? or correct (C)?? ").lower()
        if feedback == "h":
            high = guess  - 1
        elif feedback == "l":
            low = guess + 1
    print(f"yie yie, you did it, another banger!!!, for guessing {guess} as the correct number!. ay3kooo :) ")

computer_guess(1000)
 