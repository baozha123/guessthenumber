import random

top_range = input("This is your guess range. Type a number above 0: ")

if top_range.isdigit():
    top_range = int(top_range)
else:
    print("Please type a number next time.")
    quit()

random_number = random.randint(0, top_range)
guesses = 0
while True:
    guesses += 1
    user_guess = input("Take a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    else:
        if user_guess > random_number:
            print("You were above the number")
        else:
            print("You were below the number")

print("You got it in", guesses, "guesses")