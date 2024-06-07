import random

def guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guess = None

    print("Welcome to the Guessing Game!")
    print("I have generated a random number between 1 and 100.")
    print("Try to guess the number!")

    while guess != number_to_guess:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    print(f"Congratulations! You guessed the number {number_to_guess} correctly.")
    print(f"It took you {attempts} attempts to guess the number.")

if __name__ == "__main__":
    guessing_game()
