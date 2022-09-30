import random
from time import sleep

# Computer picks a number
compick = random.randrange(0,25)
# Main game loop
guessed = False
score  = 100
guesses = 0
sleep(0.5)
gamemode = input("Would you like to play in regular or hard mode? (r/h)")
if gamemode == "r":
    print("You will have 5 guesses to guess the number from 1-25. Each consecutive incorrect guess will reduce your score by 10 and give you a hint. Once the score reaches 0, the game ends.")
elif gamemode == "h":
    print("You will have 5 guesses to guess the number from 1-25. Each consecutive incorrect guess will reduce your score by 10. Once the score reaches 0, the game ends."
sleep(2)
print(f"Your score is {score}")

# Define hints
def hintfunc(ug):
        hinttype = random.randrange(1,4)
        cprand = random.randrange(1,5)
        cpover = (compick - cprand)
        cpunder = (compick + cprand)
        if hinttype == 1 and type(ug) == int:
            print(f"HINT: The number is over {cpover}")

        elif hinttype == 2 and type(ug) == int:
            print(f"HINT: The number is under {cpunder}")
        
        elif hinttype == 3 or 4 and type(ug) == int:
            if (compick%2) == 0: # Returns remainder: if its 0, the number is even 
                sleep(0.5)
                print(f"HINT: The number is an even number")

            elif (compick%2) > 0: # Returns remainder: if its greater than 0, the number is odd
                sleep(0.5)
                print(f"HINT: The number is an odd number")




while guessed == False:
    #print(compick)
    userguess = int(input("Guess the number "))

    if int(userguess) == compick:
        sleep(0.5)
        print(f"Good Job! You guessed the number! Your score is {score}")
        guessed == True
        break

    elif int(userguess) != compick:
        sleep(0.5)
        print("Oops, wrong number, try again")
        sleep(0.5)
        if gamemode == "r":
            hintfunc(userguess)
            score -=10
        elif gamemode == "h":
            score -= 10
        print(f"Your score is {score}")

    
    if score <= 0:
        sleep(0.5)
        print(f"Oops, looks like you failed to guess the number. It was {compick}")
        break
