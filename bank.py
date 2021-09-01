###Author: Hasan Taleb
###Class: CSc110
###Description: A program that creates a simple
###             banking system. It creates a certain
###             number of accounts based on the user input
###             and then can recieve several different
###             commands to either display the account
###             amounts, add or subtract from an account,
###             move an amount from one account to another,
###             or simply exit the program.

#Import the os module
import os

def get_command():
    '''
    This function asks the user for a banking
    command and then splits their input at every
    space.
    '''
    command = input('Banking command:\n')
    return command.split(' ')

def exit_program():
    '''
    This function uses the os module to exit
    the program.
    '''
    os._exit(0)

def display_balance(acct_lst):
    '''
    This function uses a for loop to print
    the balance of each account by printing the monetary
    value that is at each index in the account list.
    acct_lst: A list that holds the monetary values of each
    account according to how many accounts the user requested to
    create.
    '''
    for i in range(0, len(acct_lst)):
        print((str(i+1) + ':' + '$' + str(acct_lst[i])), end = '  ')
    print('\n', end = '')

def add_balances(acct_lst, command):
    '''
    This function uses the command parameter to
    determine which account to access and the amount
    to add to that account. It then adds the amount
    to the current value of the account.
    acct_lst: A list that holds the monetary values of each
    account according to how many accounts the user requested to
    create.
    command: A list containing the user's command line which is
    seperated into a command key, an account or accounts,
    and a monetary amount.
    '''
    acct = int(command[1]) - 1
    ammount = float(command[2])
    acct_lst[acct] += ammount

def subtract_balances(acct_lst, command):
    '''
    This function uses the command parameter to
    determine which account to access and the amount
    to subtract from that account. It then subtracts the amount
    from the current value of the account.
    acct_lst: A list that holds the monetary values of each
    account according to how many accounts the user requested to
    create.
    command: A list containing the user's command line which is
    seperated into a command key, an account or accounts,
    and a monetary amount.
    '''
    acct = int(command[1]) - 1
    ammount = float(command[2])
    acct_lst[acct] -= ammount

def move_balances(acct_lst, command):
    '''
    This function uses the command parameter to determine
    which two accounts the user wants to access.
    It then subtracts the desired amount from the first
    account in the command line and adds it to the second.
    acct_lst: A list that holds the monetary values of each
    account according to how many accounts the user requested to
    create.
    command: A list containing the user's command line which is
    seperated into a command key, an account or accounts,
    and a monetary amount.
    '''
    acct_1 = int(command[1]) - 1
    acct_2 = int(command[2]) - 1
    ammount = float(command[3])
    acct_lst[acct_1] -= ammount
    acct_lst[acct_2] += ammount

def main():
    #Get the number of accounts from the user
    accounts = int(input('Number of accounts:\n'))
    #Create a list containing as many starting zeros
    #as the number of accounts
    acct_lst = [0.0] * accounts

    #Create a while loop that will keep asking
    #for commands and will execute the
    #appropriate function based on the command.
    #The loop will only stop if the exit command
    #is typed in.
    while True:
        command = get_command()
        command_type = command[0]
        if command_type == 'display':
            display_balance(acct_lst)
        elif command_type == 'add':
            add_balances(acct_lst, command)
        elif command_type == 'subtract':
            subtract_balances(acct_lst, command)
        elif command_type == 'move':
            move_balances(acct_lst, command)
        else:
            exit_program()



main()
