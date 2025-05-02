from random import randint
from art import logos

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to check users' guess against actual answer 
def check_answer(user_guess, actual_answer):
    if user_guess > actual_answer:
        print("Too high")
        return False
    elif user_guess < actual_answer:
        print("Too low")
        return False
    else:
        print(f"You got it! The answer was {actual_answer}")
        return True

# Function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level.lower() == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

# Main game function
def play_game():
    print(logos)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    # print(f"Psst, the correct answer is {answer}")  # For testing only

    turns = set_difficulty()

    while turns > 0:
        print(f"\nYou have {turns} attempts remaining to guess the number.")
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        is_correct = check_answer(guess, answer)
        if is_correct:
            break
        turns -= 1

        if turns == 0:
            print(f"\nYou've run out of guesses. The answer was {answer}.")
        else:
            print("Guess again.")

# Run the game
play_game()
