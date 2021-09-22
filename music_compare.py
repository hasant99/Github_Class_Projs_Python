""" File: music_compare.py
    Author: Hasan Taleb
    Purpose: This file uses imported functions
    from utils.py to calculate find the similarity between
    two songs.first it prints the list of all songs in the
    file, then it prints the similarity valuies of all songs,
    and finally prints information about the two most
    similar songs.
"""

from utils import read_file
from utils import get_slices
from utils import compare_sets
from utils import compare_melodies


def print_songlist(songs):
    '''
    This function loops through the tuples in the songs array
    and prints out each index.
    songs: An array containing tuples that have  the id, 
    title information, and melodies of each song in the 
    original data file.
    '''
    print('--- SONG LIST ---')
    for tuple in songs:
        print('id=' +str(tuple[0]) + ' info=' + '"' +str(tuple[1])+'"'\
            + ' notes=' + str(tuple[2]))


def print_comparisons(songs, n):
    '''
    This function uses the compare_melodies function and a for
    loop to retrieve the similarity value for the first song
    compared to every other song in the file. It then prints
    both songs ids and their similarity.
    songs: An array containing tuples that have  the id, 
    title information, and melodies of each song in the 
    original data file.
    n: A user input integer that represents how many chords
    to slice out at a time.
    '''
    print('--- COMPARISONS ---')
    for i in range(1, len(songs)):
        similarity= compare_melodies(songs[0][2], songs[i][2], n)
        print('id_a=' + str(songs[0][0]) + ' id_b=' + str(songs[i][0]) +\
            ' similarity=' + str(similarity))

def get_melodies(m1, m2, n):
    '''
    This function first calls the get_slices
    function on m1 and m2 to get the desired
    array of slices for both melodies. Then it
    loops through the slices, converts the slice arrays
    to tuples, and appends the tuples to set 1 for m1 and 
    set 2 for m2. Then it converts the sets back into
    lists and returns them in sorted form.
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
    melody_1= list(set1)
    melody_2= list(set2)
    return sorted(melody_1), sorted(melody_2)

def print_results(songs, n):
    '''
    This function first calculates the similarity of each pair
    of songs and then appends the similariy along with ids to 
    an array. It thne loops through the tat list and appends the
    similarity values to a new list and finds the max. Then it uses
    nested for loops to find the ids, info, and melodies of the songs
    with the greatest similarity values and places that information
    in new variables. It then calles the get_melodies function to
    get sorted melody sets. Finally it prints all of that information
    in the appropriate layout. 
    songs: An array containing tuples that have  the id, 
    title information, and melodies of each song in the 
    original data file.
    n: A user input integer that represents how many chords
    to slice out at a time.
    '''
    print('--- RESULT ---')
    sim_lst=[]
    for i in range(1, len(songs)):
        similarity= compare_melodies(songs[0][2], songs[i][2], n)
        sim_lst.append([songs[0][0], songs[i][0],similarity])
    find_max=[]
    for sim in sim_lst:
        find_max.append(sim[2])
    largest_sim = max(find_max)
    for lst in sim_lst:
        if largest_sim in lst:
            for tuple in songs:
                if lst[0] in tuple:
                    name1 = tuple[0]
                    info1 = tuple[1]
                    melody1 = tuple[2]
                elif lst[1] in tuple:
                    name2 = tuple[0]
                    info2 = tuple[1]
                    melody2 = tuple[2]
    set1, set2 = get_melodies(melody1, melody2, n)
    print('Most similar songs:')
    print(' ' + str(info1))
    print(' ' + str(info2))
    print()
    print(' ' + 'ids: ' + str(name1))
    print(' ' + 'ids: ' + str(name2))
    print()
    print('Melodies:')
    print(' ' + str(' '.join(melody1)))
    print(' ' + str(' '.join(melody2)))
    print()
    print('Set 1')
    for element in set1:
        print('  ' + str(' '. join(element)))
    print()
    print('Set 2')
    for element in set2:
        print(' ' + str(' '. join(element)))


def main():
    file = input('file:')
    n = int(input('n: '))
    songs = read_file(open(file, 'r'))
    print_songlist(songs)
    print_comparisons(songs, n)
    print_results(songs, n)
    
main()