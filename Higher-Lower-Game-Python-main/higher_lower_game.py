from higher_lower_art import logo, vs
from game_data import data
import random
print(logo)
score = 0
account_b = random.choice(data)

def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name},a {account_descr} from {account_country}"

def check_answer(guess, a_follower_acc, b_follower_acc):
    """" Take the guess and follower account, check whether guess is correct"""
    if a_follower_acc > b_follower_acc:
        return guess == "a"
    else:
        return guess =="b"

game_should_continue = True

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B'.").lower()
    a_follower_acc = account_a["follower_count"]
    b_follower_acc = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_acc, b_follower_acc)

    if is_correct:
        score += 1
        print(f"You are right! Current score: {score}")
    else:
        game_should_continue = False
        print(f"Sorry that is wrong! Final score: {score}")



