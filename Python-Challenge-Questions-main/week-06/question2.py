import random

print("I have picked a number between 1 and 100.")

random_number = random.randint(1, 100)

is_game_on = True
counter = 0
while is_game_on:
    guess = int(input("Guess the number: "))
    if guess < random_number:
        print("Increase your guess.")
    elif guess > random_number:
        print("Decrease your guess.")
    else:
        print(f"Your guess was correct! correct number was {random_number}")
        is_game_on = False
    counter += 1


print(f"You found the correct answer after {counter} attempts")
