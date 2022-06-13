import random #this calls the function random

choices = ['R', 'P', 'S'] #this is a list of choices for the computer to select from
print('This is a game of Rock, Paper, Scissors. \nYou would be going up against the computer.')

#this is a while loop for running the game.
while True:
    player = input("Enter 'R' for Rock, 'P' for Paper, 'S' for Scissors: ").upper()
    computer = random.choice(choices)  #computer can randomly pick from the list of choices.
    if player == 'R' and computer == 'R':
        print('Player(Rock) : CPU(Rock)')
        print("It's a draw.")
        break
    elif player == 'P' and computer == 'P':
        print('Player(Paper) : CPU(Paper)')
        print("It's a draw.")
        break
    elif player == 'S' and computer == 'S':
        print('Player(Scissors) : CPU(Scissors)')
        print("It's a draw.")
        break
    elif player == 'P' and computer == 'R':
        print('Player(Paper) : CPU(Rock)')
        print("You win!")
        continue
    elif player == 'R' and computer == 'P':
        print('Player(Rock) : CPU(Paper)')
        print("You lose!")
        continue
    elif player == 'R' and computer == 'S':
        print('Player(Rock) : CPU(Scissors)')
        print("You win!")
        continue
    elif player == 'S' and computer == 'R':
        print('Player(Scissors) : CPU(Rock)')
        print("You lose!")
        continue
    elif player == 'P' and computer == 'S':
        print('Player(Paper) : CPU(Scissors)')
        print("You lose!")
        continue
    elif player == 'S' and computer == 'P':
        print('Player(Scissors) : CPU(Paper)')
        print("You win!")
        continue
    else:
        print('Invalid input. Try again.')