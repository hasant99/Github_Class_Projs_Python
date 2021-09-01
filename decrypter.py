###Author: Hasan Taleb
###Class: CSc110
###Description: A program that decrypts an
###             encrypted file selected by the user.
###             It first .combines the encrypted file and
###             index files into a list in the order
###             they are read. Then this program reorders
###             the list numerically to decrypt the file
###             and then reassembles the text in the right
###             order and writes that information to a new_lst
###             file called decrypted.txt.

def create_new_list(encrypted_file, index_file):
    '''
    This file uses a for loop to take the
    information from encrypted_file and index_file
    and assemble it into a list. The format of the list
    is a line of the encrypted_file followed by it's
    corresponding index from index_file.
    encrypted_file: The file chosen by the user
    that is already encrypted.
    index_file: The file used as a key that contains
    the indexes corresponding to the out of order lines
    in the encrypted_file.
    '''
    encrypted_lst = []
    text_file = open(encrypted_file, 'r')
    key_file = open(index_file, 'r')
    key_file = key_file.readlines()
    i = 0
    for line in text_file:
        encrypted_lst.append(line.strip('\n'))
        encrypted_lst.append((key_file[i]).strip('\n'))
        i+=1
    return encrypted_lst


def decode_list(encrypted_lst):
    '''
    This function takes the information from
    encrypted_lst and uses a for loop to sort
    the list in ascending numeric order. It then
    removes the numeric value and adds the
    reordered text to new_lst in order to
    decrypt the file.
    encrypted_lst: A list containing each line of the
    encrypted_file followed by it's
    corresponding index from index_file.
    '''
    new_lst= []
    while len(encrypted_lst) > 0:
        minimum = int(encrypted_lst[1])
        for i in range(1, len(encrypted_lst), 2):
            if int(encrypted_lst[i]) < minimum:
                minimum = int(encrypted_lst[i])
        new_lst.append(encrypted_lst[
        (encrypted_lst.index(str(minimum)))-1])
        encrypted_lst.remove(encrypted_lst[
        (encrypted_lst.index(str(minimum)))-1])
        encrypted_lst.remove(str(minimum))
    return new_lst

def write_decrypted_file(decrypted_lst):
    '''
    This function takes the information
    from decrypted_lst and writes it into
    a new file named decrypted.txt.
    decrypted_lst: A list containing the
    lines from the encrypted file sorted
    back into the original order.
    '''
    decrypted_file = open('decrypted.txt', 'w')
    for i in range(0,len(decrypted_lst)):
        line = str(decrypted_lst[i])
        decrypted_file.write(line + '\n')
    decrypted_file.close()

def main():
    #Get the desired file to decrypt from the user
    encrypted_file = input('Enter the name of' +
    ' an encrypted text file:\n')
    #Get the associated index file from the user
    index_file = input('Enter the name of' +
    ' the encryption index file:\n')
    #Run appropriate functions to successfully decrypt file
    create_new_list(encrypted_file, index_file)
    encrypted_lst = create_new_list(encrypted_file, index_file)
    decrypted_lst = decode_list(encrypted_lst)
    write_decrypted_file(decrypted_lst)

main()
