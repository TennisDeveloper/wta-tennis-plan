import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('WTA_Tennis_Plan')

def get_hours_of_tennis_training_data():
    """
    Get "number of tennis training hours" input from the user. Input should be a list of hours per each day 
    of the week, separated by commas.
    """
    print("Please enter the number of tennis training hours per week for each day separately.")
    print("Data should be seven numbers, separated by commas.")
    print("Please start from tennis training hours on Saturday  and continue until the next Friday.")
    print("Remember that your goal is to achieve 10 hours of training per week.")
    print("Example: 1, 1.5, 2, 0, 2, 3, 0 \n ")

    data_str_tennis_hours = input("Enter your data here: ")
    print(f"The data provided is: {data_str_tennis_hours}")

def get_hours_of_fitness_training_data():
    """
    Get "number of fitness training hours" input from the user. Input should be a list of hours per each day 
    of the week, separated by commas.
    """
    print("Please enter the number of fitness training hours per week for each day separately.")
    print("Data should be seven numbers, separated by commas.")
    print("Please start from fitness training hours on Saturday and continue until the next Friday.")
    print("Remember that your goal is to achieve 5 hours of fitness training per week.")
    print("Example: 1, 1, 0.5, 0, 1, 0.5, 0 \n ")

    data_str_fitness_hours = input("Enter your data here: ")
    print(f"The data provided is: {data_str_fitness_hours}")

def get_hours_of_sleeping_data():
    """
    Get "number of sleeping hours" input from the user. Input should be a list of hours per each day 
    of the week, separated by commas.
    """
    print("Please enter the number of sleeping hours per week for each day separately.")
    print("Data should be seven numbers, separated by commas.")
    print("Please start from sleeping hours on Saturday and continue until the next Friday.")
    print("Remember that your goal is to achieve 9 hours of sleep per day.")
    print("Example: 8, 9, 8, 6, 5.5, 7, 6.5 \n ")

    data_str_sleeping_hours = input("Enter your data here: ")
    print(f"The data provided is: {data_str_sleeping_hours}")

def get_mental_training_data():
    """
    Get "mental training session" input from the user. Input should be a list of mental training sessions per each day 
    of the week, separated by commas.
    """
    print("Please enter if you had the mental training session during the week. Please input each day separately.")
    print("Your answer should be either Yes or No for each day of the week, separated by commas.")
    print("Please start from mental sessions on Saturday and continue until the next Friday.")
    print("Remember that your goal is to have mental session before your tournament.")
    print("Example: Yes, No, No, No, No, No, No \n ")

    data_str_mental_training = input("Enter your data here: ")
    print(f"The data provided is: {data_str_mental_training}")

def get_nutrition_data():
    """
    Get "nutrition data" input from the user. Input should be a list of nutrition evaluation per each day 
    of the week, separated by comma. The aim is to monitor if the user was eating healthy or he was 
    eating any food containing gluteen, lactose or drinking alcohol.
    """
    print("Please enter your nutrition info of the week. Please input each day separately.")
    print("Your answer should be seven values, either Ok or in case you ate or drank anything containing gluteen, lactose or alcohol, please write either gluteen or lactose or alcohol. Do this for each day of the week, separated by commas.")
    print("Please start from nutrition evaluation on Saturday and continue until next Friday.")
    print("Remember that your goal is not to eat food containing gluteen or lactose or drink alcohol.")
    print("Example: Ok, Ok, gluteen, lactose, alcohol, Ok, Ok \n ")

    data_str_nutrition = input("Enter your data here: ")
    print(f"The data provided is: {data_str_nutrition}")

def get_tournaments_data():
    """
    Get "tournaments data" input from the user. Input should be a list of tournament participations per each day 
    of the week, separated by commas. The aim is to monitor if the user on a given day has participated on a
    tournament or not.
    """
    print("Please enter your tournament participation info of the week. Please input each day separately.")
    print("Your answer should be seven values, either Yes if you played a tournament or No if you didn't.")
    print("Please input your data for each day of the week, separated by commas.")
    print("Please start from Saturday and continue until the next Friday.")
    print("Remember that your goal is to participate at least on two tournaments per month.")
    print("Example: Yes, Yes, No, No, No, No, No \n ")

    data_str_tournaments = input("Enter your data here: ")
    print(f"The data provided is: {data_str_tournaments}")

get_hours_of_tennis_training_data()
get_hours_of_fitness_training_data()
get_hours_of_sleeping_data()
get_mental_training_data()
get_nutrition_data()
get_tournaments_data()






