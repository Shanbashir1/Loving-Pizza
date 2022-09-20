import time
import random
from datetime import date, datetime
import gspread
from google.oauth2.service_account import Credentials
from decimal import *
from art import tprint
from prettytable import PrettyTable
from colorama import Fore, Style

"""
API's worksheets  - Python code linked to google worksheet
The data will collect the Pizza type, sizes, name and any additional toppings. 
The information will also return customer order details, once a reciept has been created. 
"""

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_pizza')

order_str = SHEET.worksheet('order_list')
data = order_str.get_all_values()
type_list = order_str.col_values(1)[1:]  
size_list = order_str.col_values(3)[1:]  
topping_list = order_str.col_values(4)[1:]  
pizza_list = order_str.col_values(2)[1:]  
price_list = order_str.col_values(5)[1:]  

"""
Data to be returned to worksheet, with customer order informatio
"""
customer = SHEET.worksheet('order')
# Defined variables 
customer_details = []
prices = []

"""
Defining the main functions 
"""
def main():
    customer_name()
    size_names()
    pizza_size()

"""
Using art format to print a Welcome Logo
"""
tprint('Welcome to Loving Pizza', font = 'cybermedium')

"""
Customer to enter his name and then be prompted by a Welcome message
The Customer name will be logged into the worksheet (later in the programme)
The customer will enter his first name
"""
def customer_name():
    while True:
        try:
            customer_name.first = input(Fore.BLUE + "\nWelcome to Loving Pizza! Please enter your \
First Name: " + Style.RESET_ALL).capitalize()
            if not customer_name.first.isalpha():
                print(Fore.RED + f"{customer_name.first } is not a valid name. Please enter \
a valid name" + Style.RESET_ALL)
            if len(customer_name.first) <= 2 or len(customer_name.first) > 12:
                print(Fore.RED + f"OOPS, Your name should consist of more than 2 characters. Please Try again." + Style.RESET_ALL)
                continue
            customer_name.surname = input(Fore.BLUE + "\nPlease enter your \
Surname: " + Style.RESET_ALL).capitalize()
            if not customer_name.first.isalpha():
                print(Fore.RED + f"{customer_name.first } is not a valid name. Please enter \
a valid name" + Style.RESET_ALL)
            elif len(customer_name.surname) <= 2 or len(customer_name.surname) > 12:
                print(Fore.RED + f"OOPS, Your name should consist of more than 2 characters. Please Try again."  + Style.RESET_ALL)
                continue
            else:
                customer_details.append(customer_name.first)
                customer_details.append(customer_name.surname)
            
        except IndexError:
            print(f"\nWelcome to Loving Pizza {customer_name.first}, {customer_name.surname} ")
        break
    return customer_name.first, customer_name.surname

"""
Options for the user to select the size of pizza they require
The Price is listed and displayed for the user 
"""

def size_names():
    """
    Creates a prettytable for user to select pizza sizes and records data on to worksheet
    """
    print("\nPlease Select the Pizza Size you require?")
    time.sleep(1)  
    size_name = []
    for siz_name in size_list:
        size_name.append(siz_name)
    num = []
    for i in range(1, 5):
        num.append(i)

    size_names.names = dict(zip(num, size_name))

    size_table = PrettyTable()
    size_table.field_names = num
    size_table.add_row(size_name)
    print(size_table)
    return size_name
"""
Prompts user to select options from previous function relating to pizza size. 
The user is then displayed with their choice
"""
def pizza_size():
    while True:
        pizza_size.piz = input(Fore.BLUE + "\nPlease select the size of the Pizza you require? \
1) Small 2) Medium 3) Large 4) Xlarge \n" + Style.RESET_ALL).lower()
        if pizza_size.piz == "1":
            customer_details.append("Small")
            print("\nYou selected SMALL, approx 3-4 slices\n")
            prices.append(7.50)
            break
        elif pizza_size.piz == "2":
            customer_details.append("Medium")
            print("\nYou selected MEDIUM, approx 5-6 slices")
            prices.append(8.50)
            break
        elif pizza_size.piz == "3":
            customer_details.append("Large")
            print("\nYou selected LARGE, approx 7-8 slices")
            prices.append(12.50)
            break
        elif pizza_size.piz == "4":
            customer_details.append("XLarge")
            print("\nYou selected XLARGE, approx 9-10 slices")
            prices.append(15.50)
            break
        else:
            print(Fore.RED + "Please type 1, 2, 3 or 4" + Style.RESET_ALL)
            continue
        return pizza_size
   
main()