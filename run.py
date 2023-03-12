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
    print(initial_stock)


print(get_initial_stock_data())

