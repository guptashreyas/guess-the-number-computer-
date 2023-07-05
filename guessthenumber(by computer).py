import random


def guess_number():
    low = 1
    high = 100
    guessed = False

    print("Think of a number between 1 and 100.")

    while not guessed:
        guess = random.randint(low, high)
        feedback = input(
            f"Is {guess} too high (H), too low (L), or correct (C)? "
        ).upper()

        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
        elif feedback == "c":
            guessed = True
            print("Hooray! The computer guessed the number correctly.")
        else:
            print("Invalid input. Please enter 'H', 'L', or 'C'.")


guess_number()
