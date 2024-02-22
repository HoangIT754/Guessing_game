import random

def start_game():
    print("----------------------------------------")
    print("  Welcome to the Number Guessing Game!  ")
    print("----------------------------------------")

    player_choose = "yes"
    high_score = float('inf')

    while player_choose.lower() == "yes":
        num_guess = random.randint(1, 10)

        count = 0
        while True:
            try:
                num_player = int(input("Pick a number between 1 and 10: "))
                if 1 <= num_player <= 10:
                    break
                else:
                    print("Your number is out of range. Please enter a number between 1 and 10.")
            except ValueError:
                print("It is not a number! Please enter an integer between 1 and 10.")

        while num_guess != num_player:
            if num_player < num_guess:
                print("It is higher!")
            else:
                print("It is lower!")
            count += 1

            while True:
                try:
                    num_player = int(input("Try again: "))
                    if 1 <= num_player <= 10:
                        break
                    else:
                        print("Your number is out of range. Please enter a number between 1 and 10.")
                except ValueError:
                    print("It is not a number! Please enter an integer between 1 and 10.")

        count += 1
        print("You got it! It took you", count, "tries.")

        if count < high_score:
            high_score = count

        player_choose = input("Would you like to play again? [yes/no]: ")

    print("The HIGHSCORE is", high_score, "tries. Goodbye!")


start_game()
