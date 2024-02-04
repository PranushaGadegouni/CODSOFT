import random

def get_user_choice():
    """
    Function to get the user's choice for Rock, Paper, or Scissors.
    Validates the input and prompts the user until a valid choice is entered.
    """
    while True:
        user_choice = input("Choose Rock, Paper, or Scissors: ").capitalize()
        if user_choice in ["Rock", "Paper", "Scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")

def get_computer_choice():
    """
    Function to generate a random choice for the computer (Rock, Paper, or Scissors).
    """
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """
    Function to determine the winner based on user and computer choices.
    Uses a dictionary to define winning conditions and checks for ties.
    """
    # Using a dictionary to define winning conditions
    win_conditions = {
        ("Rock", "Scissors"): "You win!",
        ("Paper", "Rock"): "You win!",
        ("Scissors", "Paper"): "You win!"
    }

    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice, computer_choice) in win_conditions:
        return win_conditions[(user_choice, computer_choice)]
    else:
        return "Computer wins!"

def main():
    """
    Main function to execute the Rock, Paper, Scissors game.
    """
    print("Welcome to Rock, Paper, Scissors!")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose {user_choice}.")
        print(f"Computer chose {computer_choice}.")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
