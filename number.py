import random

randomNumber = random.randrange(1,10)
print(randomNumber)

userInput = int(input("Guess a number from 1 to 10: "))

while userInput != randomNumber:
    print("Thats Incorrect!")
    userInput = int(input("Guess a number from 1 to 10: "))

print("Thats correct!")