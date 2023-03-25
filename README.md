### Welcome WTA Tennis Plan Users,

This console is a weekly plan for professional women tennis players. In order that
tennis players will succeed, they need to optimize their tennis training, sleeping,
fitness, nutrition, mental training and of course they need to play tournaments!

The idea here is that after the week is over, tennis player will come to this 
console and inputs all those categories of data per each day separately.

Afterwards tha data will be validated and evaluated if the training in all areas
succeeded. The player will get printed messages to the terminal about how she performed
over the last week. Please note, all inputs start from Saturday and continue until
next Friday. 
This is done only for practical reasons. Player usually plays tournaments 
over the weekend and he cannot predict how many hours she will play on the court. 
Usually, if she wins he continues further. So only at the end of the tournament
she knows, how many hours she played. One of the criteria is not to play more
than 10 hours per week on court. Therefore she can better plan the week of trainings
after the tournament is over.


## Feautures
1. Taking User Input Data Per Each Day of the Week

The player will input following data:
    - number of tennis training hours
    - number of fitness training hours
    - number of sleeping hours
    - nutrition overview
    - tournaments participation
    - mental training sesions

 ![menu_bar, the navigation menu image](/assets/images/menu_bar.png)
 Input picture

2. Input Data Validations

Following validations are performed:
* For number of tennis, fitness and sleeping hours, input has to be a number and
    must have seven values for each day of the week. Otherwise the player is prompted
    to input the numbers again.
* For mental training data or tournaments data, user inputs either "yes" or "no.
    Therefore input is validated against these options. No other options are allowed
    Again seven values are expected.
* For nutrition data user has another list of valid values. Here the idea is to
    check if the player optimizes the nutrition process, meaning player has to avoid
    gluten, lactose, and alcohol. Therefore only those values as ['ok', 'gluten'
    'lactose',' alcohol'] are permitted to input.

![menu_bar, the navigation menu image](/assets/images/menu_bar.png)
 Validations picture

2. Data Transformation

The following transformations are performed:
* Latest data of trainings, nutrition, tournaments.. is accessed via Python
* Number of the current week is calculated.
* Based on data type either sum, average or count is used to calculate the data aggregation for the whole week.

3. Google Sheet WTA Tennis Plan Update

Final list of data for each category is saved and sent to Google Sheets.

![google_sheets, the WTA Tennis Plan Google Sheets image](/assets/images/google_sheets.png)
 Google Sheet picture

4. Evaluation of Player Input

User input is evaluated based on the criteria.

![menu_bar, the navigation menu image](/assets/images/menu_bar.png)
 Picture of the evaluation

## Data Model
In principle the data model is similar for each process. User is prompted to enter
the data, data is validated, transformed, Google Sheet is updated and user seens
the evaluation of his input. Please find the Data Model Flowchart below:


![wta_tennis_plan_flowchart, the data model image](/assets/images/wta_tennis_plan_flowchart.jpeg)

## Testing

I have manually tested the project as following:
* Via Python Console, intentionally putting wrong input to check if error message appears
* Via Heroku
* I have passed the code via PEP8 linter and confirmed that there are no issues

## Bugs

There are no outstanding bugs. I have solved all of them during the implementation.

## Deployment
This project was deployed using Code Institute's mock terminal for Heroku.

Steps for Deployment:
* Fork or clone this depository
* Create a new heroku app
* Set the buildbacks to Python and NodeJS in that order
* Link the heroku app to that repository
* Click on Deploy

## Credits

Code Institute for deployment terminal.
Code Institute for inspiration in the Love Sandwiches project
Stack Overflow and https://chat.openai.com/chat for coding inspirations. Mainly
validations, loop & if statements.