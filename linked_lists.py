# linked_lists.py
"""Volume II Lab 4: Data Structures 1 (Linked Lists)
<Juan>
<M321L>
<September>
"""


# Problem 1
class Node(object):
    """A basic node class for storing data."""
    def __init__(self, data):
        """Store 'data' in the 'value' attribute. Raise a TypeError if the data is npot an int, long or float"""
        if type(data) is not int and type(data) is not float and type(data) is not long and type(data) is not str:
            raise TypeError("Wrong type of data")

        else:
            self.value = data




class LinkedListNode(Node):
    """A node class for doubly linked lists. Inherits from the 'Node' class.
    Contains references to the next and previous nodes in the linked list.
    """
    def __init__(self, data):
        """Store 'data' in the 'value' attribute and initialize
        attributes for the next and previous nodes in the list.
        """
        Node.__init__(self, data)       # Use inheritance to set self.value.
        self.next = None
        self.prev = None





class LinkedList(object):
    """Doubly linked list data structure class.

    Attributes:
        head (LinkedListNode): the first node in the list.
        tail (LinkedListNode): the last node in the list.
    """
    def __init__(self):
        """Initialize the 'head' and 'tail' attributes by setting
        them to 'None', since the list is empty initially.
        """

        self.head = None
        self.tail = None

    def find(self, data):
        A = self.head

        def real_find(a,b):
            if a is None:
                raise ValueError("You are very bad at programming... just sayin")
            elif a.value == b:
                return a
            else:
                return real_find(a.next, b)

        return real_find(A, data)



    def append(self, data):
        """Append a new node containing 'data' to the end of the list."""
        # Create a new node to store the input data.

        new_node = LinkedListNode(data)
        if self.head is None:
            # If the list is empty, assign the head and tail attributes to
            # new_node, since it becomes the first and last node in the list.
            self.head = new_node
            self.tail = new_node
        else:
            # If the list is not empty, place new_node after the tail.
            self.tail.next = new_node               # tail --> new_node
            new_node.prev = self.tail               # tail <-- new_node
            # Now the last node in the list is new_node, so reassign the tail.
            self.tail = new_node

    # Problem 2
    def find(self, data):
        """Return the first node in the list containing 'data'.
        If no such node exists, raise a ValueError.

        Examples:
            >>> l = LinkedList()
            >>> for i in [1,3,5,7,9]:
            ...     l.append(i)
            ...
            >>> node = l.find(5)
            >>> node.value
            5
            >>> l.find(10)
            ValueError: <message>
        """

        def _step(current):
            """Recursively step through the linkedlist until the node containing
            'data' is found. If there is no such node, raise a Value Error.
            """
            if current is None:                     # Base case 1: dead end.
                raise ValueError(str(data) + " is not in the list.")
            if data == current.value:               # Base case 2: data found!
                return current
            if data != current.value:                # Step to the left.
                return _step(current.next)

        return _step(self.head)

    # Problem 3
    def __len__(self):
        """Return the number of nodes in the list.

        Examples:
            >>> l = LinkedList()
            >>> for i in [1,3,5]:
            ...     l.append(i)
            ...
            >>> len(l)
            3
            >>> l.append(7)
            >>> len(l)
            4
        """
        largo = 0
        current = self.head
        while current is not None:
            largo += 1
            current = current.next
        return largo


    # Problem 3
    def __str__(self):
        """String representation: the same as a standard Python list.

        Examples:
            >>> l1 = LinkedList()   |   >>> l2 = LinkedList()
            >>> for i in [1,3,5]:   |   >>> for i in ['a','b',"c"]:
            ...     l1.append(i)    |   ...     l2.append(i)
            ...                     |   ...
            >>> print(l1)           |   >>> print(l2)
            [1, 3, 5]               |   ['a', 'b', 'c']
        """
        current = self.head
        string = []
        while current is not None:
            string.append(current.value)
            current = current.next
        return str(string)

    # Problem 4
    def remove(self, data):
        """Remove the first node in the list containing 'data'. Return nothing.

        Raises:
            ValueError: if the list is empty, or does not contain 'data'.

        Examples:
            >>> print(l1)       |   >>> print(l2)
            [1, 3, 5, 7, 9]     |   [2, 4, 6, 8]
            >>> l1.remove(5)    |   >>> l2.remove(10)
            >>> l1.remove(1)    |   ValueError: <message>
            >>> l1.remove(9)    |   >>> l3 = LinkedList()
            >>> print(l1)       |   >>> l3.remove(10)
            [3, 7]              |   ValueError: <message>
        """
        the_node = self.find(data)


        if the_node == self.head:
            self.head = the_node.next

        elif the_node == self.tail:
            befi = self.tail.prev
            befi.next = None
            self.tail = befi

        elif the_node == self.head and self.head.next is None:
            self.head = the_node.next
            self.tail = None

        else:
            nexti = the_node.next
            befi = the_node.prev
            nexti.prev = befi
            befi.next = nexti



    # Problem 5
    def insert(self, data, place):
        """Insert a node containing 'data' immediately before the first node
        in the list containing 'place'. Return nothing.

        Raises:
            ValueError: if the list is empty, or does not contain 'place'.

        Examples:
            >>> print(l1)           |   >>> print(l1)
            [1, 3, 7]               |   [1, 3, 5, 7, 7]
            >>> l1.insert(7,7)      |   >>> l1.insert(3, 2)
            >>> print(l1)           |   ValueError: <message>
            [1, 3, 7, 7]            |
            >>> l1.insert(5,7)      |   >>> l2 = LinkedList()
            >>> print(l1)           |   >>> l2.insert(10,10)
            [1, 3, 5, 7, 7]         |   ValueError: <message>
        """
        new_node = LinkedListNode(data)
        the_place = self.find(place)

        if the_place == self.head:
            new_second = self.head
            new_node.next = new_second
            self.head = new_node


        else:
            new_second = the_place
            same_prev = the_place.prev

            same_prev.next = new_node
            new_second.prev = new_node
            new_node.next = new_second
            new_node.prev = same_prev

# Problem 6: Write a Deque class.

class Deque(LinkedList):
    def __init__(self):
        LinkedList.__init__(self)

    def pop(self):
        thisone = self.tail.value
        befi = self.tail.prev
        befi.next = None
        self.tail = befi
        return thisone

    def popleft(self):
        thisone = self.head
        valor = thisone.value
        self.head = thisone.next
        return valor

    def appendleft(self, data):
        new_node = LinkedListNode(data)
        new_second = self.head
        new_node.next = new_second
        self.head = new_node

    def remove(*args, **kwargs):
        raise NotImplementedError("Use pop() or popleft() for removal")

    def insert(*args, **kwargs):
        raise NotImplementedError("Use pop() or popleft() for removal")
# Problem 7

def prob7(infile, outfile):
    """Reverse the file 'infile' by line and write the results to 'outfile'."""
    with open(infile, 'r') as myfile:
        contents = myfile.read()

    with open(outfile, "w") as thefile:
        lines = contents.strip().split("\n")
        #for i in xrange(len(lines)):
        lines.reverse()
        thefile.write("\n".join(lines))


if __name__ == "__main__":
    print True
