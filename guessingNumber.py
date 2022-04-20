import random


chances = 5
num = 5

while chances >= 0:
    guessNumber = int(input("Enter Your Guess: \n"))

    if(guessNumber == num):
        print("You Won")
        print(num)
        break
    else:
        chances = chances - 1

        if(chances == 0):
            print("You Lost The Number Was ", num)
            break
        if(guessNumber > 5):
            print("Your Guess Was Too High: Guess a number lower than 8")
        if(guessNumber < 5):
            print("Your Guess Was Too Low: Guess a number higher than 4")
