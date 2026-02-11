import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
items = [rock, paper, scissors]
index = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors.\n"))
if index>=0 and index<=2:
    user = items[index]
    print(user)
    numb = random.randint(0, 2)
    computer = items[numb]
    print("Computer chose:\n "+computer)
    if user == rock:
        if computer == paper:
            print("You lost")
        elif computer == scissors:
            print("You won!")
        else:
            print("It is a tie")
    elif user == paper:
        if computer == paper:
            print("It is a tie")
        elif computer == scissors:
            print("You lost")
        else:
            print("You won")
    else:
        if computer == paper:
            print("You won")
        elif computer == scissors:
            print("It is a tie")
        else:
            print("You lost")
else:
    print("Invalid number!")



