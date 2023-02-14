
import gspread
from google.oauth2.service_account import Credentials
import random
import calendar
import time
from datetime import datetime

# The SCOPE lists the APIs that the program should access in order to run.
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('project3')


def get_user_choice():
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
    # Take user input
    # user_choice = int(input("Enter a your choice here: "))
    user_input = input("Enter a your choice here: ")

    try:
        user_choice = int(user_input)
        while user_choice > 3 or user_choice < 1:
            user_choice = int(input("Enter a valid choice please: "))
        if user_choice == 1:
            user_choice_name = 'Rock'
        elif user_choice == 2:
            user_choice_name = 'Paper'
        else:
            user_choice_name = 'Scissors'
        print("User choice is ", user_choice_name)
        return user_choice
    except ValueError as e:
        print(f"Invalid data: {e}, please try again\n")
        return get_user_choice()


def get_computer_choice():
    print('Now it is the Computers turn....')
    computer_choice = random.randint(1, 3)

    # initialize value of computer_choice_name
    # variable corresponding to the choice value
    if computer_choice == 1:
        computer_choice_name = 'Rock'
    elif computer_choice == 2:
        computer_choice_name = 'Paper'
    else:
        computer_choice_name = 'Scissors'

    print("Computer choice is ", computer_choice_name)
    return computer_choice


def condition_check():
    user_selection = int(get_user_choice())
    computer_selection = int(get_computer_choice())

    playerwon = False
    draw = False

    # check draw
    if user_selection == computer_selection:
        print("It is a Draw \n", end="")
        draw = True
    # condition for winning
    elif (user_selection == 2 and computer_selection == 1):
        print("Player won, paper wins => \n", end="")
        playerwon = True

    elif (user_selection == 1 and computer_selection == 2):
        print("Computer won, paper wins => \n", end="")

    elif (user_selection == 1 and computer_selection == 3):
        print("Player won, Rock wins=>\n", end="")
        playerwon = True

    elif (user_selection == 3 and computer_selection == 1):
        print("Computer won, Rock wins=>\n", end="")

    elif (user_selection == 2 and computer_selection == 3):
        print("Player won, scissors win => \n", end="")
        playerwon = True

    elif (user_selection == 3 and computer_selection == 2):
        print("Computer won, scissors win => \n", end="")

    return playerwon, draw


def update_worksheet(data):
    """
    Update the specified worksheet,
    adding a new row with the list data provided.
    """
    print("Updating worksheet...\n")
    records_worksheet = SHEET.worksheet("records")

    # adds new row to the end of the current data
    records_worksheet.append_row(data)
    print("worksheet updated successfully\n")


def get_last_3_entires():
    """
    Collect columns of data from the worksheet.
    Get the top 3 highest scores of the players.
    """

    records = SHEET.worksheet("records")

    player_res_col = records.col_values(4)

    for i in range(1, len(player_res_col)):
        player_res_col[i] = int(player_res_col[i])
    print(player_res_col)


def main():
    """
    Run all program functions
    """
    records = SHEET.worksheet('records')

    data = records.get_all_values()
    print("Welcome to Rock, Paper, Scissors game. \n")
    print("Winnin rules of the game are: \n")
    print("Paper beats rock \nRock beats scissors \nScissors beats paper \n")
    player_name = input("Enter your players name: \n")
    userscore = 0
    computerscore = 0
    while True:

        playerwon, draw = condition_check()
        print("playerwon", playerwon)
        print("draw", draw)
        if (playerwon):
            userscore = userscore + 1
        elif (draw):
            print("Its a draw")
        else:
            computerscore = computerscore + 1
        print("Player score", userscore)
        print("Computer score", computerscore)
        print("Do you want to play again? (Y/N)")

        ans = input().lower()
        if ans == 'n':
            break

    print("thanks for playing")
    current_GMT = time.gmtime()
    time_stamp = calendar.timegm(current_GMT)
    date_time = datetime.fromtimestamp(time_stamp)
    str_time = date_time.strftime("%I%p %M:%S")
    str_date = date_time.strftime("%d-%b-%Y")
    data = [str_date, str_time, player_name, userscore, computerscore]
    update_worksheet(data)
    records = SHEET.worksheet("records")
    player_names_col = records.col_values(3)
    rownum = player_names_col.index(player_name)+1
    row = records.row_values(rownum)
    print("Your last game result:")
    print(data)
    print("Your first game result:")
    print(row)


main()
