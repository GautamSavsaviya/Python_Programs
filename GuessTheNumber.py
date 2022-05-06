NoOfGuess = 5
TotalGuess = 0
print("You have only 9 turn to guess the number")

while True:
    num = int(input("Enter the number that you guess: "))
    if num < 23:
        print("Your number is lower than my number")
        NoOfGuess -= 1
        TotalGuess += 1
        print("Total turn you took: " + str(TotalGuess))
        print("Total turn left: " + str(NoOfGuess))
        if TotalGuess == 9:
            print("You lose the game")
            break

    elif num > 23:
        print("Your number is greater than my number")
        NoOfGuess -= 1
        TotalGuess += 1
        print("Total turn you took: " + str(TotalGuess))
        print("Total turn left: " + str(NoOfGuess))
        if TotalGuess == 9:
            print("You lose the game")
            break

    elif num == 23:
        print("Your number is match with my number")
        print("You won the game")
        print("You have took " + str(TotalGuess) + "turn for win the match")
        print("Total turn left: " + str(NoOfGuess))
        break


    