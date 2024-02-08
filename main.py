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
            print('nice')
            break
        elif user_input == 'home' or user_input == 'Home':
            print('nice')
            break
        elif user_input == 'back' or user_input == 'Back':
            print('nice')
            break

#as of now only way to get to list page is from welcome screen so all back needs to do is display home screen again

if __name__ == '__main__':
    welcomePage()
