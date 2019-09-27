import random

choice = ["rock", "paper","scissors"]

computer = choice[random.randint(0,2)]

print('Welcome to the Rock, Paper, Scissors Game\n')
player = input("Your Choice: ").lower()

print("Computer Choice: " + computer)

if player == computer:
    print("Draw")
elif player == "rock" and computer == "paper":
    print("Computer Wins")
elif player == "rock" and computer == "scissors":
    print("Player Wins")
elif player == "paper" and computer == "rock":
    print("Player Wins")
elif player == "paper" and computer == "scissors":
    print("Computer Wins")
elif player == "scissors" and computer == "rock":
    print("Computer Wins")
elif player == "scissors" and computer == "paper":
    print("Player Wins")
elif player != "rock" and "paper" and "scissors":
    print("Help:\n")
    print("Type rock, paper or scissors")
    
