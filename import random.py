import random

print("=" * 40)
print("🎮 WELCOME TO NUMBER GUESSING GAME 🎮")
print("=" * 40)

while True:
    number = random.randint(1, 100)
    attempts = 0

    print("\nI have selected a number between 1 and 100.")
    print("Can you guess it?")

    while True:
        try:
            guess = int(input("\nEnter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")

            elif guess < number:
                print("Too Low! Try Again.")

            elif guess > number:
                print("Too High! Try Again.")

            else:
                print("\n🎉 Congratulations! You guessed the correct number.")
                print(f"It took you {attempts} attempts.")
                break

        except ValueError:
            print("Please enter a valid number.")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\nThank you for playing!")
        print("Have a great day! 😊")
        break