import random
import math

def main():
    try:
        lower = int(input("Enter the lower bound of the range: "))
        upper = int(input("Enter the upper bound of the range: "))
    except ValueError:
        print("Please enter valid integers for the range.")
        return

    if lower >= upper:
        print("Invalid range! Lower bound must be less than upper bound.")
        return

    secret_number = random.randint(lower, upper)
    max_chances = math.ceil(math.log2(upper - lower + 1))

    print(f"\nI have picked a number between {lower} and {upper}.")
    print(f"You have {max_chances} chances to guess it correctly!\n")

    for attempt in range(1, max_chances + 1):
        try:
            guess = int(input(f"Attempt {attempt}: Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if guess == secret_number:
            print(f"🎉 Congratulations! You guessed the number in {attempt} attempt(s).")
            break
        elif guess < secret_number:
            print("Your guess is too low. Try again!")
        else:
            print("Your guess is too high. Try again!")
    else:
        print(f"\n😢 You've used all your chances.")
        print(f"The correct number was: {secret_number}")
        print("Better luck next time!")

if __name__ == "__main__":
    main()
