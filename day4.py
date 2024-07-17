
'''
heads_tails = random.randint(0,1)
if heads_tails == 0:
    print("Tails")
else:
    print("Heads")
'''
'''
sse = ["ES", "MG", "SP", "RJ"]
sou = ["RS", "SC", "PR"]

ss = [sou, sse]
print(ss)
num_of_ss = len(ss)
print(num_of_ss)
'''
'''
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[0][1])
'''


# ROCK PAPER AND SCISSORS PROJECTS #

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

import random

game_images = [rock, paper, scissors]
user_choice = int(input("Welcome to the Rock, paper and scissors game. Choose '0' for Rock. Choose '1' for paper. Choose '2' for scissors\n"))
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number")
else:
    print(game_images[user_choice])
    computer_choice = random.randint (0,2)
    print(f"Computer chose: ")
    print (game_images [computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You win")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("Computer wins")
    elif user_choice > computer_choice:
        print ("You win")
    elif computer_choice == user_choice:
        print("It's a draw")
    elif user_choice >= 3 or user_choice < 0:
        print("You typed an invalid number")


















