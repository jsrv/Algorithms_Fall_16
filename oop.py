# oop.py
"""Introductory Labs: Object Oriented Programming.
<Juan S Rodriguez>
<Math 320>
<September 8>
"""

def test_backpack():
    testpack = Backpack("Barry", "black") # Instantiate the object.
    if testpack.max_size != 5: # Test an attribute.
        print("Wrong default max_size!")
    for item in ["pencil", "pen", "paper", "computer","bike","car"]:
        testpack.put(item) # Test a method.
    print(testpack.contents)

def test_jetpack():
    testpack1 = Jetpack("Pedro", "negra") # Instantiate the object.
    if testpack1.max_size != 2: # Test an attribute.
        print("Wrong default max_size!")
    for item in ["lapiz", "esfero", "papel", "pc","bici"]:
        testpack1.put(item) # Test a method.
    print testpack1.fuel
    testpack1.fly(2)
    print testpack1.fuel
    testpack1.dump()
    print testpack1.fuel
    testpack1.fly(2)

class Backpack(object):
    """A Backpack object class. Has a name and a list of contents.

    Attributes:
        name (str): the name of the backpack's owner.
        contents (list): the contents of the backpack.
    """

    # Problem 1: Modify __init__() and put(), and write dump().
    def __init__(self, name, color, max_size=5):
        """Set the name and initialize an empty contents list.

        Inputs:
            name (str): the name of the backpack's owner.

        Returns:
            A Backpack object wth no contents.
        """
        self.name = name
        self.contents = []
        self.max_size = max_size
        self.color = color

    def put(self, item):
        """Add 'item' to the backpack's list of contents."""
        if len(self.contents) < self.max_size:
            self.contents.append(item)
        else:
            print "No Room!"

    def take(self, item):
        """Remove 'item' from the backpack's list of contents."""
        self.contents.remove(item)

    def dump(self):
        self.contents = []

    # Magic Methods -----------------------------------------------------------

    # Problem 3: Write __eq__() and __str__().
    def __add__(self, other):
        """Add the number of contents of each Backpack."""
        return len(self.contents) + len(other.contents)

    def __lt__(self, other):
        """Compare two backpacks. If 'self' has fewer contents
        than 'other', return True. Otherwise, return False.
        """
        return len(self.contents) < len(other.contents)

    def __eq__(self, other):
        if (self.color == other.color) and (self.name == other.name) and (self.contents == other.contents):
            return True
        else:
            return False

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        printable1 = "Owner: "+"\t\t"+str(self.name)+"\n"+"Color: "+"\t\t"+str(self.color)+"\n""Size: "+"\t\t"+str(len(self.contents))+"\n"
        printable2 = "Max Size: " + "\t" + str(self.max_size) +"\n"+"Contents: "+"\t"+ str(self.contents)
        printable = printable1 + printable2
        return printable

# An example of inheritance. You are not required to modify this class.
class Knapsack(Backpack):
    """A Knapsack object class. Inherits from the Backpack class.
    A knapsack is smaller than a backpack and can be tied closed.

    Attributes:
        name (str): the name of the knapsack's owner.
        color (str): the color of the knapsack.
        max_size (int): the maximum number of items that can fit
            in the knapsack.
        contents (list): the contents of the backpack.
        closed (bool): whether or not the knapsack is tied shut.
    """
    def __init__(self, name, color, max_size=3):
        """Use the Backpack constructor to initialize the name, color,
        and max_size attributes. A knapsack only holds 3 item by default
        instead of 5.

        Inputs:
            name (str): the name of the knapsack's owner.
            color (str): the color of the knapsack.
            max_size (int): the maximum number of items that can fit
                in the knapsack. Defaults to 3.

        Returns:
            A Knapsack object with no contents.
        """
        Backpack.__init__(self, name, color, max_size)
        self.closed = True

    def put(self, item):
        """If the knapsack is untied, use the Backpack.put() method."""
        if self.closed:
            print("I'm closed!")
        else:
            Backpack.put(self, item)

    def take(self, item):
        """If the knapsack is untied, use the Backpack.take() method."""
        if self.closed:
            print("I'm closed!")
        else:
            Backpack.take(self, item)




# Problem 2: Write a 'Jetpack' class that inherits from the 'Backpack' class.
class Jetpack(Backpack):
    def __init__(self, name, color, max_size=2):
        Backpack.__init__(self, name, color, max_size)
        self.fuel=10

    def fly(self, amount):
        if self.fuel < amount:
            print("Not enough fuel!")
        else:
            self.fuel -= amount

    def dump(self):
        Backpack.dump(self)
        self.fuel = 0
# Problem 4: Write a 'ComplexNumber' class.

class ComplexNumber(object):
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def conjugate(self):
        return ComplexNumber(self.real, -self.imag)

    def __abs__(self):
        return (((self.real**2)+(self.imag**2))**(.5))

    def __lt__(self, other):
        if abs(self) < abs(other):
            return True

        elif abs(self) >= abs(other):
            return False


    def __gt__(self, other):
        if abs(self) > abs(other):
            return True

        elif abs(self) <= abs(other):
            return False


    def __eq__(self, other):
        if (self.imag == other.imag) and (self.imag == other.imag):
            return True
        else:
            return False


    def __ne__(self, other):
        return not self == other


    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.imag * other.real + self.real * other.imag
        return ComplexNumber(real,imag)

    def __div__(self, other):
        numerator = self * other.conjugate()
        denominator = other.real**2 + other.imag**2
        really = (float(numerator.real))/denominator
        fakey = (float(numerator.imag))/denominator
        return ComplexNumber(really, fakey)

    def __str__(self):
        thenumb = "(" + str(self.real)+ " + " + str(self.imag) + "i" ")"
        return thenumb





"""if __name__ == "__main__":
    test_backpack()
    test_jetpack()"""
