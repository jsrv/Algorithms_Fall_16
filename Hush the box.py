"""Shut the box"""
import random
import box as b
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


if __name__ == "__main__":

    person = raw_input('Enter your name: ')
    remain = numblist
    print('Hello', person)
    res = base(remain, person)
    while res[0] == True:
        res = base(res[1], person)
    print "Game over"
    print "Final score: "
    print sum(res[1])
