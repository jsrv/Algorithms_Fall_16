# exceptions_fileIO.py
"""Introductory Labs: Exceptions and File I/O.
<Juan S Rodriguez>
<Math 321 Lab>
<September 15>
"""


# Problem 1
def arithmagic():
    step_1 = raw_input("Enter a 3-digit number where the first and last "
                                            "digits differ by 2 or more: ")
    lenstep1 = str(step_1)

    if len(lenstep1) != 3:
        raise ValueError("It should have been 3 digits long")
    a = lenstep1[0]
    b = lenstep1[2]
    a, b = max(a,b), min(a,b)
    print a
    print b
    if (a-b) < 2:
        raise ValueError("It should have been a 2 difference")
    step_2 = raw_input("Enter the reverse of the first number, obtained "
                                            "by reading it backwards: ")
    if lenstep1 != 3:
        raise ValueError("It should have been 3 digits long")
    step_3 = raw_input("Enter the positive difference of these numbers: ")
    step_4 = raw_input("Enter the reverse of the previous result: ")
    print str(step_3) + " + " + str(step_4) + " = 1089 (ta-da!)"


# Problem 2
def random_walk(max_iters=1e12):
    walk = 0
    direction = [-1, 1]
    for i in xrange(int(max_iters)):
        walk += choice(direction)
    return walk


# Problems 3 and 4: Write a 'ContentFilter' class.
if __name__ == "__main__":
    arithmagic()
