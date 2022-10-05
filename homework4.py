# homework2

def create_dicts(min_count, max_count) -> list:
    import random
    import string

    # create a list of random number of dicts (from 2 to 10)
    number_of_dict = random.randint(min_count, max_count)  # randomly choose number of dicts in a list
    ls_of_dicts = []  # empty list
    cnt_in_ls = 0  # count for dict in the list
    while cnt_in_ls < number_of_dict:  #
        number_of_keys = random.randint(min_count, max_count)  # randomly choose number of key,value pairs in dict
        d1 = {}  # empty dict
        cnt_in_dict = 0  # count for key,value pairs
        while cnt_in_dict < number_of_keys:
            d1.update({random.choice(string.ascii_letters).lower(): random.randint(0, 100)})  # add new random key,value
            cnt_in_dict += 1  # increase count of key,value pairs
        ls_of_dicts.append(d1)  # add new dict to the list
        cnt_in_ls += 1  # increase count of dicts in the list
    return ls_of_dicts


def add_dicts(d, ind, full_dict):
    for letter, number in d.items():                                 # iterating through key,value in dict
        if letter in full_dict.keys():                               # checking if we already have key in full_dict
            if number <= full_dict[letter]:                          # checking if current number smaller than in full_dict
                pass                                                 # skip it
            else:                                                    # current number is bigger
                new_letter = letter+"_"+ind
                full_dict.update({new_letter: number})           # update key,value; add to key index of dict
                full_dict.pop(letter)                                # remove pair with smaller value
        else:                                                        # if key is not in full_dict
            full_dict.update({letter: number})                       # add key, value pair
    return full_dict, ind


def merge_dicts(ls_of_dicts):
    full_dict = {}  # empty resulting dict
    for d in ls_of_dicts:  # iterating through dicts
        ind = str(ls_of_dicts.index(d) + 1)  # saving index of dict for updating full_dict key
        add_dicts(d, ind, full_dict)
    print(full_dict)


ls_of_dicts = create_dicts(2, 10)
merge_dicts(ls_of_dicts)


# homework3
def count_whitespaces(primary_sentence: str) -> int:
    all_symbols = len(primary_sentence)  # count all symbols in the text
    all_words = primary_sentence.split()  # get a list of only words and punctuation
    words_count = 0  # set count of not_whitespaces to 0
    for i in all_words:  # count number of symbols in list of words
        words_count += len(i)
    number_of_whitespaces = all_symbols - words_count  # count whitespaces by subtracting not_whitespaces from all symbols
    return number_of_whitespaces


def fix_sentence_beginning(norm_sentence):
    for ind, symbol in enumerate(norm_sentence):  # using enumerate to get letter and its index
        if symbol == '.':  # checking for '.'
            while (not norm_sentence[ind].isalpha()) and ind < len(
                    norm_sentence) - 1:  # searching for letter after '.' and checking for an end of string
                ind += 1  # index of a letter after '.'
                next_ind = ind + 1  # index of next letter for further concatenation
            norm_sentence = norm_sentence[0:ind] + norm_sentence[ind].upper() + norm_sentence[next_ind:]  # concatenation of string before letter + letter in upper case + rest of the string
    return norm_sentence


def normalize_sentence(primary_sentence):
    low_sentence = primary_sentence.lower()
    norm_sentence = low_sentence.capitalize()  # making first letter upper case
    fix_sentence_beginning(norm_sentence)
    return norm_sentence


def last_words(norm_sentence):
    last_words = []  # empty list for last words of sentences
    all_words = norm_sentence.split()
    for word in all_words:  # using earlier split list of all words in lower case to find words that end with '.'
        if word.endswith(('.', '!', '?', '...')):
            last_words.append(word[:-1])  # adding word to list
    return last_words


def last_word_sentence(norm_sentence):
    last_words(norm_sentence)
    last_sentence = ' '.join(last_words) + '.'  # joining word in list with ' ' and concatenating with '.' at the end
    last_sentence = last_sentence.capitalize()  # making first letter upper case
    new_sentence = norm_sentence + '\n    ' + last_sentence  # adding new sentence in the same style
    return new_sentence


def fix_iz(new_sentence):
    right_sentence = new_sentence.replace(' iz ', ' is ')
    return right_sentence

primary_sentence = '''homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
'''
norm_sentence = normalize_sentence(primary_sentence)
new_sentence = last_word_sentence(norm_sentence)
right_sentence = fix_iz(new_sentence)
print(right_sentence)
number_of_whitespaces = count_whitespaces(primary_sentence)
print(f'\n Number of whitespaces is {number_of_whitespaces}')
