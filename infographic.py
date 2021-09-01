###Author: Hasan Taleb
###Class: CSc110
###Description: A program that reads a .txt file
###             and outputs a graphic that displays
###             the total unique words and the most used
###             small, medium, and large words. It also
###             displays the amount of small, medium, and
###             large words, the capitalized and non capitalized
###             words, and the puncuated and non punctuated words
###             each in bar graphs.

from graphics import graphics

def read_and_process(file):
    '''
    This function opens, reads and splits the file
    parameter into individual words. It then places
    the words into the list word_lst and returns the
    list.
    file: A .txt file chosen by the user.
    '''
    word_lst = []
    txt_file = open(file, 'r')
    for line in txt_file:
        line = line.strip('\n')
        words = line.split(' ')
        for word in words:
            if word != '':
                word_lst.append(word)
    return word_lst

def count_words(word_lst):
    '''
    This function places the unique words from
    word_lst into a dictionary and counts how
    many times they appear in the list. The word
    is the key and it's count is the value.
    word_lst: A list containing every word
    from the .txt file.
    '''
    word_counts = {}
    for word in word_lst:
        if word != '':
            if word not in word_counts:
                word_counts[word] = 1
            else:
                word_counts[word] += 1
    return word_counts

def most_occurrences(word_counts):
    '''
    This function iterates through the keys in
    word_counts and uses if statements to classify
    whether a word is small(length 0-4, inclusive),
    medium(length 5-7, inclusive) or
    large( length 8+, inclusive). It then counts
    how many words fall into each category and also
    assigns the most occuring word in each category
    to a variable. These values are then returned
    to the function.
    word_counts: A dictionary containing every
    unique word in the .txt file as a key with the number
    of times the unique word appears as the value.
    '''
    small_count = 0
    medium_count = 0
    large_count = 0
    small_max = 0
    small_word = ''
    medium_max = 0
    medium_word = ''
    large_max = 0
    large_word = ''
    for word in word_counts:
        if len(word) >= 0 and len(word) <= 4:
            small_count +=1
            if word_counts[word] > small_max:
                small_max = word_counts[word]
                small_word = word
        elif len(word) >= 5 and len(word) <= 7:
            medium_count +=1
            if word_counts[word] > medium_max:
                medium_max = word_counts[word]
                medium_word = word
        else:
            large_count +=1
            if word_counts[word] > large_max:
                large_max = word_counts[word]
                large_word = word
    return small_word, small_count, medium_word, medium_count, large_word, large_count


def count_capital(word_counts):
    '''
    This function uses a for loop to iterate
    through the keys in word_counts and assign
    words beginning with a capital letter to
    capital_lst and all other words to lowercase_lst.
    word_counts: A dictionary containing every
    unique word in the .txt file as a key with the number
    of times the unique word appears as the value.
    '''
    capital_lst = []
    lowercase_lst = []
    for word in word_counts:
        if word != '':
            if word[0].isupper():
                capital_lst.append(word)
            else:
                lowercase_lst.append(word)
    return len(capital_lst), len(lowercase_lst)

def count_punctuated(word_counts):
    '''
    This function uses a for loop to iterate
    through the keys in word_counts and assign
    words ending with punctuation to
    punc_lst and all other words to non_punc_lst.
    word_counts: A dictionary containing every
    unique word in the .txt file as a key with the number
    of times the unique word appears as the value.
    '''
    punc_lst = []
    non_punc_lst = []
    for word in word_counts:
        if word != '':
            if word[-1] == '.':
                punc_lst.append(word)
            else:
                non_punc_lst.append(word)
    return len(punc_lst), len(non_punc_lst)



def build_chart(gui, file, word_counts, small_word,
small_count, medium_word, medium_count, large_word,
large_count, word_lst, capitals, lowercases, punc_words,
non_punc_words):
    '''
    This function builds the chart with all the information
    on the .txt file in visual form. It first creates the
    background and prints the header titles. Then it creates
    the graphs and titles that display the remaining
    information.
    gui: A 650 x 700 canvas used to draw graphics on.
    file: A .txt file chosen by the user.
    word_counts: A dictionary containing every
    unique word in the .txt file as a key with the number
    of times the unique word appears as the value.
    small_word: The most occuring word in the .txt file
    with a length 0-4, inclusive.
    small_count: The amount of times small_word appears
    in the .txt file.
    medium_word: The most occuring word in the .txt file
    with a length 5-7, inclusive.
    medium_count: The amount of times medium_word appears
    in the .txt file.
    large_word: The most occuring word in the .txt file
    with a length 8+, inclusive.
    large_count: The amount of times large_word appears
    in the .txt file.
    capitals: A list containing all the capital words
    in the .txt file.
    lowercases: A list containing all the lowercase words
    in the .txt file.
    punc_words: A list containing all the punctuated words
    in the .txt file.
    non_punc_words: A list containing all the non punctuated
    words in the .txt file.
    '''
    #Background and header titles
    gui.rectangle(0, 0, 650, 700, 'gray20')
    gui.text(50, 50, file, 'cyan', 25)
    gui.text(50, 100, 'Total Unique Words: ' + str(len(word_counts)), 'white', 25)
    gui.text(50, 150, 'Most used words (s/m/l): ', 'white', 13)
    gui.text(250, 150, small_word + ' (' + str(word_counts[small_word]) + 'x) '
    + medium_word + ' (' + str(word_counts[medium_word]) + 'x) '
    + large_word + ' (' + str(word_counts[large_word]) + 'x) ', 'cyan', 13)
    #Bar graph titles
    gui.text(50, 180, 'Word lengths', 'cyan', 18)
    gui.text(250, 180, 'Cap/Non-Cap', 'cyan', 18)
    gui.text(450, 180, 'Punct/Non-Punct', 'cyan', 18)
    #Word lengths graph
    gui.rectangle(50, 220, 145, (450/len(word_counts) * small_count), 'deep sky blue')
    gui.text(50, 220, 'small words', 'white', 10)
    gui.rectangle(50, 220 + (450/len(word_counts) * small_count), 145,
    (450/len(word_counts) * medium_count), 'lime green')
    gui.text(50, 220 + (450/len(word_counts) * small_count), 'medium words', 'white', 10)
    gui.rectangle(50, 220 + (450/len(word_counts) * medium_count)
    + (450/len(word_counts) * small_count), 145,
    (450/len(word_counts) * large_count), 'deep sky blue')
    gui.text(50, 220 + (450/len(word_counts) * medium_count)
    + (450/len(word_counts) * small_count), 'large words', 'white', 10)
    #Cap/Non-Cap graph
    gui.rectangle(255, 220, 145, (450/len(word_counts) * capitals), 'deep sky blue')
    gui.text(255, 220, 'Capitalized', 'white', 10)
    gui.rectangle(255, 220 + (450/len(word_counts) * capitals), 145,
    (450/len(word_counts) * lowercases), 'lime green')
    gui.text(255, 220 + (450/len(word_counts) * capitals), 'Non Capitalized', 'white', 10)
    #Punct/Non-Punct graph
    gui.rectangle(450, 220, 145, (450/len(word_counts) * punc_words), 'deep sky blue')
    gui.text(450, 220, 'Punctuated', 'white', 10)
    gui.rectangle(450, 220 + (450/len(word_counts) * punc_words), 145,
    (450/len(word_counts) * non_punc_words), 'lime green')
    gui.text(450, 220 + (450/len(word_counts) * punc_words), 'Non Puncuated', 'white', 10)

def main():
    #Create a canvas and assign it to gui variable
    gui = graphics(650, 700, 'canvas')
    #Get the desired file to analyze
    file = input('Enter the name of a text file:\n')
    #Execute functions
    word_lst = read_and_process(file)
    word_counts = count_words(word_lst)
    small_word, small_count, medium_word, medium_count,\
    large_word, large_count = most_occurrences(word_counts)
    capitals, lowercases = count_capital(word_counts)
    punc_words, non_punc_words = count_punctuated(word_counts)
    build_chart(gui, file, word_counts, small_word,
    small_count, medium_word, medium_count, large_word, large_count, word_lst,
    capitals, lowercases, punc_words, non_punc_words)


main()
