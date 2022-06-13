import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_choice = input("choose  Rock R /Paper P /Scissors S or Q to quit: ").lower()
    print("Player:", user_choice + ".")
    if user_choice == "q":
        break
    if user_choice not in options:
        print("invalid choice, please try again")
        continue

    random_number = random.randint(0, 2)

       

    computer_choice = options[random_number]
    print("CPU:", computer_choice + ".")

    if user_choice == "rock" and computer_choice == "scissors":
        print("you won!")
        user_wins += 1

    elif user_choice == "paper" and computer_choice == "rock":
        print("you won!")
        user_wins += 1

    elif user_choice == "scissors" and computer_choice == "paper":
        print("you won!")
        user_wins += 1
    elif user_choice == computer_choice :
        print("Its a tie!!!")

    else:
        print("You lost")
        computer_wins += 1

print("You won", user_wins, "times.")
print("Computer won", computer_wins, "times.")
print("Thank you for playing")