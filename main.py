import random

# Computer move
computer_Move = random.choice(["rock", "paper", "scissors"])

# Player move
player_Move = input("Enter your move (rock, paper, scissors): ").lower()

# Initialize result
result = ""

# Validate input
if player_Move not in ["rock", "paper", "scissors"]:
    print("Invalid move! Please choose rock, paper, or scissors.")
else:
    # Display computer move
    print(f"Computer chose {computer_Move}.")

    # Determine result
    if computer_Move == player_Move:
        result = "It's a draw!"
    elif (computer_Move == "rock" and player_Move == "paper") or \
         (computer_Move == "paper" and player_Move == "scissors") or \
         (computer_Move == "scissors" and player_Move == "rock"):
        result = "You won! 🎉"
    else:
        result = "You lost! 😢"

    # Print final result
    print(f"You chose {player_Move} and {result}")
