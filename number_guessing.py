import random
a = int(input ("Enter the bottom of the range: "))
b = int(input ("Enter the top of the range: "))
r = random.randint (a,b)
guess_count= 0
while True:
    guess = int(input("What's your guess?: "))
    if guess < r:
        print ("guess a larger number")
        guess_count += 1
    elif guess > r:
        print ("guess a smaller value")
        guess_count += 1
    else:
        print ("You've guessed the number correctly!")
        guess_count += 1
        break

print (f"You guessed the number in {guess_count} tries.")




