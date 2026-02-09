import random
counter=0

jackpot=random.randint(1,100)
guess=int(input("Guess the Number"))
while guess!=jackpot:
    if guess <jackpot:
        print("Guess Higher")
    else:
        print("Guess Lower")

    counter +=1
    guess=int(input("Guess the Number"))

counter +=1
print("Right Answer")
print("You took",counter,"attempts")