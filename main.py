import random

randomNumber = str(random.randrange(1000, 10000))

print("Welcome to Mastermind Game! Try to guess the number which ranges from 1000 to 10000 (exlusively)! Good luck! :)")

while True:
    try:
        userGuess = int(input("Type your 4-digits long guess here: "))
    except ValueError:
        print("Your guess must be an integer that ranges from 1000 to 10000 (exclusively). Please try again.")
        continue
    if userGuess < 1000 or userGueAss >= 10000:
        print("The digit must be in range betweeen 100- and 10000 (exclusively).")
        continue

    userGuess = str(userGuess)
    result = ""
    countCorrectDigits = 0
    
    for i in range(len(randomNumber)):
              if userGuess[i] == randomNumber[i]:
                result += userGuess[i]
                countCorrectDigits += 1
              else:
                result += "X"

    if countCorrectDigits == len(randomNumber):
        print("Congratulations! You won! The guessed number was:", randomNumber)
        res = input("Would you like to keep playing (y/n): ").strip().lower()
        if res == 'y':
            print("Perfect! Let's keep playing!")
            randomNumber = str(random.randrange(1000, 10000))
            continue
        else:
            print("See you next time! :)")
            break

    print("You got", countCorrectDigits, "digits correct!:", result)
    print("Keep going!")
