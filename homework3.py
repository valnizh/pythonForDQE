import re

primary_sentence = '''homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
'''

low_sentence = primary_sentence.lower()              # make all letters lower case

# Calculating number of whitespaces                  # first let`s calculate whitespaces? because it is need to be donr in original text
all_symbols = len(low_sentence)                      # count all symbols in the text
all_words = low_sentence.split()                     # get a list of only words and punctuation
words_count = 0                                      # set count of not_whitespaces to 0
for i in all_words:                                  # count number of symbols in list of words
    words_count += len(i)
number_of_whitespaces = all_symbols - words_count    # count whitespaces by subtracting not_whitespaces from all symbols

# Normalizing letter cases
norm_sentence = low_sentence.capitalize()                                                              # making first letter upper case
for ind, symbol in enumerate(norm_sentence):                                                           # using enumerate to get letter and its index
    if symbol == '.':                                                                                  # checking for '.'
        while (not norm_sentence[ind].isalpha()) and ind < len(norm_sentence) - 1:                     # searching for letter after '.' and checking for an end of string
            ind += 1                                                                                   # index of a letter afer '.'
            next_ind = ind + 1                                                                         # index of next letter for further concatination
        norm_sentence = norm_sentence[0:ind] + norm_sentence[ind].upper() + norm_sentence[next_ind:]   # concatination of string before letter + letter in upper case + rest of the string

# Sentence made of last words
last_words = []                                                 # empty list for last words of sentences
for word in all_words:                                          # using earlier split list of all words in lower case to find words that end with '.'
    if word.endswith('.'):
        last_words.append(word[:-1])                            # adding word to list
last_sentence = ' '.join(last_words) + '.'                      # joining word in list with ' ' and concatinating with '.' at the end
last_sentence = last_sentence.capitalize()                      # making first letter upper case
new_sentence = norm_sentence + '\n    ' + last_sentence         # adding new sentence in the same style

# Fix“iz” with correct “is”

right_sentence = new_sentence.replace(' iz ', ' is ')           # because "iz" only incorrect in cases where it's "is", not in a middle of words: simply replacing it

# printing new correct sentence and count of whitespaces in original one
print(right_sentence)
print(f'\n Number of whitespaces is {number_of_whitespaces}')
