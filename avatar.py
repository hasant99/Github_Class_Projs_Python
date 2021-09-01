###Author: Hasan Taleb
###Class: CSc110
###Description: A program that can either print out a pre-made
###             avatar or can create a custom avatar based on
###             various user inputs

# Premade or custom function
def premade_or_custom():
    '''This function asks the user to
        input what kind of avatar they want
        to create and then returns their answer
        to the function.'''
    print('----- AVATAR -----')
    avatar_type = input('Select an Avatar or create your own:\n')
    while avatar_type != 'Chris' and avatar_type != 'Jane' \
        and avatar_type != 'Jeff' and avatar_type != 'exit'\
        and avatar_type != 'custom':
        avatar_type = input('Select an Avatar or create your own:\n')
    return avatar_type
# Hat function
def hat_type(direction):
    '''This function will print out
        a certain kind of hat based on
        the direction variable which
        should be a string.'''
    if direction == 'left':
        print('       ~-~')
        print('     /-~-~-\\')
        print(' ___/_______\\')
    elif direction == 'right':
        print('       ~-~')
        print('     /-~-~-\\')
        print('    /_______\___')
    elif direction == 'both':
        print('       ~-~')
        print('     /-~-~-\\')
        print(' ___/_______\___')
    else:
        print('       ~-~')
        print('     /-~-~-\\')
        print('    /_______\\')
# Face function
def face_type(hair_length, eye_char):
    '''This function prints out either a
        face with long hair or short hair based
        on whether the hair_length variable is
        true or not and also assigns a character
        to represent the eyes beased on the variable
        eye_char. Both variables should be strings.'''
    if hair_length == 'True':
        print('   "|"""""""|"')
        print('   "| ' + eye_char + '   ' + eye_char + ' |"')
        print('   "|   V   |"')
        print('   "|  ~~~  |"')
        print('   " \_____/ "')
    else:
        print("    |'''''''| ")
        print('    | ' + eye_char + '   ' + eye_char + ' |')
        print('    |   V   | ')
        print('    |  ~~~  | ')
        print('     \_____/  ')
#Arms function
def arms_type(arm_style):
    '''This function prints out the avatar's
        arms and uses the variable arm_style
        to determine a character to print the
        arms with.'''
    print(' 0', end = '')
    i = 0
    while i < 4:
        print(arm_style, end = '')
        i += 1
    print('|---|', end = '')
    i = 0
    while i < 4:
        print(arm_style, end = '')
        i += 1
    print('0')
#Torso function
def torso(torso_length):
    '''This function contains a loop
        that prints out as many sections
        of the torso as the variable
        torso_length is equal to.'''
    i = 0
    while i < torso_length:
        print('      |-X-|\n', end = '')
        i += 1
#Leg function
def leg(leg_length, shoe_look):
    '''This function prints out both
        the avatar's legs and shoes
        using a series of if statements
        that will print out a height
        for the legs according to the
        variable leg_length. It also
        uses the variable shoe_look
        to print out that string as
        the avatar's shoes.'''
    print('      HHHHH')
    if leg_length == 1:
        print('     /// \\\\\\')
    if leg_length == 2:
        print('     /// \\\\\\')
        print('    ///   \\\\\\')
    if leg_length == 3:
        print('     /// \\\\\\')
        print('    ///   \\\\\\')
        print('   ///     \\\\\\')
    if leg_length == 4:
        print('     /// \\\\\\')
        print('    ///   \\\\\\')
        print('   ///     \\\\\\')
        print('  ///       \\\\\\')
    print(shoe_look + '       ' + shoe_look)
#Main function
def main():
    '''First the main function determines
        if the user has input the name of
        a premade avatar and will print that
        avatar if they have. If the user inputs
        the string custom then it will ask the
        user for a series of inputs and will
        then assign these inputs to the functions
        representing the different avatar body
        parts to print out a custom avatar.'''
    avatar_type = premade_or_custom()
    if avatar_type == 'Jeff':
        print()
        hat_type('both')
        face_type('False', '0')
        torso(1)
        arms_type('=')
        torso(4)
        leg(2, '#HHH#')
    elif avatar_type == 'Jane':
        print()
        hat_type('right')
        face_type('True', '*')
        arms_type('T')
        torso(2)
        leg(3, '<|||>')
    elif avatar_type == 'Chris':
        print()
        hat_type('front')
        face_type('False', 'U')
        torso(1)
        arms_type('W')
        torso(2)
        leg(4, '<>-<>')
    elif avatar_type == 'custom':
        print('Answer the following questions to create a custom avatar')
        hat_style = input('Hat style ?\n')
        if hat_style != 'left' and hat_style != 'right' and hat_style != 'both':
            hat_style = 'front'
        eye_char = input('Character for eyes ?\n')
        long_hair = input('Long hair (True/False) ?\n')
        arm_style = input('Arm style ?\n')
        torso_length = int(input('Torso length ?\n'))
        leg_length = int(input('Leg length (1-4) ?\n'))
        shoe_look = input('Shoe look ?\n')
        print()
        hat_type(hat_style)
        face_type(long_hair, eye_char)
        arms_type(arm_style)
        torso(torso_length)
        leg(leg_length, shoe_look)
    else:
        print(end = '')


main()








