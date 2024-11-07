import random
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(player_choice: str, computer_choice: str) -> str:
    if player_choice == computer_choice:
        return "It's a draw"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
    (player_choice == "paper" and computer_choice == "rock") or \
          (player_choice == "scissors" and computer_choice == "paper"):
        return "You Win!"
    else:
        return "You Lose!"

def play_game():
    print("Welcome to Rock, Paper, Scissors")

    while True:
        player_choice = input("Enter your choice (rock, paper, scissors), or type 'stop' to end the game: ").lower()

        if player_choice == "stop":
            print("Thanks for playing!")
            break
        
        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice")
            continue
        
        computer_choice = get_computer_choice()
        print(f"The computer chose: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)
        print(result)

play_game()