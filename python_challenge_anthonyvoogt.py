'''
Python Challenge
version 1.0
Author: Anthony Voogt
Opdrachtgever: Nick Douma
Bronnen: 
"stackoverflow.com"
"geeksforgeeks.com"
"w3schools.com"
'''

# Maak de onderstaande challenges in Python. Je aanpak en keuzes staan hierbij centraal.
# Challenges bevatten welke input en output je code dient te accepteren en produceren:

# 1. Reverse a string
# used a question as well, to make it more clear for the user



reverse = input ("which word would you like to reverse? ")
print (reverse[::-1])


# 2. Reverse a sentence.
# Function to reverse words of string 
def rev_sentence(sentence): 
  
#     # first split the string into words 
    words = sentence.split(' ') 
  
#     # then reverse the split string list and join using space 
    reverse_sentence = ' '.join(reversed(words)) 
  
#     # finally return the joined string 
    return reverse_sentence 

inp = 'John likes Dogs'
print (rev_sentence(inp))
# ik heb deze oplossing gevonden op geeksforgeeks, ik kon dit niet zelf bedenken.



# 3.Find a minimum in a list of integers.
# 4. Find a maximum in a list of integers.

# I've done this item within my own knowledge, it took some time. but eventually 
# i had to use google, found out that i wasnt that far off. 
# only thing was that i had to define the min and max from list "cijfers"

cijfers = [100, 600, 300, 10, 2, -100, 0]

# lowest_number = min()
# highest_number = max()


lowest_number = min(cijfers)
highest_number = max(cijfers)

print (lowest_number)
print (highest_number)


# 5. Calculate the remainder of a division.

# new function which divides
# arguments: in1 = a number, in2 = a number
# rm stands for remainder
def calculate_remainder (in1, in2):
    rm = in1 % in2
    return rm

#input question for user
number1 = input("choose a number you want to calculate the remainder for: ")
number2 = input("choose another number: ")

# str to int for a whole number 
number1 = int(number1)
number2 = int(number2)

# checksum with a round
remainder = calculate_remainder(number1, number2)
print ("The remainder of the sum is:", (remainder))



# 6. Return the unique values in a list.

inp = [1, 1, 2, 3, 4, 4, "a", "a", "z"]
# make it a set, in that way the "extra" numbers become redundant and get expelled from the set list.
myset =list(set(inp))
print(myset)

#7. Return the unique values in a list and the count of occurrences.
from collections import Counter
inp = [1, 1, 2, 3, 4, 4, "a", "a", "z"]
print (Counter(inp))
# When i run this program it will counter the highest ones first. 



# 8. Given a calculation string, calculate the result.

# inp = "3 + 2 / 5"
# out = 3.4
# i've used a previous made calculator


def calculate_string (in1, in2, in3):
    rm = in1 + in2 / in3 
    return rm

#input question for user
number1 = input("Choose a number: ")
number2 = input("Choose another number you want to add: ")
number3 = input("Choose a number you would like to divide: ")

# str to int for a whole number 
number1 = int(number1)
number2 = int(number2)
number3 = int(number3)

# checksum
divided = calculate_string(number1, number2, number3)
print ("The checksum is:",(divided))



# 9. Create a method that calculates a Fibonacci sequence for n=20 counts.


def fibonacci(n):
    start = [0,1]
    for i in range (n-1):
        start.append(start[i] + start[i+1])
    return start
print (fibonacci(20))

# de start is [0,1], de rest van de getallen de vorige 2 opgetelde getallen toe aan de reeks. 

#10. Filter a list of objects by an object property.

class Foo:
    prop = None
    def __init__(self, prop):
        self.prop = prop


def filter_obj(inp, waarde):
    lijst = []
    # Loop over alle elementen in de lijst
    for obj in inp:
        if obj.prop == waarde:
            lijst.append(obj)
    return lijst

inp = [Foo("a"), Foo("a"), Foo("b"), Foo("c")]
out = filter_obj(inp, "b")

print(out)

# 11. Produce a list of values based on a property of a list of objects.

def list_obj(inp, waarde):
    l = [getattr(obj, waarde) for obj in inp]
    return l

#ik blijf een code krijgen als 0x0000001c0ca5 etc. 
#helaas krijg ik opdracht 10 en 11 niet werkend.







