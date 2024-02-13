#CS361 Main Project

def welcomePage():
    '''Display the welcome page'''

    print('Welcome')
    print('This is the Home Page')
    print('''This program contains information on the previous years of the professional surfing circuit known as the WSL.
At this stage of development the program will produce a list of surfers and their rankings from an inputted year.
Type "help" for a detailed list of commands and how to use them.''')
    print()


    user_input = input('To begin please enter a valid year between 2010 and 2023 or enter another command: ')

    valid_years = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']

    for i in valid_years:
        if user_input == i:
            displayList(i)
        elif user_input == 'help' or user_input == 'Help':
            for i in range(3):
                print()
            helpPage()
            break
        elif user_input == 'home' or user_input == 'Home':
            welcomePage()
            break
        elif user_input == 'back' or user_input == 'Back':
            welcomePage()
            break
    else:
        print('Sorry the inputted text was invalid, please try again.')
        welcomePage()


#as of now only way to get to list page is from welcome screen so all back needs to do is display home screen again
def helpPage():
    '''Display the Help page'''

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
    user_input = input('Type "home" to go back to the Home page: ')

    if user_input == 'home':
        for i in range(3):
            print()
        welcomePage()
    elif user_input == 'exit':
        for i in range(3):
            print()
        exit()
    elif user_input == 'back':
        for i in range(3):
            print()
        welcomePage()
    else:
        print('Sorry the inputted text was invalid, please try again.')
        helpPage()

def displayList(year):
    '''Displays a list of surfers'''
    file = open('C:\\List of Surfers\\' + str(year) + '.txt', 'r')
    counter = 0
    for current_line in file:
        if counter == 0:
            current_line.strip()
            print('1: ')
            counter += 1
        else:
            print(current_line.strip())
            counter += 1
        if counter == 2:
            break

    counter = 0
    for current_line in file:
       current_line.strip()
       counter += 1
       if counter == 2:
           break
    rank = 2
    counter = 1
    overall_counter = 0
    for current_line in file:
        #want 1, 2
        if counter == 1:
            print(rank, ': ')
            counter += 1
            overall_counter += 1
            rank += 1
        elif counter == 2:
            print(current_line.strip())
            counter += 1
            overall_counter += 1
        else:
            counter += 1
        if counter == 3 or counter == 4:
            current_line.strip()
        if counter > 4:
            counter = 1


        if overall_counter == 18:
            break

    print()
    user_input = input('Type "home" to go back to the Home page: ')

    if user_input == 'home':
        for i in range(3):
            print()
        welcomePage()
    elif user_input == 'exit':
        for i in range(3):
            print()
        exit()
    elif user_input == 'back':
        for i in range(3):
            print()
        welcomePage()
    else:
        print('Sorry the inputted text was invalid, please try again.')
        helpPage()

if __name__ == '__main__':
    welcomePage()
