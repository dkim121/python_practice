import random

secretNumber = random.randint(1, 30)
print("I am thinking about a number between 1 and 30.")

# Player can guess maximum 6 times.
for guessTaken in range(1, 7):
    print("Take a guess.")
    guess = int(input())

    if guess < secretNumber:
        print("Your number is too low.")
    elif guess > secretNumber:
        print("Your number is too high.")
    else:
        print("You're right!")
        break

if guess == secretNumber:
    print("Good job! You guessed my number in " + str(guessTaken) + " guesses!")

else:
    print("Nope, The number I was thinking of was " + str(secretNumber))
