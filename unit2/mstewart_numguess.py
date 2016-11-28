import random
num = random.randint(0,100)
num_guess = int(input("Guess a number between 1 and 100: "))
guesses_taken = 0
while(num >= 1 or num <= 100):
    if num_guess > num:
        print("Too high! Try again.")
        num_guess = int(input("Guess a number between 1 and 100: "))
        guesses_taken =  guesses_taken + 1
    elif num_guess < num:
        print("Too low! Try again.")
        num_guess = int(input("Guess a number between 1 and 100: "))
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