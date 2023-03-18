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


def get_entries_data():
    """
    Get entries input from the user.
    Running a while loop that should recive
    valide input from the user, the loop
    should be repeted until the input is valid.
    The input should contain a string
    of 5 numbers separated by a commas
    that can be divisible by 6
    """
    # Create a while loop that repets itself until data provided is True.
    while True:
        print("Please enter the number of bottles "
              "for each drink introduced in the bar.")
        print("Data should be 5 numbers divisible by 6, "
              "separated by commas.")
        print("Example: 12,24,36,48,60\n")

        entries_str = input("Enter the number of bottles here: ")

        entries_data = entries_str.split(",")

        if validate_entries(entries_data):
            print("Entries are valid")
            break

    return entries_data


def validate_entries(entries):
    """
    Convert all string values into integers,
    Raises ValueError if strings cannot be
    converted into integers, if there aren't
    exactly 5 values, or if the values entered
    cannot be divided by 6.
    Function return True if the user insert correct values.
    """
    # Convert list of string into integers and raise VallueError
    # if entries are not integers or more or less then 5 numbers.
    try:
        entries = [int(entry) for entry in entries]
        if len(entries) != 5:
            raise ValueError(
                f"The user must enter exactly 5 values,"
                f" you provided {len(entries)}"
            )
    except ValueError as err:
        print(f"Invalid entries: {err}, please try again.\n")
        return False
    # Use modulo operator to check if the integers can
    # be devided by 6.
    for entry in entries:
        if int(entry) % 6 != 0:
            print(f"{int(entry)} is not divisible by 6.\n")
            return False
    return True


def update_worksheet_data(bottles_data, worksheet):
    """
    Collect a list of integers and push it into the worksheet.
    Update the worksheet with the data provided.
    """
    print(f"Update {worksheet} worksheet...\n")
    update_worksheet = SHEET.worksheet(worksheet)
    update_worksheet.append_row(bottles_data)
    print(f"{worksheet} worksheet updated successfully.\n")


def calculate_total_stock(entries_row):
    """
    Add entries to initial stock to get the final
    stock existing in the bar.
    -Initial stock represents the number of bottles
    per each drink that exist in the bar before entries.
    -Entries represents the user input that is
    added to the initial stock to create a bigger stock
    for the current day's sale.
    Function returns the calculate total_stock.
    """
    print("Calculating total stock...")
    # Import last row of initial stock data from worksheet
    initial_stock = SHEET.worksheet("initial_stock").get_all_values()
    initial_stock_row = initial_stock[-1]

    # Adding entries input to initial_stock iterating
    # through both at the same time to calculate total_stock.
    total_stock_bottles = []
    for initial_stock, entries in zip(initial_stock_row, entries_row):
        total_stock = int(initial_stock) + entries
        total_stock_bottles.append(total_stock)

    return total_stock_bottles


def get_sales_data():
    """
    Get sales input from the user.
    Running a while loop that should recive
    valide input from the user, the loop
    should be repeted until the input is valid.
    The input should contain a string
    of 5 numbers separated by a commas.
    Function returns the sales_data.
    """
    # Create a while loop that repets itself until data provided is True.
    while True:
        print("Please enter the current day sales data.")
        print("Data should be 5 numbers, separated by commas.")
        print("Example: 1,2,3,4,5\n")

        sales_str = input("Enter the current day sales data here: ")

        sales_data = sales_str.split(",")

        if validate_sales(sales_data):
            print("Sales data are valid")
            break

    return sales_data


def validate_sales(sales):
    """
    Convert all string values into integers,
    Raises ValueError if strings cannot be
    converted into integers, if there aren't
    exactly 5 values.
    Function return True if the conditions met
    and False if VallueError rise.
    """
    # Convert a list of strings into integers and rise
    # VallueError if user input contain more than 5 numbers.
    try:
        sales = [int(sale) for sale in sales]
        if len(sales) != 5:
            raise ValueError(
                f"The user must enter exactly 5 values,"
                f" you provided {len(sales)}"
            )
    except ValueError as err:
        print(f"Invalid entries: {err}, please try again.\n")
        return False
    return True


def calculate_final_stock(sales_row):
    """
    Substract sales from total stock to get the new
    initial stock for the next selling day.
    """
    print("Calculating final_stock ...")
    # Import the last row of total_stock data from worksheet.
    total_stock = SHEET.worksheet("total_stock").get_all_values()
    total_stock_row = total_stock[-1]

    # Substract sales input from total_stock iterating
    # through both at the same time to calculate total_stock.
    final_stock_bottles = []
    for total_stock, sales in zip(total_stock_row, sales_row):
        final_stock = int(total_stock) - sales
        final_stock_bottles.append(final_stock)

    return final_stock_bottles


def calculate_revenue(sales_row):
    """
    Import drinks_prices from worksheet.
    Calculate revenue multiplying sales with drinks_prices.
    """
    # Import drinks_prices from worksheet
    print("Calculating revenue ...")
    drinks_prices = SHEET.worksheet("drinks_prices").get_all_values()
    drinks_prices_row = drinks_prices[-1]

    # Multiply drinks_prices with sales iterating
    # through both at the same time to calculate revenue.
    revenue_data = []
    for drinks_prices, sales in zip(drinks_prices_row, sales_row):
        revenue = int(drinks_prices) * sales
        revenue_data.append(revenue)

    return revenue_data


def main():
    """
    Function created to hold
    and run all program funtions
    """
    # All program functions are called here.
    entries_data = get_entries_data()
    new_entries_data = [int(entry_data) for entry_data in entries_data]
    update_worksheet_data(new_entries_data, "entries")
    total_stock_data = calculate_total_stock(new_entries_data)
    update_worksheet_data(total_stock_data, "total_stock")
    sales_data = get_sales_data()
    new_sales_data = [int(sale_data) for sale_data in sales_data]
    update_worksheet_data(new_sales_data, "sales")
    final_stock_data = calculate_final_stock(new_sales_data)
    update_worksheet_data(final_stock_data, "final_stock")
    update_worksheet_data(final_stock_data, "initial_stock")
    revenue_data = calculate_revenue(new_sales_data)
    update_worksheet_data(revenue_data, "revenue")


print("Welcome to Garden Bar stock calculation!\n")
main()
