# trees.py
"""Volume 2A: Data Structures II (Trees).
<Name>
<Class>
<Date>
"""
import numpy as np
import random
import time
import scipy
from matplotlib import pyplot as plt

class SinglyLinkedListNode(object):
    """Simple singly linked list node."""
    def __init__(self, data):
        self.value, self.next = data, None

class SinglyLinkedList(object):
    """A very simple singly linked list with a head and a tail."""
    def __init__(self):
        self.head, self.tail = None, None
    def append(self, data):
        """Add a Node containing 'data' to the end of the list."""
        n = SinglyLinkedListNode(data)
        if self.head is None:
            self.head, self.tail = n, n
        else:
            self.tail.next = n
            self.tail = n

def iterative_search(linkedlist, data):
    """Search 'linkedlist' iteratively for a node containing 'data'.
    If there is no such node in the list, or if the list is empty,
    raise a ValueError.

    Inputs:
        linkedlist (SinglyLinkedList): a linked list.
        data: the data to search for in the list.

    Returns:
        The node in 'linkedlist' containing 'data'.
    """
    current = linkedlist.head
    while current is not None:
        if current.value == data:
            return current
        current = current.next
    raise ValueError(str(data) + " is not in the list.")

# Problem 1
def recursive_search(linkedlist, data):
    """Search 'linkedlist' recursively for a node containing 'data'.
    If there is no such node in the list, or if the list is empty,
    raise a ValueError.

    Inputs:
        linkedlist (SinglyLinkedList): a linked list object.
        data: the data to search for in the list.

    Returns:
        The node in 'linkedlist' containing 'data'.
    """
    current = linkedlist.head
    def recursivecheese(current, data):

        if current == None:
            raise ValueError(str(data) + " is not in the list.")
        elif current.value == data:
            return current
        #what should I put inside the recursive_search given that I want to take off something from
        else:
            return recursivecheese(current.next, data)
    return recursivecheese(current, data)

class BSTNode(object):
    """A Node class for Binary Search Trees. Contains some data, a
    reference to the parent node, and references to two child nodes.
    """
    def __init__(self, data):
        """Construct a new node and set the data attribute. The other
        attributes will be set when the node is added to a tree.
        """
        self.value = data
        self.prev = None        # A reference to this node's parent node.
        self.left = None        # self.left.value < self.value
        self.right = None       # self.value < self.right.value


class BST(object):
    """Binary Search Tree data structure class.
    The 'root' attribute references the first node in the tree.
    """
    def __init__(self):
        """Initialize the root attribute."""
        self.root = None

    def find(self, data):
        """Return the node containing 'data'. If there is no such node
        in the tree, or if the tree is empty, raise a ValueError.
        """

        # Define a recursive function to traverse the tree.
        def _step(current):
            """Recursively step through the tree until the node containing
            'data' is found. If there is no such node, raise a Value Error.
            """
            if current is None:                     # Base case 1: dead end.
                raise ValueError(str(data) + " is not in the tree.")
            if data == current.value:               # Base case 2: data found!
                return current
            if data < current.value:                # Step to the left.
                return _step(current.left)
            else:                                   # Step to the right.
                return _step(current.right)

                # Start the recursion on the root of the tree.
        return _step(self.root)

    # Problem 2
    def insert(self, data):
        """Insert a new node containing 'data' at the appropriate location.
        Do not allow for duplicates in the tree: if there is already a node
        containing 'data' in the tree, raise a ValueError.

        Example:
            >>> b = BST()       |   >>> b.insert(1)     |       (4)
            >>> b.insert(4)     |   >>> print(b)        |       / \
            >>> b.insert(3)     |   [4]                 |     (3) (6)
            >>> b.insert(6)     |   [3, 6]              |     /   / \
            >>> b.insert(5)     |   [1, 5, 7]           |   (1) (5) (7)
            >>> b.insert(7)     |   [8]                 |             \
            >>> b.insert(8)     |                       |             (8)
        """
        new_node = BSTNode(data)

        if self.root == None:
            self.root = new_node
        else:
            def _adopt(parent, newnode):

                if parent is None:
                    parent = new_node
                elif parent.value == new_node.value:                     # Base case 1: Already there.
                    raise ValueError(str(new_node.value) + " is already on the tree")

                elif parent.value < new_node.value:                # Step to the right.
                    if parent.right is None:
                        parent.right = new_node
                        new_node.prev = parent
                    elif parent.right is not None:
                        _adopt(parent.right, new_node)

                else:                                   # Step to the left.
                    if parent.left is None:
                        parent.left = new_node
                        new_node.prev = parent
                    elif parent.left is not None:
                        _adopt(parent.left, new_node)

            _adopt(self.root, new_node)

    # Problem 3
    def remove(self, data):
        """Remove the node containing 'data'. Consider several cases:
            1. The tree is empty
            2. The target is the root:
                a. The root is a leaf node, hence the only node in the tree
                b. The root has one child
                c. The root has two children
            3. The target is not the root:
                a. The target is a leaf node
                b. The target has one child
                c. The target has two children
            If the tree is empty, or if there is no node containing 'data',
            raise a ValueError.

        Examples:
            >>> print(b)        |   >>> b.remove(1)     |   [5]
            [4]                 |   >>> b.remove(7)     |   [3, 8]
            [3, 6]              |   >>> b.remove(6)     |
            [1, 5, 7]           |   >>> b.remove(4)     |
            [8]                 |   >>> print(b)        |
        """
        def find_yo_kids(rightroot):
            if rightroot.left is None:
                valor = rightroot.value
                self.remove(valor)
                return valor

            if rightroot.left is not None:
                return find_yo_kids(rightroot.left)

        to_delete = self.find(data)

        if self.root is None:
            raise ValueError(str(data) + " the tree is broken.")

        elif to_delete is None:
            raise ValueError(str(data) + " the node is nowhere to be found boy!")

        elif to_delete.value == self.root.value:
            if self.root.right is None and self.root.left is None:              #lonely root works
                self.root = None

            elif self.root.right is not None and self.root.left is not None:    #double kids
                self.root.value = find_yo_kids(self.root.right)

            elif self.root.right is not None:           #right kid only
                new_father = self.root.right
                self.root = new_father
                new_father.prev = None

            elif self.root.left is not None:            #left kid only
                new_father = self.root.left
                self.root = new_father
                new_father.prev = None

        else:                       #data in tree but not root

            if to_delete.right is None and to_delete.left is None:              #Leaf works

                if to_delete.prev.value < to_delete.value:
                    to_delete.prev.right = None
                else:
                    to_delete.prev.left = None

            elif to_delete.right is not None and to_delete.left is not None:    #Double kid
                to_delete.value = find_yo_kids(to_delete.right)

            elif to_delete.right is not None:           #right kid only works
                new_father = to_delete.right
                if to_delete.prev.value < to_delete.value:
                    to_delete.prev.right = to_delete.right
                else:
                    to_delete.prev.left = to_delete.right


            elif to_delete.left is not None:            #left kid only works
                new_father = to_delete.left
                if to_delete.prev.value < to_delete.value:
                    to_delete.prev.right = to_delete.left
                else:
                    to_delete.prev.left = to_delete.left



    def __str__(self):
        """String representation: a hierarchical view of the BST.
        Do not modify this method, but use it often to test this class.
        (this method uses a depth-first search; can you explain how?)

        Example:  (3)
                  / \     '[3]          The nodes of the BST are printed out
                (2) (5)    [2, 5]       by depth levels. The edges and empty
                /   / \    [1, 4, 6]'   nodes are not printed.
              (1) (4) (6)
        """

        if self.root is None:
            return "[]"
        str_tree = [list() for i in xrange(_height(self.root) + 1)]
        visited = set()

        def _visit(current, depth):
            """Add the data contained in 'current' to its proper depth level
            list and mark as visited. Continue recusively until all nodes have
            been visited.
            """
            str_tree[depth].append(current.value)
            visited.add(current)
            if current.left and current.left not in visited:
                _visit(current.left, depth+1)
            if current.right and current.right not in visited:
                _visit(current.right, depth+1)

        _visit(self.root, 0)
        out = ""
        for level in str_tree:
            if level != list():
                out += str(level) + "\n"
            else:
                break
        return out


class AVL(BST):
    """AVL Binary Search Tree data structure class. Inherits from the BST
    class. Includes methods for rebalancing upon insertion. If your
    BST.insert() method works correctly, this class will work correctly.
    Do not modify.
    """
    def _checkBalance(self, n):
        return abs(_height(n.left) - _height(n.right)) >= 2

    def _rotateLeftLeft(self, n):
        temp = n.left
        n.left = temp.right
        if temp.right:
            temp.right.prev = n
        temp.right = n
        temp.prev = n.prev
        n.prev = temp
        if temp.prev:
            if temp.prev.value > temp.value:
                temp.prev.left = temp
            else:
                temp.prev.right = temp
        if n == self.root:
            self.root = temp
        return temp

    def _rotateRightRight(self, n):
        temp = n.right
        n.right = temp.left
        if temp.left:
            temp.left.prev = n
        temp.left = n
        temp.prev = n.prev
        n.prev = temp
        if temp.prev:
            if temp.prev.value > temp.value:
                temp.prev.left = temp
            else:
                temp.prev.right = temp
        if n == self.root:
            self.root = temp
        return temp

    def _rotateLeftRight(self, n):
        temp1 = n.left
        temp2 = temp1.right
        temp1.right = temp2.left
        if temp2.left:
            temp2.left.prev = temp1
        temp2.prev = n
        temp2.left = temp1
        temp1.prev = temp2
        n.left = temp2
        return self._rotateLeftLeft(n)

    def _rotateRightLeft(self, n):
        temp1 = n.right
        temp2 = temp1.left
        temp1.left = temp2.right
        if temp2.right:
            temp2.right.prev = temp1
        temp2.prev = n
        temp2.right = temp1
        temp1.prev = temp2
        n.right = temp2
        return self._rotateRightRight(n)

    def _rebalance(self,n):
        """Rebalance the subtree starting at the node 'n'."""
        if self._checkBalance(n):
            if _height(n.left) > _height(n.right):
                if _height(n.left.left) > _height(n.left.right):
                    n = self._rotateLeftLeft(n)
                else:
                    n = self._rotateLeftRight(n)
            else:
                if _height(n.right.right) > _height(n.right.left):
                    n = self._rotateRightRight(n)
                else:
                    n = self._rotateRightLeft(n)
        return n

    def insert(self, data):
        """Insert a node containing 'data' into the tree, then rebalance."""
        BST.insert(self, data)
        n = self.find(data)
        while n:
            n = self._rebalance(n)
            n = n.prev

    def remove(*args, **kwargs):
        """Disable remove() to keep the tree in balance."""
        raise NotImplementedError("remove() has been disabled for this class.")

def _height(current):
    """Calculate the height of a given node by descending recursively until
    there are no further child nodes. Return the number of children in the
    longest chain down.

    This is a helper function for the AVL class and BST.__str__().
    Abandon hope all ye who modify this function.

                                node | height
    Example:  (c)                  a | 0
              / \                  b | 1
            (b) (f)                c | 3
            /   / \                d | 1
          (a) (d) (g)              e | 0
                \                  f | 2
                (e)                g | 0
    """
    if current is None:
        return -1
    return 1 + max(_height(current.right), _height(current.left))


# Problem 4
def prob4():
    """Compare the build and search speeds of the SinglyLinkedList, BST, and
    AVL classes. For search times, use iterative_search(), BST.find(), and
    AVL.find() to search for 5 random elements in each structure. Plot the
    number of elements in the structure versus the build and search times.
    Use log scales if appropriate.
    """

    with open("english.txt", 'r') as myfile:
        contents = myfile.read()
    dataset = contents.strip().split("\n")
    Avion_Build = []
    Avion_Searc = []
    Barco_Build = []
    Barco_Searc = []
    Singl_Build = []
    Singl_Searc = []

    domain = xrange(10,1000,50)
    for i in domain:

        rand_list = random.sample(dataset, i)

        Tsolve = time.time()
        Avion = AVL()
        for i in xrange(len(rand_list)):
            Avion.insert(rand_list[i])
        Avion_Build.append(time.time()-Tsolve)

        Tsolve = time.time()
        Barco = BST()
        for i in xrange(len(rand_list)):
            Barco.insert(rand_list[i])
        Barco_Build.append(time.time()-Tsolve)

        Tsolve = time.time()
        Singl = SinglyLinkedList()
        for i in xrange(len(rand_list)):
            Singl.append(rand_list[i])
        Singl_Build.append(time.time()-Tsolve)

        subrand_list = random.sample(rand_list, 5)

        Tsolve = time.time()
        for word in subrand_list:
            iterative_search(Singl, word)
        Singl_Searc.append(time.time()-Tsolve)

        Tsolve = time.time()
        for word in subrand_list:
            Avion.find(word)
        Avion_Searc.append(time.time()-Tsolve)

        Tsolve = time.time()
        for word in subrand_list:
            Barco.find(word)
        Barco_Searc.append(time.time()-Tsolve)

    plt.subplot(121)
    plt.loglog(domain, Barco_Build, label="BST")
    plt.loglog(domain, Avion_Build, label="AVL")
    plt.loglog(domain, Singl_Build, label="SLL")
    plt.legend(loc="upper left")
    plt.title("Build Time", fontsize=18)

    plt.subplot(122)
    plt.loglog(domain, Barco_Searc, label="BST")
    plt.loglog(domain, Avion_Searc, label="AVL")
    plt.loglog(domain, Singl_Searc, label="SLL")
    plt.legend(loc="upper left")
    plt.title("Search Time", fontsize=18)

    plt.show()

"""
if __name__ == "__main__":
    B = SinglyLinkedList()
    B.append(34)
    B.append(12)
    print(str(B))
    A = BST()
    A.insert(10)
    A.insert(15)
    A.insert(12)
    A.insert(17)
    A.insert(5)
    A.insert(2)
    A.insert(7)
    A.insert(1)
    A.insert(3)
    A.insert(6)
    A.insert(8)
    A.insert(11)
    A.insert(13)
    A.insert(16)
    A.insert(18)
    A.remove(16)
    A.remove(15)
    A.remove(5)
    A.remove(10)
    print(str(A))


    prob4()
"""
