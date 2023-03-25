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


"""
Following functions get inputs from the user, which is used further for
evaluation and input to Google sheet WTA Tennis Plan.
"""


def get_hours_of_tennis_training_data():
    """
    Get "number of tennis training hours" input from the user.
    Input should be a list of hours per each day of the week,
    separated by commas. The loop will repeatedly request data
    until it is valid.
    """
    while True:
        print_statements("tennis", "numbers")
        print("Your goal is to achieve 10 hours of training per week.")
        print("Example: 1, 1.5, 2, 0, 2, 3, 0 \n ")

        data_str_tennis_hours = input("Enter your data here: \n")
        hours_of_tennis_training_data = data_str_tennis_hours.split(",")
        if validate_numbers_data(hours_of_tennis_training_data):
            print("Data is valid!")
            break

    return hours_of_tennis_training_data


def get_hours_of_fitness_training_data():
    """
    Get "number of fitness training hours" input from the user.
    Input should be a list of hours per each day of the week,
    separated by commas. The loop will repeatedly request data
    until it is valid.
    """

    while True:
        print_statements("fitness", "numbers")
        print("Your goal is to achieve 5 hours of fitness training per week.")
        print("Example: 1, 1, 0.5, 0, 1, 0.5, 0 \n ")

        data_str_fitness_hours = input("Enter your data here: \n")
        hours_of_fitness_training_data = data_str_fitness_hours.split(",")
        if validate_numbers_data(hours_of_fitness_training_data):
            print("Data is valid!")
            break
    return hours_of_fitness_training_data


def get_hours_of_sleeping_data():
    """
    Get "number of sleeping hours" input from the user.
    Input should be a list of hours per each day of the week,
    separated by commas. The loop will repeatedly request data
    until it is valid.
    """
    while True:
        print_statements("sleeping", "numbers")
        print("Your goal is to achieve 9 hours of sleep per day.")
        print("Example: 8, 9, 8, 6, 5.5, 7, 6.5 \n ")

        data_str_sleeping_hours = input("Enter your data here: \n")
        hours_of_sleeping_data = data_str_sleeping_hours.split(",")
        if validate_numbers_data(hours_of_sleeping_data):
            print("Data is valid!")
            break
    return hours_of_sleeping_data


def get_mental_training_data():
    """
    Get "mental training session" input from the user.
    Input should be a list of mental training sessions per each day
    of the week, separated by commas. The loop will repeatedly
    request data until it is valid.
    """
    while True:
        print_statements("mental", "values")
        print("Your goal is to have mental session before your tournament.")
        print("Your answer should be either 'yes' or 'no'.")
        print("Example: yes, no, no, no, no, no, no \n ")
        data_str_mental_training = input("Enter your data here: \n")
        string_check = data_str_mental_training.replace(" ", "")
        mental_training_data = string_check.split(",")
        if validate_yes_no_data(mental_training_data):
            print("Data is valid!")
            break
    return mental_training_data


def get_nutrition_data():
    """
    Get "nutrition data" input from the user. Input should be
    a list of nutrition evaluation per each day of the week,
    separated by comma. The aim is to monitor if the user was eating
    healthy or he was eating any food containing gluteen, lactose or
    drinking alcohol. The loop will repeatedly request data until it is valid.
    """
    while True:
        print_statements("nutrition", "values")
        print('''Your goal is not to eat food containing gluteen or lactose
        or drink alcohol.''')
        print('''Your input should be 'ok' if you did everything properly.
        In case you ate or drank anything containing gluteen, lactose or
        alcohol, please write either gluteen or lactose or alcohol.''')
        print("Example: ok, ok, gluteen, lactose, alcohol, ok, ok \n ")

        data_str_nutrition = str(input("Enter your data here: \n"))
        string_check = data_str_nutrition.replace(" ", "")
        nutrition_data = string_check.split(",")
        if validate_nutrition_data(nutrition_data):
            print("Data is valid!")
            break
    return nutrition_data


def get_tournaments_data():
    """
    Get "tournaments data" input from the user. Input should be a list
    of tournament participations per each day of the week, separated
    by commas. The aim is to monitor if the user on a given day has
    participated on a tournament or not. The loop will repeatedly
    request data until it is valid.
    """
    while True:
        print_statements("tournaments", "values")
        print("Your goal is to participate on one tournament per week.")
        print('''Your input should be either 'yes' if you played a tournament
        or 'no' if you didn't.''')
        print("Example: yes, yes, no, no, no, no, no \n ")

        data_str_tournaments = input("Enter your data here: \n")
        string_check = data_str_tournaments.replace(" ", "")
        tournaments_data = string_check.split(",")
        if validate_yes_no_data(tournaments_data):
            print("Data is valid!")
            break
    return tournaments_data


"""
Print statement function for the input data functions
"""


def print_statements(training_category, training_type):
    """
    Print statements for the input data functions
    """
    if training_category == "hours":
        line_1 = f'Please enter the number of {training_category} hours \
        per week for each day separately.'
    else:
        line_1 = f'Please enter your {training_category} data \
        information per week for each day separately.'

    line_2 = f'Data should be seven {training_type}, \
    separated by commas.'
    line_3 = f'Please start from {training_type} on Saturday \
    and continue until the next Friday.'
    input_intro_for_user = print(line_1 + " " + line_2 + " " + line_3)
    return input_intro_for_user


"""
Following functions validate the user input.
"""


def validate_numbers_data(values):
    """
    Inside the try converts all string values into floats.
    Raises ValueError if strings cannot be converted into floats, or
    if there aren't exactly 7 values.
    """
    try:
        [float(value) for value in values]
        if len(values) != 7:
            raise ValueError(
                f"7 values are requested, you have provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, input valid data into the terminal.\n")
        return False
    return True


def validate_yes_no_data(values):
    """
    Inside the try validates if the values provided are from the list
    [yes, no]. Raises ValueError if strings have different values than
    the list [yes, no], or if there aren't exactly 7 values.
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
                f"7 values are requested, you have provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, input valid data into the terminal.\n")
        return False
    return True


def validate_nutrition_data(values):
    """
    Inside the try validates if the values provided are from the list
    [ok, gluteen, lactose, alcohol]. Raises ValueError if strings have
    different values than the list [ok, gluteen, lactose, alcohol], or
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
                f"7 values are requested, you have provided {len(values)}"
            )

    except ValueError as e:
        print(f"Invalid data: {e}, input valid data into the terminal.\n")
        return False
    return True


"""
Following update_worksheet function updates the Google Worksheet
WTA Tennis Plan. Function has other inner functions which calculate
the summary values from the input of the user and evaluate the
overall input.
"""


def upd_wsheet(data, sheet, metric, training_type, l_bound, u_bound):
    """
    Update WTA Tennis Plan worksheet with the user input and calculated input
    """
    print(f"Updating {sheet} worksheet...\n")
    worksheet = SHEET.worksheet(sheet).get_all_values()
    last_row_worksheet = worksheet[-1]
    first_cell = int(last_row_worksheet[0]) + 1
    last_cell = summary(data, sheet, metric, training_type, l_bound, u_bound)
    data.append(last_cell)
    data.insert(0, first_cell)

    worksheet_update = SHEET.worksheet(sheet)
    worksheet_update.append_row(data)
    print(f"{sheet} worksheet updated successfully!\n")


def summary(data, sheet, metric, training_type, l_bound, u_bound):
    """
    Calculate sum of user input data
    """
    if metric == "addition":
        param = sum(data)
        ev_training(param, sheet, training_type, 'trained', l_bound, u_bound)
        return param

    elif metric == "average_value":
        param = sum(data) / len(data)
        ev_training(param, sheet, training_type, 'slept', l_bound, u_bound)
        return param
    elif metric == "count_case":
        param = (data.count("gluteen")
                 + data.count("lactose")
                 + data.count("alcohol"))
        ev_training(param, sheet, training_type, 'ate', l_bound, u_bound)
        return param
    elif metric == "count_yes":
        param = data.count("yes")
        if sheet == "TournamentsOverview":
            ev_training(param, sheet, training_type,
                        'played', l_bound, u_bound)
        elif sheet == "MentalTraining":
            ev_training(param, sheet, training_type, 'had mental training for',
                        l_bound, u_bound)
        return param


def ev_training(summary_metric, sheet, training_type, activity, l_bound,
                u_bound):
    """
    Evaluate progress of tennis training of the last week.
    """
    if summary_metric >= l_bound and summary_metric <= u_bound:
        print(f'''Congrats, you have achieved your weekly goal in
              {training_type}!''')
        if (sheet == 'HoursOfTennisTraining' or
           sheet == "HoursOfFitnessTraining" or
           sheet == "MentalTraining"):
            if summary_metric == 1:
                print(f'You {activity} {summary_metric} hour.')
            elif summary_metric != 1:
                print(f'You {activity} {summary_metric} hours.')
        if sheet == "HoursOfSleeping":
            print(f'''You {activity} {round(summary_metric,2)}
                      hours on average.''')
        if sheet == "Nutrition":
            print(f'You {activity} healthy.')
        if sheet == "TournamentsOverview":
            print('''Congrats, you played a tournament this week,
                  hopefully you won!''')
    elif summary_metric > u_bound:
        if sheet == "Nutrition":
            print(f'You {activity} unhealthy.')
        else:
            print('You were to harsh on you this week! Do less next week!')
    else:
        print(f'''You haven't achieved your {training_type}
              goal of the week, do more!''')
        if (sheet == 'HoursOfTennisTraining' or
           sheet == 'HoursOfFitnessTraining' or
           sheet == 'MentalTraining'):
            if summary_metric == 1:
                print(f'You {activity} {summary_metric} hour.')
            elif summary_metric != 1:
                print(f'You {activity} {summary_metric} hours.')
        if sheet == "HoursOfSleeping":
            print(f'''You {activity} {round(summary_metric,2)}
                  hours on average.''')
        if sheet == "Nutrition":
            print(f'You {activity} unhealthy.')
        if sheet == "TournamentsOverview":
            print('''You didn't play a tournament this week,
                  try playing next week!''')


# All program functions
def main():
    """
    Run all program functions.
    """

    training_data_tennis = get_hours_of_tennis_training_data()
    hours_of_tennis_training_data = [float(num)
                                     for num in training_data_tennis]
    update_tennis_worksheet = upd_wsheet(hours_of_tennis_training_data,
                                         'HoursOfTennisTraining',
                                         'addition',
                                         'tennis', 9, 10)
    training_data_fitness = get_hours_of_fitness_training_data()
    hours_of_fitness_training_data = [float(num)
                                      for num in training_data_fitness]
    update_fitness_worksheet = upd_wsheet(hours_of_fitness_training_data,
                                          'HoursOfFitnessTraining',
                                          'addition',
                                          'fitness', 4, 5)
    sleeping_data = get_hours_of_sleeping_data()
    hours_of_sleeping_data = [float(num) for num in sleeping_data]
    update_sleeping_worksheet = upd_wsheet(hours_of_sleeping_data,
                                           'HoursOfSleeping',
                                           'average_value',
                                           'sleeping', 8, 9)
    mental_training_data = get_mental_training_data()
    update_mental_training_worksheet = upd_wsheet(mental_training_data,
                                                  'MentalTraining',
                                                  'count_yes',
                                                  'mental training',
                                                  1, 2)
    nutrition_data = get_nutrition_data()
    update_nutrition_worksheet = upd_wsheet(nutrition_data,
                                            'Nutrition',
                                            'count_case',
                                            'eating', 0, 0)
    tournaments_data = get_tournaments_data()
    update_tournament_worksheet = upd_wsheet(tournaments_data,
                                             'TournamentsOverview',
                                             'count_yes',
                                             'tournaments', 1, 1)


"""
This is the main function from where the program starts.
"""


print('''Welcome to the WTA Tennis Plan automation!
      Let's evaluate your progress to become a
      proffesional tennis player!\n''')
main()
