range1 = int(input("Pick the first number you want the number to be between: "))
range2 = int(input("Pick the second number you want the number to be between: "))
import random
num = random.randint(range1,range2)
num_guess = int(input("Guess a number between {} and {}, including {} and {}: ".format(range1, range2, range1, range2)))
guesses_taken = 0
while(num >= range1 or num <= range2):
    if num_guess > num:
        print("Too high! Try again.")
        num_guess = int(input("Guess a number between {} and {}, including {} and {}: ".format(range1, range2, range1, range2)))
        guesses_taken =  guesses_taken + 1
    elif num_guess < num:
        print("Too low! Try again.")
        num_guess = int(input("Guess a number between {} and {}, including {} and {}: ".format(range1, range2, range1, range2)))
        guesses_taken =  guesses_taken + 1
    elif num_guess == num:
        guesses_taken = guesses_taken + 1
        print("You got it! It was indeed {}.".format(num))
        if guesses_taken > 1:
            print("It took you {} tries.".format(guesses_taken))
            break
        elif guesses_taken == 1:
            print("It took you {} try.".format(guesses_taken))
            break
        break