#CS361 Main Project

def welcomePage():
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
            print('nice')
        elif user_input == 'help' or user_input == 'Help':
            for i in range(3):
                print()
            helpPage()
            break
        elif user_input == 'home' or user_input == 'Home':
            print('nice')
            break
        elif user_input == 'back' or user_input == 'Back':
            print('nice')
            break

#as of now only way to get to list page is from welcome screen so all back needs to do is display home screen again
def helpPage():
    print('Help')
    print()
    print('''This is the help screen, below is a list of the basic commands in the program 
and how to use them''')
    print()
    print('Commands: ')
    commands = {'help' : 'Type "help" to display the help screen (this screen).',
                'exit' : 'Type "exit" at any time to exit the program.',
                'back' : 'Type "back" at any time to go back to the previous page you were on.'}

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


if __name__ == '__main__':
    welcomePage()
