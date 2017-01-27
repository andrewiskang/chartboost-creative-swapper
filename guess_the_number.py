import random

print("Let's play a guessing game!")
print("I'm thinking of a number from 1 to 100. Can you guess it?")
print("I'll let you know if the number is higher or lower than your guess,")
print("So try to get the answer in as little guesses as possible!\n")

# x refers to the randomized answer
x = str(random.randint(0, 100))

# n refers to the number of guesses (starts at 0)
n = 0

while True:
    guess = input("Guess my number (1-100), or type 'giveup' to stop playing: ")
    n += 1
    if guess.lower() == "giveup":
        print("You gave up with %d guesses.\n" % n)
        break
    elif guess == x:
        print("You win!\n Number of guesses: %d" % n)
        break
    elif guess < x:
        print("Wrong! The real number is higher than your guess.\n")
    elif guess > x:
        print("Wrong! The real number is lower than your guess.\n")
    else:
        print("What? %s does not work as a guess, try guessing again.\n" % guess)
