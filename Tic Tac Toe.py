def sum(a, b, c):  # override sum function with three arguments
    return a + b + c


def printBoard(xState, zState):  # print board into the terminal
    one = 'X' if xState[0] else ('O' if zState[0] else " ")
    two = 'X' if xState[1] else ('O' if zState[1] else " ")
    three = 'X' if xState[2] else ('O' if zState[2] else " ")
    four = 'X' if xState[3] else ('O' if zState[3] else " ")
    five = 'X' if xState[4] else ('O' if zState[4] else " ")
    six = 'X' if xState[5] else ('O' if zState[5] else " ")
    seven = 'X' if xState[6] else ('O' if zState[6] else " ")
    eight = 'X' if xState[7] else ('O' if zState[7] else " ")
    nine = 'X' if xState[8] else ('O' if zState[8] else " ")
    print(f" {one} | {two} | {three} ")
    print(f"---|---|---")
    print(f" {four} | {five} | {six} ")
    print(f"---|---|---")
    print(f" {seven} | {eight} | {nine} ")


def checkWin(xState, zState, player1_name, player2_name):
    win_conditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 8]]
    for win_condition in win_conditions:
        if sum(xState[win_condition[0]], xState[win_condition[1]], xState[win_condition[2]]) == 3:
            print(f"\n{player1_name.capitalize()} won...!")
            return 1

        if sum(zState[win_condition[0]], zState[win_condition[1]], zState[win_condition[2]]) == 3:
            print(f"\n{player2_name.capitalize()} won...!")
            return 0

        return -1


if __name__ == "__main__":
    print("Welcome to Tic Tac Toe")
    player1_name = input("Please enter player 1 name: ")
    player2_name = input("Please enter player 2 name: ")
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1  # 1 for player1 and 0 for player2
    while True:
        printBoard(xState, zState)  # for print board
        win = checkWin(xState, zState, player1_name, player2_name)
        if win != -1:  # check wining player
            break

        if turn == 1:
            print(f"----{player1_name.capitalize()}'s chance----")
            choice = int(input("Enter your choice between 1 to 9: "))
            xState[choice - 1] = 1
        else:
            print(f"----{player2_name.capitalize()}'s chance----")
            choice = int(input("Enter your choice between 1 to 9: "))
            zState[choice - 1] = 1

        turn = 1 - turn
