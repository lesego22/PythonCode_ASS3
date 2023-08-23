#### EXERCISE 3 30 MARKS############

# Student name: Magoro LM
# Student no: 217233747
# Date: 03/08/2023
# Assignment 3: Python 

####################
## Problem 1 - 10 Points##
####################

# Given the string:
s= 'fullstackslp'

# Use indexing to print out the following:
# 'f'
print(s[0])

# 'p'
print(s[11])

# 'stack'
print(s[4:9])

# 'slp'
print(s[9:])

# 'cks'
print(s[7:10])

# Bonus: Use indexing to reverse the STRINGS

print(s[::-1])

####################
## Problem 2 - LISTS - 5 Marks##
####################

# Using keys and indexing, grab 'hello' from the following Dictionaries:

d1 = {'simple_key':'hello'}
print(d1['simple_key'])

d2 = {'k1':{'k2':'hello'}}
print(d2['k1']['k2'])

d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d3['k1'][0]['nest_key'][1][0])

####################
## Problem 4 - SETS - 4 Marks##
####################

# Use a set to find the unique value of the list bellow:

mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
# Your code here:
set_res=set(mylist)
list_res=(list(set_res))
for item in list_res:
    print(item)

####################
## Problem 5 - FORMATTING - 5 Marks##
####################

# You are given the variables:
age = 45
name = "kyle"

# Use print formatting to print the following string
# "hello my dog's name is kyle and he looks 45 years old"
my_string="hello my dog's name is {} and he looks {} years old".format(name,age)
print(my_string)