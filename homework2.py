import string
import random

# create a list of random number of dicts (from 2 to 10)
number_of_dict = random.randint(2, 10)
ls_of_dicts = []
cnt_in_ls = 0
while cnt_in_ls < number_of_dict:
    number_of_keys = random.randint(2, 10)
    d1 = {}
    cnt_in_dict = 0
    while cnt_in_dict < number_of_keys:
        d1.update({random.choice(string.ascii_letters).lower(): random.randint(0, 100)})
        cnt_in_dict += 1
    ls_of_dicts.append(d1)
    cnt_in_ls += 1

# get previously generated list of dicts and create one common dict
full_dict = {}
for d in ls_of_dicts:
    ind = str(ls_of_dicts.index(d) + 1)
    for letter, number in d.items():
        if letter in full_dict.keys():
            if number <= full_dict[letter]:
                pass
            else:
                full_dict.update({letter+"_"+ind: number})
                full_dict.pop(letter)
        else:
            full_dict.update({letter: number})
print(number_of_dict, ls_of_dicts)
print(full_dict)
