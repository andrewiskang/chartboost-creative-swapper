import random

def roll():
    number = random.randint(0, 6)
    print("Your number is %d!" % number)

roll()

again = input("Would you like to roll another? Answer with yes/no: ")

again = again.lower()

if again == "yes":
    roll()
elif again == "no":
    print("Okay.")
else:
    print("I didn't understand that, please try again.")
