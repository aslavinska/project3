# Rock, Paper, Scissors

This game is a Rock, Paper, Scissors game. User is playing agains the computer and its designed for intertaiment. The computer selects random option from an array of 3 options. 
At the end of the game the user will be able to see their score vs computer score. The game is designed to be unlimited until the user selects that they do not wish to continue the game.
In the image below you are able to see how the games main page will look on different devices. 

![Responsive](/assets/images/Responsive.jpg)

# How to play

When the game is launched the user will be asked to enter their username. After that the user will be presented with the game rules and choices. Out of 3 choices the user can select 1 - Rock, 2 - Paper or 3 - Scissors. After the user enters the number of their selection the computer will chose a number from 1 to 3 at random, then the result who won and current score will be displayed to the player. 

# Features

- ## Existing Features
When the player exits the game the score with time,date stamp and user name will be uploaded to the google excel sheet on google cloud, [the link to the document](https://docs.google.com/spreadsheets/d/1F5zwRo01onh-AabcT0iuz1QTQHAk1fY6IeQYId1ddes/edit#gid=1680754323)
After this is done the last 3 entries from the table will be displayed to the player before the end of the program and exit from the console. 

# Data Model 

# Testing

 ## Bugs 

 ### Solved bugs
 (IndentationError: unindent does not match any outer indentation level) this error accured during the user choice development in the line of code : choice = int(input("Enter your choice:" ))
 - In order to resolve it following steps were taken:
    alligning the code properly 



## Validator Testing 
- PEP8
    - No errors were returned from PEP8online.com, see the image below:
    ![PEP8](/images/pep8%20validator.jpg.jpg)

## Unfixed Bugs

No unfixed bugs that have been identified. 

# Deployment 

The project was deployed using Code Institute's mock terminal for Heroku.
- Steps for deployment: 
    - Fork or clone this repository
    - Create a new Heroku app
    - Set the buildbacks to Python and NodeJs in that order
    - Link the Heroku app to the repository
    - Click on Deploy 

The live link can be found here - [Rock, Paper, Scissors](https://aslavinska.github.io/).

# Credits

## Content
- The idea for the project has been provided by the Code Institute.  
- The template for the Read.me file has been taked from Code Institute. 
