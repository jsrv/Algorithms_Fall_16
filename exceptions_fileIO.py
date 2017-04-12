# exceptions_fileIO.py
"""Introductory Labs: Exceptions and File I/O.
<Juan S Rodriguez>
<Math 321 Lab>
<September 15>
"""
from random import choice

# Problem 1
def arithmagic():
    step_1 = raw_input("Enter a 3-digit number where the first and last "
                                            "digits differ by 2 or more: ")
    lenstep1 = str(step_1)

    if len(step_1) != 3:
        raise ValueError("It should have been 3 digits long")

    a = step_1[0]
    b = step_1[2]
    a, b = max(a,b), min(a,b)
    print a
    print b
    A = float(a)
    B = float(b)
    if (A-B) < 2:
        raise ValueError("It should have been a 2 difference")
    step_2 = raw_input("Enter the reverse of the first number, obtained "
                                            "by reading it backwards: ")
    if (step_1[::-1]) != step_2:
        raise ValueError("It should have been the reverse dude")


    step_3 = raw_input("Enter the positive difference of these numbers: ")
    c, d = max(step_2, step_1), min(step_2, step_1)
    C = int(c)
    D = int(d)
    print C
    print D
    if int(step_3) != (C-D):
        raise ValueError("You should learn how to substract better")

    step_4 = raw_input("Enter the reverse of the previous result: ")
    if step_3[::-1] != step_4:
        raise ValueError("Last step failed, so close though!")

    print str(step_3) + " + " + str(step_4) + " = 1089 (ta-da!)"



# Problem 2
def random_walk(max_iters=1e12):

    try:
        walk = 0
        direction = [-1, 1]
        for i in xrange(int(max_iters)):
            walk += choice(direction)
        print("process completed")
    except KeyboardInterrupt:
        print ["Process interrupted at iteration ", i]

    return walk

class ContentFilter(object):
    def __init__(self, FileName):
        if type(FileName) != str:
            raise TypeError("You should learn what a string is.")
        with open(FileName, 'r') as myfile:
            self.contents = myfile.read()
        self.FileName=FileName


    def uniform(self, outfile, mode = "w", case = "upper"):

        if mode != "w" and mode != "a":
            raise ValueError("You need to choose a different mode")

        with open(outfile, mode) as thefile:
            if case == "upper":
                thefile.write(self.contents.upper())

            elif case == "lower":
                thefile.write(self.contents.lower())

            else:
                raise ValueError("You need to choose a different case")



    def reverse(self, outfile, unit="line", mode="w"):
        if mode != "w" and mode != "a":
            raise ValueError("You need to choose a different mode")

        with open(outfile, mode) as thefile:
            if unit == "line":
                lines = self.contents.strip().split("\n")
                #for i in xrange(len(lines)):
                lines.reverse()
                thefile.write("\n".join(lines))

            elif unit == "word":
                lines = self.contents.strip().split("\n")
                for i in xrange(len(lines)):
                    words = lines[i].split(" ")
                    words.reverse()
                    thefile.write(" ".join(words))
                    thefile.write("\n")

            else:
                raise ValueError("You need to choose a different unit")


    def transpose(self, outfile, mode="w"):

        if mode != "w" and mode != "a":
            raise ValueError("You need to choose a different mode")

        with open(outfile, mode) as thefile:
            a = self.contents
            matrix = self.contents.strip().split("\n")
            numbrows = len(matrix)
            numbcols = len(matrix[0].split(" "))

            new_mat = [[0]*numbrows for i in range(numbcols)]

            maxi = max(numbcols,numbrows)
            mini = min(numbcols,numbrows)

            for i in xrange(numbrows):
                matrix[i] = matrix[i].split(" ")


            for i in xrange(numbrows):
                for j in xrange(numbcols):
                    new_mat[j][i] = matrix [i][j]
            thefile.write('\n'.join(' '.join(new_mat[i]) for i in xrange(numbcols)))


    def __str__(self):
        a = self.contents

        spaces = 0
        tabs = 0
        newline = 0

        for i,line in enumerate(a):
            spaces += line.count(' ')
            tabs += line.count('\t')
            newline += line.count('\n')
        totalw = spaces + tabs + newline

        lines = len(self.contents.split("\n"))
        tots = len(a)
        alpha = len([c for c in a if c.isalpha()])
        numbs = len([c for c in a if c.isdigit()])
        whites = len([c for c in a if c.isspace()])

        car = "Source file:" + "\t" + "\t"+ "\t" + self.FileName + "\n" + "Total characters:" + "\t"+ "\t" + str(tots) + "\n" + "Alphabetic characters:" + "\t"+ "\t" +  str(alpha) + "\n"
        car += "Numerical characters:" + "\t"+ "\t"+str(numbs) + "\n" + "Whitespace characters:" +  "\t"+ "\t" +  str(totalw) + "\n" + "Number of lines:" + "\t"+ "\t" + str(lines)
        return car


# Problems 3 and 4: Write a 'ContentFilter' class.
"""if __name__ == "__main__":
    testdrive = ContentFilter("car.txt")
    print(testdrive)
    testdrive.reverse("outfile.txt","word")
    testdrive.transpose("outfile1.txt")
"""
