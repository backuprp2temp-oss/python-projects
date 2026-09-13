print ("Welcome to my computer quiz")
playing = input ("Do you want to play the game? ")
if playing.lower() != "yes" :
    quit()
print ("okay! let's play the game :)")
score = 0
answer = input ("What does GPU stand for? ")
if answer.lower() == "graphics processing unit" :
    print ("congratulations! your answer is correct!! ")
    score += 1
else:
    print ("Sorry, unfortunately the answer is incorrect :( ")

answer = input ("What is the full form of LLM? ")
if answer.lower() == "large language model" :
    print ("congratulations! your answer is correct!! ")
    score += 1
else:
    print ("Sorry, unfortunately the answer is incorrect :( ")

answer = input ("What does RSI stands for? ")
if answer.lower() == "recursive self-improvement" :
    print ("congratulations! your answer is correct!! ")
    score += 1
else:
    print ("Sorry, unfortunately the answer is incorrect :( ")

answer = input ("What is the study called where we reverse-engineer trained neural networks from their internal weights and activations down to human-understable algorithms?")
if answer.lower() == "mechanistic interpretability" :
    print ("congratulations! your answer is correct!! ")
    score += 1
else:
    print ("Sorry, unfortunately the answer is incorrect :( ")

print (f"Your final score is: {score}")
print ("The game has ended, Thank you!")


