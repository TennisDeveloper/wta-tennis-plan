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


#Data inputs:
def get_hours_of_tennis_training_data():
    """
    Get "number of tennis training hours" input from the user. Input should be a list of hours per each day 
    of the week, separated by commas.
    """
    while True:
        print("Please enter the number of tennis training hours per week for each day separately.")
        print("Data should be seven numbers, separated by commas.")
        print("Please start from tennis training hours on Saturday  and continue until the next Friday.")
        print("Remember that your goal is to achieve 10 hours of training per week.")
        print("Example: 1, 1.5, 2, 0, 2, 3, 0 \n ")

        data_str_tennis_hours = input("Enter your data here: ")
        hours_of_tennis_training_data = data_str_tennis_hours.split(",")
        
        if validate_numbers_data(hours_of_tennis_training_data):
            print("Data is valid!")
            break
    

def get_hours_of_fitness_training_data():
    """
    Get "number of fitness training hours" input from the user. Input should be a list of hours per each day 
    of the week, separated by commas.
    """

    while True:
        print("\nPlease enter the number of fitness training hours per week for each day separately.")
        print("Data should be seven numbers, separated by commas.")
        print("Please start from fitness training hours on Saturday and continue until the next Friday.")
        print("Remember that your goal is to achieve 5 hours of fitness training per week.")
        print("Example: 1, 1, 0.5, 0, 1, 0.5, 0 \n ")

        data_str_fitness_hours = input("Enter your data here: ")
        hours_of_fitness_training_data = data_str_fitness_hours.split(",")
        validate_numbers_data(hours_of_fitness_training_data)
        if validate_numbers_data(hours_of_fitness_training_data):
            print("Data is valid!")
            break


def get_hours_of_sleeping_data():
    """
    Get "number of sleeping hours" input from the user. Input should be a list of hours per each day 
    of the week, separated by commas.
    """
    while True:
            
        print("\nPlease enter the number of sleeping hours per week for each day separately.")
        print("Data should be seven numbers, separated by commas.")
        print("Please start from sleeping hours on Saturday and continue until the next Friday.")
        print("Remember that your goal is to achieve 9 hours of sleep per day.")
        print("Example: 8, 9, 8, 6, 5.5, 7, 6.5 \n ")

        data_str_sleeping_hours = input("Enter your data here: ")
        hours_of_sleeping_data = data_str_sleeping_hours.split(",")
        
        if validate_numbers_data(hours_of_sleeping_data):
            print("Data is valid!")
            break



def get_mental_training_data():
    """
    Get "mental training session" input from the user. Input should be a list of mental training sessions per each day 
    of the week, separated by commas.
    """
    while True:
        print("\nPlease enter if you had the mental training session during the week. Please input each day separately.")
        print("Your answer should be either 'yes' or 'no' for each day of the week, separated by commas.")
        print("Please start from mental sessions on Saturday and continue until the next Friday.")
        print("Remember that your goal is to have mental session before your tournament.")
        print("Example: yes, no, no, no, no, no, no \n ")
        data_str_mental_training = input("Enter your data here: ")
        data_str_mental_training_wo_spaces = data_str_mental_training.replace(" ", "")
        mental_training_data = data_str_mental_training_wo_spaces.split(",")
        
        if validate_yes_no_data(mental_training_data):
            print("Data is valid!")
            break

def get_nutrition_data():
    """
    Get "nutrition data" input from the user. Input should be a list of nutrition evaluation per each day 
    of the week, separated by comma. The aim is to monitor if the user was eating healthy or he was 
    eating any food containing gluteen, lactose or drinking alcohol.
    """

    while True:
        print("\nPlease enter your nutrition info of the week. Please input each day separately.")
        print("Your answer should be seven values, either 'ok' or in case you ate or drank anything containing gluteen, lactose or alcohol, please write either gluteen or lactose or alcohol. Do this for each day of the week, separated by commas.")
        print("Please start from nutrition evaluation on Saturday and continue until next Friday.")
        print("Remember that your goal is not to eat food containing gluteen or lactose or drink alcohol.")
        print("Example: ok, ok, gluteen, lactose, alcohol, ok, ok \n ")

        data_str_nutrition = str(input("Enter your data here: "))
        data_str_nutrition_wo_spaces = data_str_nutrition.replace(" ","")
        nutrition_data = data_str_nutrition_wo_spaces.split(",")
        
        if validate_nutrition_data(nutrition_data):
            print("Data is valid!")
            break

def get_tournaments_data():
    """
    Get "tournaments data" input from the user. Input should be a list of tournament participations per each day 
    of the week, separated by commas. The aim is to monitor if the user on a given day has participated on a
    tournament or not.
    """

    while True:
        print("\nPlease enter your tournament participation info of the week. Please input each day separately.")
        print("Your answer should be seven values, either 'yes' if you played a tournament or 'no' if you didn't.")
        print("Please input your data for each day of the week, separated by commas.")
        print("Please start from Saturday and continue until the next Friday.")
        print("Remember that your goal is to participate at least on two tournaments per month.")
        print("Example: yes, yes, no, no, no, no, no \n ")

        data_str_tournaments = input("Enter your data here: ")
        data_str_tournaments_wo_spaces = data_str_tournaments.replace(" ","")
        tournaments_data = data_str_tournaments_wo_spaces.split(",")
        
        if validate_yes_no_data(tournaments_data):
            print("Data is valid!")
            break



#Validations of data inputs:
def validate_numbers_data(values):
    """
    Inside the try converts all string values into floats. 
    Raises ValueError if strings cannot be converted into floats, or
    if there aren't exactly 7 values.
    """
    try: 
        [float(value)  for value in values]
        if len(values) != 7:
            raise ValueError(
                f"Exactly 7 values are requested, you have provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please input valid data into the terminal.\n")
        return False
    
    return True

def validate_yes_no_data(values):
    """
    Inside the try validates if the values provided are from the list [yes, no]. 
    Raises ValueError if strings have different values than the list [yes, no], or
    if there aren't exactly 7 values.
    """
    try: 

        valid_values = ['yes', 'no']

        if all(elem in valid_values for elem in values):
            print("The input string contains only valid values.")
        else:
            raise ValueError(
                f"The input string contains invalid value: {values}"
            )
         

        if len(values) != 7:
            raise ValueError(
                f"Exactly 7 values are requested, you have provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please input valid data into the terminal.\n")
        return False
    
    return True

def validate_nutrition_data(values):
    """
    Inside the try validates if the values provided are from the list [ok, gluteen, lactose, alcohol]. 
    Raises ValueError if strings have different values than the list [ok, gluteen, lactose, alcohol], or
    if there aren't exactly 7 values.
    """
    try: 

        valid_values = ['ok', 'gluteen', 'lactose', 'alcohol']

        if all(elem in valid_values for elem in values):
            print("The input string contains only valid values.")
        else:
            raise ValueError(
                f"The input string contains invalid value: {values}"
            )
           

        if len(values) != 7:
            raise ValueError(
                f"Exactly 7 values are requested, you have provided {len(values)}"
            )
        
    except ValueError as e:
        print(f"Invalid data: {e}, please input valid data into the terminal.\n")
        return False
    
    return True



#get_hours_of_tennis_training_data()
#get_hours_of_fitness_training_data()
#get_hours_of_sleeping_data()
#get_mental_training_data()
#get_nutrition_data()
get_tournaments_data()






