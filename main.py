# Rock, Paper, Scissors Game 
#Learnug here
import random 

while True:
    Player = input("Enter a choice R(rock), P(paper), S(scissors):")
    possible_action = ["R", "P", "S"]
    CPU = random.choice(possible_action)
    print(f"\nYou chose {Player}, computer chose {CPU}.\n")

    if Player == CPU:
        print(f"Both players selcted {Player}. It's a tie!")
    elif Player == "R":
        if CPU == "S":
            print("Player(R): CPU(S) rock smashes scissors!, You win!")
        else:
            print("Player(R): CPU(P) Paper covers rock! You lose!")
    elif Player == "P":
        if CPU == "R":
            print("Player(P): CPU(R) paper covers rock! You win!")
        else:
            print("Player(P): CPU(S) scissors cuts paper! You lose!")
    elif Player == "S":
        if CPU == "P":
            print("Player(S): CPU(P) scissors cuts paper! You win!")
        else:
            print("Player(S): CPU(R) rock smashes scissors!, You lose!")
        
    else:
        print("That's not a valid input. Check your spelling!")           
            
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
