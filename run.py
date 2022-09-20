import time
import random
from datetime import date, datetime
import gspread
from google.oauth2.service_account import Credentials
from decimal import *
from art import tprint
from beautifultable import BeautifulTable
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
name_list = order_str.col_values(3)[1:]  
topping_list = order_str.col_values(4)[1:]  
pizza_list = order_str.col_values(2)[1:]  
price_list = order_str.col_values(5)[1:]  

"""
Data to be returned to worksheet, with customer order informatio
"""
customer = SHEET.worksheet('order')

"""
Defining the main functions 
"""
def main():
    customer_name()

"""
Using art format to print a Welcome Logo
"""
tprint('Welcome to Loving Pizza', font = 'cybermedium')

   
   
   
   
   
   
   
main()