""" File: utils.py
    Author: Hasan Taleb
    Purpose: This program contains a series of 
    functions that will be used in music_compare.py.
    These functions perform the various steps necessary
    to compare the similarity of songs in a .txt file.
"""

from os import read

def read_file(fobj):
    '''
    This function loops through the lines in fobj
    and determines whether the line starts with an @
    symbol. If it does, it collects the songs information into
    an array. If not, it collects the chord information into
    an array and then appends both song info and chord info
    into a tuple that gets added to a multidimensional array 
    and returns that array to the function.
    fobj: An opened file object that is originally
    a file name input by the user.
    '''
    song_lst = []
    info=[]
    chord_lst=[]
    for line in fobj:
        line = line.split()
        if line != []:
            if line[0] == '@':
                num = int(line[1])
                for i in range(2, len(line)):
                    info.append(line[i])
            else:
                for i in range(len(line)):
                    chord_lst.append(line[i])
                temp_tuple=(num, ' '.join(info), chord_lst)
                song_lst.append(temp_tuple)
                info=[]
                chord_lst=[]
    return(song_lst)

def get_slices(data, n):
    '''
    This function uses n and a while loop to slice out
    out n caracters at a time, and append that slice to a
    multidimensional array.
    data: Represents an array containing all of the 
    individual chords in a given song
    n: A user input integer that represents how many chords
    to slice out at a time.
    '''
    slice_lst = []
    i = 0
    while i < (len(data)-(n-1)):
        slice_lst.append(data[i:i+n])
        i+=1
    return(slice_lst)

def compare_sets(a, b):
    '''
    This function first finds the intersection of
    set a and set b. Then it finds the union of set a
    and set b. Finally, it applies the jaccard index
    formula to these values to calulate the similarity.
    a: An orginal set
    b: A second set to compare to a
    '''
    intersection = len(a.intersection(b))
    union = len(a.union(b))
    return(intersection/union)

def compare_melodies(m1, m2, n):
    '''
    This function first calls the get_slices
    function on m1 and m2 to get the desired
    array of slices for both melodies. Then it
    loops through the slices, converts the alice arrays
    to tuples, and appends the tuples to set 1 for m1 and 
    set 2 for m2. Finally it calls the comapre_sets
    function to find the jaccard index for m1 and m2.
    m1: The first melody
    m2: The second melody used to comapre to m1
    n: A user input integer that represents how many chords
    to slice out at a time.
    '''
    set1=set()
    set2=set()
    slice1= get_slices(m1, n)
    slice2= get_slices(m2, n)
    for slice in slice1:
        converted= tuple(slice)
        set1.add(converted)
    for slice in slice2:
        converted= tuple(slice)
        set2.add(converted)
    similarity= compare_sets(set1, set2)
    return(similarity)
