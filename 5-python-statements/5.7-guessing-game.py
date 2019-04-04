#The Challenge:
#Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:
#If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
#On a player's first turn, if their guess is
#within 10 of the number, return "WARM!"
#further than 10 away from the number, return "COLD!"
#On all subsequent turns, if a guess is
#closer to the number than the previous guess return "WARMER!"
#farther from the number than the previous guess, return "COLDER!"
#When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!
#You can try this from scratch, or follow the steps outlined below. A separate Solution notebook has been provided. Good luck!
from random import randint
import math
# randint returns a random integer in range [a, b], including both end points.
print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")
num = randint(1,100)
new_guess, prev_guess, count = 0, 0, 0
while new_guess != num:
    new_guess = int(input("Enter a number! "))
    count += 1
    if new_guess < 1 or new_guess > 100:
        print('OUT OF BOUNDS! Please try again: ')
        continue
    if new_guess == num:
        print(f"You won! Number of guesses is {count}")
        break
    if (count == 1):
        if math.fabs(num - new_guess) < 10:
            print("WARM!")
        else:
            print("COLD!")
        prev_guess = new_guess
        continue
    if(math.fabs(num - new_guess)) < (math.fabs(num - prev_guess)):
        print("WARMER!")
    else:
        print("COLDER!")
    prev_guess = new_guess
