
trials = 5
trials_count = 0
win = 0
No_0f_wins = win

out_of_trials = False
import random
while True and not out_of_trials:
    user_guess = input("Enter any guess from game choices: ").lower()
    game_choices = "rock", "paper", "scissors"
    comp_guess = random.choice(game_choices).lower()
    if trials_count <= trials:
        if user_guess == comp_guess:
            print(f"Both players selected {user_guess}, It`s a Tie")
            trials_count += 1
        elif user_guess == "rock":
            if comp_guess == "paper":
                print("Paper covers rock, you lose")
            else:
                print("Rock smashes scissors, You win!")
            win += 1
            trials_count += 1
        elif user_guess == "paper":
            if comp_guess == "rock":
                print("Paper covers rock, You win!")
            else:
                print("Scissors cuts paper, you lose!")
            win += 1
            trials_count += 1
        elif user_guess == "scissors":
            if comp_guess == "paper":
                print("Scissors cuts paper, You win!")
            else:
                print("Rock smashes scissors, You lose!")
            win += 1
            trials_count += 1
        elif user_guess == "Exit":
            break
        else:
            print("THE END")
    else:
        out_of_trials = True
        print("You are out of guesses.")
print("You won ", No_0f_wins)