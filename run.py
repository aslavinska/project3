import random
import gspread
from google.oauth2.service_account import Credentials

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

records = SHEET.worksheet('records')

data = records.get_all_values()
print("Welcome to Rock, Paper, Scissors game. \n")
print("Winnin rules of the game are: \n Paper beats rock \n Rock beats scissors \n Scissors beats paper \n")

def get_user_choice():
    while True:
         print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
        # Take user input
        choice = int(input("Enter your choice:" ))
        while choice > 3 or choice < 1:
            choice = int(input("Enter a valid choice please"))
        if choice == 1:
            name = 'Rock'
        elif choice == 2:
            name = 'Paper'
        else: 
            name = 'Scissors'
        #print user choice 
        print("User choice is \n", name)
def main ():
    """
    Run all program functions
    """
    get_user_choice()



main()