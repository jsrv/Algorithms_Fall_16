# standard_library.py
"""Introductory Labs: The Standard Library.
<Juan S Rodriguez>
<White Cohort - 321>
<Sept/9/2016>
"""


import calculator as c
import box as b
import sys
import random

# Problem 1
def prob1(l):
    """Accept a list 'l' of numbers as input and return a new list with the
    minimum, maximum, and average of the contents of 'l'.
    """
    ordenado = [min(l),max(l),sum(l)/float(len(l))]
    return ordenado



# Problem 2
def prob2():
    """Programmatically determine which Python objects are mutable and which
    are immutable. Test numbers, strings, lists, tuples, and dictionaries.
    Print your results to the terminal.
    """
#numeros
    siete = 7
    ocho = siete
    ocho += 1
    check1 = (siete == ocho)
    if check1 == True:
        print "numbers are mutable!"
    else:
        print "numbers are immutable!"
#strings
    casa = 'morad'
    color = casa
    color += 'a'
    check2 = (casa == color)
    if check2 == True:
        print "strings are mutable!"
    else:
        print "strings are immutable!"
#lists
    fibonacci = [1,1,2,3,5,8]
    aberra =fibonacci
    aberra.append(1)
    check3 = (aberra == fibonacci)
    if check3 == True:
        print "lists are mutable!"
    else:
        print "lists are immutable!"
#tuples
    fibonaccis = (1,1,2,3,5,8)
    aberras =fibonaccis
    aberras += (3,)
    check4 = (aberras == fibonaccis)
    if check4 == True:
        print "tuples are mutable!"
    else:
        print "tuples are immutable!"
#dictionaries
    dict_1 = {1: 'x', 2: 'b'} # Create a dictionary.
    dict_2 = dict_1 # Assign it a new name.
    dict_2[1] = 'a' # Change the 'new' dictionary.
    check5 = (dict_1 == dict_2) # Compare the two names.
    if check5 == True:
        print "dict are mutable!"
    else:
        print "dict are immutable!"


# Problem 3: Create a 'calculator' module and implement this function.


def prob3(a,b):
    """Calculate and return the length of the hypotenuse of a right triangle.
    Do not use any methods other than those that are imported from your
    'calculator' module.

    Parameters:
        a (float): the length one of the sides of the triangle.
        b (float): the length the other nonhypotenuse side of the triangle.

    Returns:
        The length of the triangle's hypotenuse.
    """
    proda = c.prodos(a,a)
    prodb = c.prodos(b,b)
    add = c.sumdos(proda,prodb)
    resultado = c.sqbt(add)
    return resultado
    pass


# Problem 4: Implement shut the box.
numblist=[1,2,3,4,5,6,7,8,9]

#Checks on the rolling number of dice and obtains the roll
def rolling(n):
    if n > 6:
        x = random.randint(1,6)
        y = random.randint(1,6)
        z = x + y
        return z
    else:
        x = random.randint(1,6)
        return x

#funcation to the determine the outcome of the turn
def winorlus(n,r):
    s = b.isvalid(n,r)
    return s

#Chack if the input given can actually take away options from the list
def checklist(roll, lists, remain):
    if sum(lists) == roll:
        if set(lists).issubset(set(remain)):
            return True

    else:
        print "invalid entry"
        return False

#Backbone of the whole operation
def base(r, person):
    print
    print('Numbers left: ', r)
    z = rolling(sum(r))
    print('Roll: ', z)
    result = winorlus(z,r)
    if result == True:
        numbers = raw_input("Numbers to eliminate: ")
        sublist = (b.parse_input(numbers,r))
        possibl = checklist(z,sublist,r)

        while possibl == False:
            numbers = raw_input("Try a different entry: ")
            sublist = (b.parse_input(numbers,r))
            possibl = checklist(z,sublist,r)

        r = [x for x in r if x not in sublist]

    else:
        print
        print(person, ', you are a looser.')
        print

    return result, r

def thename():
    if len(sys.argv) != 2:
        person = raw_input('Enter your name: ')
    else:
        person = (sys.argv[1])
    remain = numblist
    print('Hello', person)
    res = base(remain, person)
    while res[0] == True:
        res = base(res[1], person)
    print "Game over"
    print "Final score: "
    print sum(res[1])



if __name__ == "__main__":
    thename()
