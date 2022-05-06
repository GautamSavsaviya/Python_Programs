# This is my first game
# Game name is Snake Water Gun
"""
    here is some game rules:
        * You can play only with computer.
        * You can choose one item from (Snake, Water, Gun)
        * If you choose 'Snake' and computer choose 'Water' then you earn 1 point
        * If you choose 'Water' and computer choose 'Gun' then you earn 1 point
        * If you choose 'Gun' and computer choose 'Snake' then you earn 1 point
        * Above last 3 rules is same for computer
"""


def random_choice():
    import random
    choice_list = ['snake', 'water', 'gun']
    computer_choice = random.choice(choice_list)
    return computer_choice


# start main program
print("---------Snake Water Gun---------")
player_name = input("Please, Enter your name: ")
print()
computer_point = 0
player_point = 0

# start while loop for start game
while True:
    # Select option for start game or show point table or quite game
    print("Select one option from the following:")
    print("\t 1)Play Game  2)Show Point Table  3)Quite Game\n")
    try:
        user_choice = int(input("Enter your selected option: "))
        print()

        # match case statement
        match user_choice:
            case 1:
                print("---------Game Start---------")
                # player's choice
                print("Select your choice from following:")
                print("\tSnake, Water, Gun\n")
                player_choice = str(input("Enter your choice: ")).lower()
                print()
                computer_choice = random_choice()

                # if statement for checking winning conditions
                if player_choice == "snake":
                    if computer_choice == "snake":
                        print("Match draw...!\n")

                    elif computer_choice == "water":
                        print(f"{player_name.capitalize()} won...!\n")
                        player_point = player_point + 1

                    elif computer_choice == "gun":
                        print("Computer won...!\n")
                        computer_point = computer_point + 1

                elif player_choice == "water":
                    if computer_choice == "water":
                        print("Match draw...!\n")

                    elif computer_choice == "snake":
                        print("Computer won...!\n")
                        computer_point = computer_point + 1

                    elif computer_choice == "gun":
                        print(f"{player_name} won...!\n")
                        player_point = player_point + 1

                elif player_choice == "gun":
                    if computer_choice == "gun":
                        print("Match draw...!\n")

                    elif computer_choice == "snake":
                        print(f"{player_name} won...!\n")
                        player_point = player_point + 1

                    elif computer_choice == "water":
                        print("Computer won...!\n")
                        computer_point = computer_point + 1

                else:
                    print("Invalid choice, Please select your choice again\n")

            case 2:
                print("---------Point Table---------")
                print(f"{player_name.capitalize()}\tcomputer")
                print(f"{player_point}\t\t{computer_point} \n")
                if player_point > computer_point:
                    print(f"{player_name.capitalize()} won the game...!")
                elif player_point < computer_point:
                    print("Computer won the game...!")
                else:
                    print("Game draw...!")

            case 3:
                break

            case _:
                print("Invalid selection, Please select again")
                continue
    except:
        print("?...You can not enter string or floating point number...?\n")
