import time
lives = 5
stringword ="Apple"
word = list("Apple".lower())
guess = ["_"]*len(word)
winner = False
incorrectLetters = []

def printscore():
    print("\n\n\nLives: "+str(lives))
    print("Incorrect letters: ")
    for x in range(len(incorrectLetters)):
        if x == len(incorrectLetters)-1:
            print(incorrectLetters[x], end="")
        else:
            print(incorrectLetters[x], end=",")
        print("")
    for x in range(len(guess)):
        if x == len(guess)-1:
            print(guess[x], end="")
        else:
            print(guess[x], end=",")
        print("")

def askforletter():
    letterguess= input("Please guess a letter: ").lower()
    correct = False
    for x in range(len(word)):
        if(letterguess== word[x]):
            guess[x]=letterguess
            correct = True
    if correct:
        print("You got one!")
    else:
        print("Oh no! That wasn't in there")
        incorrectLetters.append(letterguess)
        global lives
        lives-=1
    time.sleep(1)


def checkwinner():
    if "_" not in guess:
        global winner
        winner = True


while lives >0 and winner == False:
    printscore()
    #Ask user for a letter
    askforletter()

    checkwinner()

    if(lives<=0):
        print("You lost!  the word was: "+stringword)
    else:
        print("Congratzzz you won! 😁😎 With "+str(lives) +" left")
print(word)
