import string
import random

# create a list of random number of dicts (from 2 to 10)
number_of_dict = random.randint(2, 10)                               # randomly choose number of dicts in a list
ls_of_dicts = []                                                     # empty list
cnt_in_ls = 0                                                        # count for dict in the list
while cnt_in_ls < number_of_dict:                                    #
    number_of_keys = random.randint(2, 10)                           # randomly choose number of key,value pairs in dict
    d1 = {}                                                          # empty dict
    cnt_in_dict = 0                                                  # count for key,value pairs
    while cnt_in_dict < number_of_keys:
        d1.update({random.choice(string.ascii_letters).lower(): random.randint(0, 100)})  # add new random key,value
        cnt_in_dict += 1                                             # increase count of key,value pairs
    ls_of_dicts.append(d1)                                           # add new dict to the list
    cnt_in_ls += 1                                                   # increase count of dicts in the list

# get previously generated list of dicts and create one common dict
full_dict = {}                                                       # empty resulting dict
for d in ls_of_dicts:                                                # iterating through dicts
    ind = str(ls_of_dicts.index(d) + 1)                              # saving index of dict for updating full_dict key
    for letter, number in d.items():                                 # iterating through key,value in dict
        if letter in full_dict.keys():                               # checking if we already have key in full_dict
            if number <= full_dict[letter]:                          # checking if current number smaller than in full_dict
                pass                                                 # skip it
            else:                                                    # current number is bigger
                full_dict.update({letter+"_"+ind: number})           # update key,value; add to key index of dict
                full_dict.pop(letter)                                # remove pair with smaller value
        else:                                                        # if key is not in full_dict
            full_dict.update({letter: number})                       # add key, value pair

print(full_dict)                                                     # print resulting dict

'''
Unfortunately could not implement backtracking of indexes for situations like:
[{'w': 64, 'p': 3}, {'w': 32, 'x': 38, 'y': 25}] result would be:
{'w': 64, 'p': 3, 'x': 38, 'y': 25} instead of
{'w_1': 64, 'p': 3, 'x': 38, 'y': 25}
'''
