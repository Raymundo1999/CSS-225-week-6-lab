#Raymundo Sanchez
#Nov 9,2020

#these two import will help since i will be able to use random and math formulas
import math
import random

#what this code will do is loop 10 times and each time it will be giving you a random integer
#and the random integers are going to be in between the numbers 25 to 35.
#the response will be given if you run it on the drive_code
def loop():
    for i in range (10):
        print ("Random integer: ", random.randint(25,35))
    
#--------------------------------------------------------------------

#this defines the lists so it can be used here and on the driver_code
#the return will return a ramdom element from the list of numbers from our drive.
#this will give us a random element from the numbers we chose of our numbers variable on our driver_code.
def lists(random_element):
    return random.choice (random_element)

#--------------------------------------------------------------------

#this will give us "one" odd number from "0 to 100"
#and then return it to us if it doesn't get an odd number and gets a even number it will make it in odd number by adding a 1
#this part is made in the else statement
#it return the even number and will add a 1 or as the return says a +1.
def odd():
    num = random.randint(0,100)
    if not num %2 ==0:
        return num
    else:
        return num +1

#-------------------------------------------------------------------

#this will caculate the a and b and give you the response to c
#fist we calculate the a square and b square which are both the math.pow to actually be able to do the square for both a and b
#then we add the letter_c = letter_a + letter_b so that we can then add the return math.sqrt letter_c
#this top part just calculates everything then square roots it with the math.sqrt
#by actually getting a response you will have to add the numbers you want (you choose the two numbers) which will be a and b
#you add the two numbers on the driver_code where it says "pythagorean (,)" <---- in here in the paratheses
#it will then print out the response and show you.
def pythagorean(a,b):
    letter_a = math.pow (a,2)
    letter_b = math.pow (b,2)
    letter_c = letter_a + letter_b
    return math.sqrt(letter_c)
    
    
