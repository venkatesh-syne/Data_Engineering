import random

secret = random.randint(1, 10)

while True:
    guess = int(input("Guess number (1-10): "))
    if guess == secret:
        print("Correct!")
        break
    else:
        print("Try again")