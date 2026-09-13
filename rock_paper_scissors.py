import random
user_wins = 0
computer_wins = 0
while True:
    user_input = input ("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        print ("Bye! see you soon!")
        print (f"user wins {user_wins} times.")
        print (f"computer wins {computer_wins} times.")
        break
        
    if user_input not in ["rock", "paper", "scissors"]:
        print ("Invalid input")
        continue 
    random_number = random.randint(1,3)
    if random_number == 1:
        if user_input == "rock":
            print ("draw")
        elif user_input == "paper":
            print ("you won!")
            user_wins += 1
        else:
            print ("computer won :( ")
            computer_wins += 1
    elif random_number == 1:
        if user_input == "rock":
            print ("computer won :( ")
            computer_wins += 1
        elif user_input == "paper":
            print ("draw")
        else:
            print ("you won!")
            user_wins += 1
    elif random_number == 2:
        if user_input == "rock":
            print ("you won!")
            user_wins += 1
        elif user_input == "paper":
            print ("computer won :( ")
            computer_wins += 1
        else:
            print ("draw")


        









