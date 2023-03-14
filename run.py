"""
Import libraries
"""
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('garden-bar-stock')


def get_initial_stock_data():
    """
    Import initial stock data from worksheet
    """
    initial_stock = SHEET.worksheet("initial stock").get_all_values()


get_initial_stock_data()


def get_entries_data():
    """
    Get the number of bottles for each drink
    introduced in the bar from the user
    """
    print("Please enter the number of bottles "
          "for each drink introduced in the bar.")
    print("Data should be 5 numbers divisible by 6, "
          "separated by commas.")
    print("Example: 12,24,36,48,60\n")

    entries_str = input("Enter the number of bottles here: ")
    entries_data = entries_str.split(",")
    validate_entries(entries_data)


def validate_entries(bottles):
    """
    Convert all string values into integers,
    Raises ValueError if strings cannot be
    converted into integers, if there aren't
    exactly 5 vaues, or if the values entered
    cannot be divided by 6.
    """
    try:
        [int(bottle) for bottle in bottles]
        if len(bottles) != 5:
            raise ValueError(
                f"The user must enter exactly 5 values,"
                f" you provided {len(bottles)}"
            )
    except ValueError as e:
        print(f"Invalid entries: {e}, please try again.\n")



get_entries_data()