#Raymundo Sanchez
#Nov 9,2020

import my_module
#this will make the loop work and show when you run
#the step to actually make it work are in the my_module
#one this to remember is to always put the location where are steps are coming from
my_module.loop()

#-------------------------------------------------------------

#this is the list that I had chosen to return the random element
#the print statement is so that it actually shows you what the random element you got
#even though it is a random element it will only ever show 2,11,or 28
#then it will show you one of these three numbers in the list it can also be bigger the list
number = my_module.lists(["2","11","28","17","66"])
print(number)

#-------------------------------------------------------------

#this will give you a random odd number
#what this means is that it will give you a number if it can't be devided by 2.
#and if you get a number that can be devided by 2 the code on my_Module will add a extra 1 to make it in odd number
#this will also be shown when you run it.
interger = my_module.odd()
print(interger)

#-------------------------------------------------------------

#this will calculate the a, and b which become the two numbers you add down here and it will give you the the response which will be c
# this will also be printed out and show when you run it with everything else.

math_problem = my_module.pythagorean(99,15)
print (math_problem)


