
from art import logos
from random import randint
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# Function to check users' guess aginst actual answer 
def check_answer(user_guess, actual_answer):
    if user_guess > actual_answer:
        print("To high")
    elif user_guess < actual_answer:
        print("Too low")
    else:
        print(f"You got it! The answer was {actual_answer}")

# Function to set difficulty
def set_dificulty():
    level = input("Choos a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS



# Choosing a random number between 1 and 100
print("Welcome to the number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
answer = randint(1, 100)
print(f"Passt, the correct answer is {answer}")


turns = set_dificulty()
print(f"You have {turns} attempts remaining to guess the number. ")



# Let the user guess a number
guess = int(input("Make guess: "))
check_answer(guess, answer)



# Track the number of turns and reduce by 1 if they get it wrong 

# Repeat the guessing functionsty if they get it wrong
