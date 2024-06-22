import random

jackpot = random.randint(1, 100)

guess = int(input("guess a number: "))
counter = 1

while guess != jackpot:
    if guess < jackpot:
        print("guess higher")
    else:
        print("guess lower")
        
    guess = int(input("again guess a number: "))
    counter += 1
    
print("correct number")
print("you took", counter, "attempts")