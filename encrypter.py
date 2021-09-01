###Author: Hasan Taleb
###Class: CSc110
###Description: A program that encrypts a file
###             chosen by the user. It scrambles
###             the lines of the selected file
###             and creates and an encrypted
###             copy as well as a file
###             containing a list of indexes that
###             acts as a key used to decrypt the
###             file.

import random

def create_line_list(text_file):
    '''
    This function opens the file chosen
    by the user and then puts each line
    of the file in a list.
    text_file: The .txt file chosen by the user
    '''
    file = open(text_file, 'r')
    file_lines = file.readlines()
    file.close()
    return file_lines

def create_index_list(file_lines):
    '''
    This function creates a list the same
    length as file_lines and assigns numbers
    in ascending order to each index of file_lines.
    file_lines: A list containing each line of the
    .txt file chosen by the user.
    '''
    index_list=[0]*len(file_lines)
    count = 1
    for i in range(0, len(index_list)):
        index_list[i] += count
        count += 1
    return index_list

def encrypt_file(line_lst, index_lst):
    '''
    This function uses a while loop
    line_lst: A list containing each line of the
    .txt file chosen by the user.
    index_lst: A list containing numbers starting with 1
    going in ascending order reaching the same length as
    line_lst.
    '''
    i = 0
    while i < (len(line_lst)*5):
        rand_int_1 = random.randint(0, len(line_lst)-1)
        rand_int_2 = random.randint(0, len(line_lst)-1)
        line_lst[rand_int_1], line_lst[rand_int_2] =\
        line_lst[rand_int_2], line_lst[rand_int_1]
        index_lst[rand_int_1], index_lst[rand_int_2] =\
        index_lst[rand_int_2], index_lst[rand_int_1]
        i+=1
    return line_lst, index_lst

def write_files(line_lst, index_lst):
    '''
    This function writes the information from line_lst
    and index_lst to new files named encrypted.txt and
    index.txt.
    index_lst: A list containing numbers starting with 1
    going in ascending order reaching the same length as
    line_lst.
    '''
    encrypted_file = open('encrypted.txt', 'w')
    for i in range(0,len(line_lst)):
        line = str(line_lst[i])
        encrypted_file.write(line)
    encrypted_file.close()

    index_file = open('index.txt', 'w')
    for i in range(0,len(index_lst)):
        num = str(index_lst[i]) + '\n'
        index_file.write(num)
    index_file.close()

def main():
    #Create a random seed of 125
    random.seed(125)
    #Get the desired file to encrypt from user
    text_file = input('Enter a name of a text file to encrypt:\n')
    #Call functions in appropriate order to encrypt desired file.
    line_lst = create_line_list(text_file)
    index_lst = create_index_list(create_line_list(text_file))
    encrypt_file(line_lst, index_lst)
    write_files(line_lst, index_lst)

main()




