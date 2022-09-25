from random import randint                            # to use random numbers generator

# creating a list of 100 random numbers from 0 to 1000
numbers = 100                                         # quantity of numbers in a list
ls = []                                               # empty list
while len(ls) < numbers:                              # loop for appending the list while it's shorter than 100
    ls.append(randint(0, 1000))                       # adding new number to the list

# sorting the list from min to max
for i in range(0, numbers-1):                         # loop for checking numbers in the list by indexes(i)
    if ls[i] <= ls[i+1]:                              # if current number is than following ->
        pass                                          # leave it as is
    else:                                             # in other case(when current is greater than following) ->
        ls[i], ls[i+1] = ls[i+1], ls[i]               # change their places in the list

# calculating avg from even and odd numbers
sum_odd = 0                                           # variable for summing odd numbers
odd = 0                                               # variable for counting odd numbers
sum_even = 0                                          # variable for summing even numbers
even = 0                                              # variable for counting even numbers
for num in ls:                                        # loop to determine if number is odd or even
    if num % 2 == 1:                                  # checking if modulus of number by 2 equal to 1
        sum_odd += num                                # adding odd number to sum_odd
        odd += 1                                      # incrementing odd numbers count by 1
    else:                                             #
        sum_even += num                               # adding even number to sum_even
        even += 1                                     # incrementing even numbers count by 1
try:                                                  # using try if there would be no odd numbers
    avg_odd = sum_odd / odd                           # counting average of odd numbers
    print('Average for odd numbers: ', avg_odd)       # printing result
except ZeroDivisionError:                             # handling of no odd numbers situation
    print('No odd numbers')                           # printing result

try:                                                  # using try if there would be no even numbers
    avg_even = sum_even / even                        # counting average of even numbers
    print('Average for even numbers: ', avg_even)     # printing result
except ZeroDivisionError:                             # handling of no even numbers situation
    print('No even numbers')                          # printing result
