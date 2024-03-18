#CS361 Main Project
from tkinter import *
import tkinter as tk
import wikipedia
import time
import requests
import subprocess
from IPython.display import Image, display
import os
backButton = "welcome"

def welcomePage():
    '''Display the welcome page'''
    global backButton
    print('Welcome')
    print('This is the Home Page')
    print('''This program contains information on the previous years of the professional surfing circuit known as the WSL.
At this stage of development the program will produce a list of surfers and their rankings from an inputted year.
Type "help" for a detailed list of commands and how to use them.''')
    print()

    with open('C:\\CS361 Final\\moreInfo.txt', 'r+') as file:
        file.truncate(0)
        file.close()

    user_input = input('To begin please enter a valid year between 2010 and 2023 or enter another command: ')

    valid_years = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']

    #checks user input against valid years and other valid commands

    if user_input == 'help' or user_input == 'Help':
        for i in range(3):
            print()
        backButton = "welcome"
        helpPage()
    elif user_input == 'exit':
        for i in range(3):
            print()
        exit()
    elif user_input == 'home' or user_input == 'Home':
        backButton = "welcome"
        welcomePage()
    elif user_input == 'back' and backButton == 'welcome':
        backButton = "welcome"
        welcomePage()
    elif user_input == 'back' and backButton == 'help':
        backButton = "welcome"
        helpPage()
    elif user_input == 'back' and backButton == 'list':
        backButton = "welcome"
        backToList()
    else:
        input_flag = False                  #checking if a year was inputted
        for i in valid_years:
            if user_input == i:
                displayList(i)
                input_flag = True
        if input_flag == False:             #if not a year must be invalid
            print('Sorry the inputted text was invalid, please try again.')
            welcomePage()

def helpPage():
    '''Display the Help page'''
    global backButton
    print('Help')
    print()
    print('''This is the help screen, below is a list of the basic commands in the program 
and how to use them''')
    print()
    print('Commands: ')
    commands = {'help' : 'Type "help" to display the help screen (this screen).',
                'exit' : 'Type "exit" at any time to exit the program.',
                'back' : 'Type "back" at any time to go back to the previous page you were on.',
                'home' : 'Type "home" at any time to go back to the home screen'}

    #displays the dictionary of commands
    i = 1
    for command, definition in commands.items():
        print(f"{i}. {command}: {definition}")
        i += 1

    print('Step by step guide on how to use the program: ')
    print('''Start at the home screen (type "home") and at the bottom of the page, a prompt will appear.
The prompt will say "To begin please enter a valid year between 2010 and 2023 or enter another command: "
To generate a list of the surfers of a given year, you type in the desired year and click enter.
This will take you to a new page with the generated list.''')
    print()
    print('Contact Information: ')
    print('Developer: eddyw@oregonstate.edu')
    print()

    #input and navigation for valid commands
    user_input = input('Type "home" to go back to the Home page: ')

    if user_input == 'home':
        for i in range(3):
            print()
        backButton = 'help'
        welcomePage()
    elif user_input == 'exit':
        for i in range(3):
            print()
        exit()
    elif user_input == 'back' and backButton == 'welcome':
        backButton = 'help'
        welcomePage()
    elif user_input == 'back' and backButton == 'help':
        backButton = 'help'
        helpPage()
    elif user_input == 'back' and backButton == 'list':
        backButton = 'help'
        backToList()
        displayList()
    else:
        print('Sorry the inputted text was invalid, please try again.')
        backButton = 'help'
        helpPage()

def displayList(year):
    '''Displays a list of surfers'''
    global backButton
    surfer_list = []                #used for getting in depth information on a surfer
    #opens file containing list of surfers and prints the top 10
    file = open('C:\\CS361 Final\\List of Surfers\\' + str(year) + '.txt', 'r')
    counter = 0                                 #Counter keeps track of how many surfers have been displayed
    for current_line in file:
        #special case for the first surfer
        if counter == 0:
            current_line.strip()
            print('1: ')
            counter += 1
        else:
            surfer_list.append(current_line.strip())
            print(current_line.strip())
            counter += 1
        if counter == 2:
            break

    #setting up the file to be read
    counter = 0
    for current_line in file:
       current_line.strip()
       counter += 1
       if counter == 2:
           break
    #beginning the printing process of ranks 2 and up
    rank = 2
    counter = 1                     #responsible for keeping format to be read
    overall_counter = 0             #responsible for the printing and location of names
    for current_line in file:
        #prints the rank
        if counter == 1:
            print(rank, ': ')
            counter += 1
            overall_counter += 1
            rank += 1
        #prints the surfer
        elif counter == 2:
            surfer_list.append(current_line.strip())
            print(current_line.strip())
            counter += 1
            overall_counter += 1
        #formatting, skips over points and country of origin
        else:
            counter += 1
        if counter == 3 or counter == 4:
            current_line.strip()
        if counter > 4:
            counter = 1


        if overall_counter == 18:
            break



    print()
    #checks for valid commands
    user_input = input('Type "home" to go back to the Home page or a name to get more information: ')

    #checking for name input

    if user_input == 'home':
        for i in range(3):
            print()
        backButton = 'list'
        welcomePage()
    elif user_input == 'exit':
        for i in range(3):
            print()
        exit()
    elif user_input == 'back':
        for i in range(3):
            print()
        backButton = 'list'
        welcomePage()
    elif user_input == 'help':
        backButton = 'list'
        helpPage()

    else:
        name = False                            #name flag used to determine if a name is used
        for i in range(len(surfer_list)):
            if user_input == surfer_list[i]:
                name = True
                moreInfo(surfer_list[i])
        if name == False:
            print('Sorry the inputted text was invalid, please try again. ITS HEREEE')
            backButton = 'list'
            helpPage()

def backToList():
    '''
    Function is responsible for keeping the program running
    when the back button is used and the previous page displays
    the list of surfers.
    '''
    print()
    print()
    year = input('Please enter the year again: ')
    displayList(year)

def moreInfo(name):
    with open('C:\\CS361 Final\\moreInfo.txt', 'w') as file:
        file.write(name + " surfer")
        file.close()
    subprocess.run(['python', 'C:\\CS361 Final\\Final Folder\\microservice\\main-microservice.py'])
    #with open('C:\\CS361 Final\\Final Folder\\microservice\\main-microservice.py', 'r') as file:
        #exec(file.read())
    time.sleep(5)
    displayInfo()
def displayInfo():
    time.sleep(4)
    with open('C:\\CS361 Final\\moreInfo.txt', 'r') as file:
        print(file.read())

    backToHome = input('Type "home" to go back to the home page: ')
    if backToHome == 'home':
        welcomePage()
    elif backToHome == 'exit':
        exit()

    while backToHome != 'home' or 'exit':
        backToHome = input('Type "home" to go back to the home page: ')
        if backToHome == 'home':
            welcomePage()
        elif backToHome == 'exit':
            exit()
        else:
            print('please type a valid command: ')



if __name__ == '__main__':
    welcomePage()