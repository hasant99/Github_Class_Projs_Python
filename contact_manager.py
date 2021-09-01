###Author: Hasan Taleb
###Class: CSc110
###Description: A program that creates a contact
###             organizer that loads in a file
###             with existing contacts. It then
###             prompts the user to enter a command.
###             The user can command the program to
###             add a contact, which will prompt
###             them to enter the name, email, and
###             phone number of the contact to add.
###             The program then adds the contact to
###             the organizer. The user can also
###             prompt the program to show contacts
###             with a certain name, email, or, phone
###             number. If the user enters the exit
###             command, the program will save the
###             current conatact list and then exit.

def read_file(file):
    '''
    This function opens the contacts.txt file
    and then puts each line of the file in a tuple.
    It then places all tuples inside a set named
    contact_set and returns this set to the function.
    file: The contacts.txt file.
    '''
    file = open(file, 'r')
    contact_set = set()
    for line in file:
        line = line.strip('\n')
        line = tuple(line.split(' | '))
        contact_set.add(line)
    file.close()
    return contact_set

def get_command():
    '''
    This function prompts the user for a
    command. It then returns a list with the
    user's command line split by the spaces.
    '''
    command = input('>\n')
    return command.split(' ')

def show_contacts(contacts, info):
    '''
    This function first uses a for loop
    to iterate through the rows in the
    contacts parameter and check if the
    info parameter exists in the row. If info
    is in the row, the function adds the row to
    a set named matches. Once the set contains
    all contacts that contain the info parameter,
    the function uses a for loop to iterate through
    a sorted version of matches and then prints each
    contact's information.
    contacts: A set containing tuples taht contain each
    contact's name, number, and email.
    info: This parameter represent's the deisred contact's
    name, number, or email.
    '''
    matches = set()
    for row in contacts:
        if info in row:
            matches.add(row)
    for contact in sorted(matches):
        print(contact[0] + "'s" + ' contact info:\n'\
        + '  email: ' + contact[1] + '\n'\
        + '  phone: ' + contact[2])
    if len(matches) == 0:
        print('None')

def add_contact(contacts, name, email, phone):
    '''
    This function creates a new tuple with
    a contact's name, number, and email. Then
    it checks if that tuple exists in contacts.
    If it doesn't exist, it adds the tuple to
    the contacts set.
    contacts: A set containing tuples taht contain each
    contact's name, number, and email.
    name: The desired contact name the user has input.
    email: The desired contact email the user has input.
    phone: The desired contact phone number the user has input.
    '''
    new_contact = (name, email, phone)
    if new_contact not in contacts:
        contacts.add(new_contact)
        print('Contact added!')
    else:
        print('Contact already exists!')

def save_contents(contact_set, file):
    '''
    This function writes the information from the
    current contact set back to the original contacts.txt
    file in order to save the user's information.
    contact_set: A set containing tuples taht contain each
    contact's name, number, and email.
    file: The contacts.txt file.
    '''
    file = open(file, 'w')
    for row in sorted(contact_set):
        for column in row:
            if column[0].isnumeric():
                file.write(str(column) + '\n')
            else:
                file.write(str(column) + ' | ')

def main():
    file = 'contacts.txt'
    contact_set = read_file(file)
    print('Welcome to the contacts app! ')
    #Create a while loop to continue asking
    #user for a command as long as their command is not
    #'exit'. The loop then uses if statements to execute
    #the appropriate function for the user's command.
    while True:
        command = get_command()
        if command[0] == 'show':
            info_type = command[3]
            if info_type == 'name':
                if len(command) == 6:
                    info = str(command[4]) + ' ' +\
                    str(command[5])
                else:
                    info = command[4]
            else:
                info = command[4]
            show_contacts(contact_set, info)
        elif command[0] == 'add':
            name = input('name:\n')
            email = input('email:\n')
            phone = input('phone:\n')
            add_contact(contact_set, name, email, phone)
        elif command[0] == 'exit':
            save_contents(contact_set, file)
            return print('Goodbye!')
        else:
            print('Huh?')

main()
