import random

def number_guessing_game():
    # The computer randomly selects a number between 1 and 100
    secret_number = random.randint(1, 100)
    max_attempts = 5
    attempts = 0
    hint_provided = False  # Track if a hint has been provided
    
    print("Welcome to the Number Guessing Game!")
    print(f"I have selected a number between 1 and 100. Try to guess it within {max_attempts} attempts!")

    while attempts < max_attempts:
        # Get the user's guess
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        attempts += 1
        remaining_attempts = max_attempts - attempts
        
        # Check if the guess is correct, too low, or too high
        if guess < secret_number:
            print(f"Too low! Try again. You have {remaining_attempts} attempt(s) left.")
        elif guess > secret_number:
            print(f"Too high! Try again. You have {remaining_attempts} attempt(s) left.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
            break
        
        # Provide a very easy hint if only 2 attempts are left and a hint hasn't been given yet
        if remaining_attempts == 2 and not hint_provided:
            hint_provided = True
            if secret_number <= 25:
                print("Hint: The number is between 1 and 25.")
            elif secret_number <= 50:
                print("Hint: The number is between 26 and 50.")
            elif secret_number <= 75:
                print("Hint: The number is between 51 and 75.")
            else:
                print("Hint: The number is between 76 and 100.")
    
    else:
        # This block executes if the while loop completes without a break
        print(f"Sorry, you've used all {max_attempts} attempts. The number was {secret_number}.")

# Start the game
number_guessing_game()