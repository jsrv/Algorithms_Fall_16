# kdtrees.py
"""Volume 2A: Data Structures 3 (K-d Trees).
<Name>
<Class>
<Date>
"""

import numpy as np
from trees import BST
from scipy.spatial import KDTree
from sklearn import neighbors

# Problem 1
def metric(x, y):
    """Return the euclidean distance between the 1-D arrays 'x' and 'y'.

    Raises:
        ValueError: if 'x' and 'y' have different lengths.

    Example:
        >>> metric([1,2],[2,2])
        1.0
        >>> metric([1,2,1],[2,2])
        ValueError: Incompatible dimensions.
    """
    if len(x) != len(y):
        raise ValueError("The arrays must be of the same size")

    else:
        a = 0
        for i in xrange(len(x)):
            a += (x[i]-y[i])**2
        a = a**.5
    return a


# Problem 2
def exhaustive_search(data_set, target):
    """Solve the nearest neighbor search problem exhaustively.
    Check the distances between 'target' and each point in 'data_set'.
    Use the Euclidean metric to calculate distances.

    Inputs:
        data_set ((m,k) ndarray): An array of m k-dimensional points.
        target ((k,) ndarray): A k-dimensional point to compare to 'dataset'.

    Returns:
        ((k,) ndarray) the member of 'data_set' that is nearest to 'target'.
        (float) The distance from the nearest neighbor to 'target'.
    """

    least = None
    a, b = np.shape(data_set)
    for i in xrange(a):
        last = metric(data_set[i],target)
        if least == None:
            point = data_set[i]
            least = last

        elif last < least:
            least = last
            point = data_set[i]

    return least, point

# Problem 3: Write a KDTNode class.
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

class KDTNode(BSTNode):
    """A Node subclass for KDT trees. Contains some data, a
    reference to the parent node, and references to two child nodes.
    """
    def __init__(self, data):
        BSTNode.__init__(self, data)
        if type(data) is not np.ndarray:
            raise ValueError("We can only work with Numpy arrays for now")
        self.axis = 0


# Problem 4: Finish implementing this class by overriding
#            the __init__(), insert(), and remove() methods.

class KDT(BST):

    """A k-dimensional binary search tree object.
    Used to solve the nearest neighbor problem efficiently.

    Attributes:
        root (KDTNode): the root node of the tree. Like all other
            nodes in the tree, the root houses data as a NumPy array.
        k (int): the dimension of the tree (the 'k' of the k-d tree).
    """

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
                raise ValueError(str(data) + " is not in the tree")
            elif np.allclose(data, current.value):
                return current                      # Base case 2: data found!
            elif data[current.axis] < current.value[current.axis]:
                return _step(current.left)          # Recursively search left.
            else:
                return _step(current.right)         # Recursively search right.

        # Start the recursion on the root of the tree.
        return _step(self.root)

    def insert(self, data):
        """Insert a new node containing 'data' at the appropriate location.
        Return the new node. This method should be similar to BST.insert().
        """

        new_node = KDTNode(data)
        kay = len(data)

        if self.root == None:
            self.root = new_node
        else:
            def _adopt(parent, newnode):

                if list(parent.value) == list(new_node.value):                     # Base case 1: Already there.
                    raise ValueError(str(new_node.value) + " is already on the tree")

                if parent.value[parent.axis] < new_node.value[parent.axis]:                # Step to the right.
                    if parent.right is None:
                        parent.right = new_node
                        new_node.prev = parent
                        new_node.axis = ((parent.axis+1)%kay)
                    elif parent.right is not None:
                        _adopt(parent.right, new_node)

                else:                                   # Step to the left.
                    if parent.left is None:
                        parent.left = new_node
                        new_node.prev = parent
                        new_node.axis = ((parent.axis+1)%kay)
                    elif parent.left is not None:
                        _adopt(parent.left, new_node)

            _adopt(self.root, new_node)

    def remove(*args, **kwargs):
            """Disable remove() to keep the tree in balance."""
            raise NotImplementedError("remove() has been disabled for this class.")


# Problem 5
def nearest_neighbor(data_set, target):
    """Use your KDT class to solve the nearest neighbor problem.

    Inputs:
        data_set ((m,k) ndarray): An array of m k-dimensional points.
        target ((k,) ndarray): A k-dimensional point to compare to 'dataset'.

    Returns:
        The point in the tree that is nearest to 'target' ((k,) ndarray).
        The distance from the nearest neighbor to 'target' (float).
    """
    m, k = np.shape(data_set)
    A = KDT()
    for i in xrange(m):
        A.insert(data_set[i])
    distance = metric(A.root.value,target)

    def KDTsearch(current, neighbor, distance):
        """The actual nearest neighbor search algorithm.

        Inputs:
            current (KDTNode): the node to examine.
            neighbor (KDTNode): the current nearest neighbor.
            distance (float): the current minimum distance.

        Returns:
            neighbor (KDTNode): The new nearest neighbor in the tree.
            distance (float): the new minimum distance.
        """
        if current is None:
            return neighbor,distance
        index = current.axis

        if metric(current.value, target) < distance:
            neighbor = current                                          # Update the best estimate.
            distance = metric(current.value, target)

        if target[index] < current.value[index]:                     # Recurse left.
            neighbor, distance = KDTsearch(current.left, neighbor, distance)

            if target[index] + distance >= current.value[index]:
                neighbor, distance = KDTsearch(current.right, neighbor, distance)
        else:                                                        # Recurse right.
            neighbor, distance = KDTsearch(current.right, neighbor, distance)
            if target[index] - distance <= current.value[index]:
                neighbor, distance = KDTsearch(current.left, neighbor, distance)
        return neighbor, distance

    a,b = KDTsearch(A.root, A.root, distance)
    return(a.value,b)



# Problem 6
def postal_problem():
    """Use the neighbors module in sklearn to classify the Postal data set
    provided in 'PostalData.npz'. Classify the testpoints with 'n_neighbors'
    as 1, 4, or 10, and with 'weights' as 'uniform' or 'distance'. For each
    trial print a report indicating how the classifier performs in terms of
    percentage of correct classifications. Which combination gives the most
    correct classifications?

    Your function should print a report similar to the following:
    n_neighbors = 1, weights = 'distance':  0.903
    n_neighbors = 1, weights =  'uniform':  0.903       (...and so on.)
    """
    possibilities = (1,4,10)

    weights = ("distance","uniform")

    labels, points, testlabels, testpoints = np.load('PostalData.npz').items()
    def helper(n, w):
        nbrs = neighbors.KNeighborsClassifier(n_neighbors=n, weights=w, p=2)
        nbrs.fit(points[1], labels[1])
        predictions = nbrs.predict(testpoints[1])
        return np.sum(predictions==testlabels[1])/float(len(predictions))

    for j in ["distance","uniform"]:
        for i in [1,4,10]:
            print "n_neighbors = ", i, "\t" "weights =\t", j, ":  ", helper(i,j)

    #instead of doing np.average(predicitons/testlabels)
    #do np.sum(predictions==testlabels)/float(len(predictions))

    """
if __name__ == "__main__":
    #print metric([1,2,3,1,2,3],[7,5,8,10,2,3])
    #print exhaustive_search(data,[1,2,8])
    #print(str(exhaustive_search(data,[-3,7,4])))

    data = np.array([[-3,7,3],[5,7,9],[4,6,8],[4,6,11],[10,11,15],[10,5,4],[15,2,4],[15,2,2],[-15,20,4],[15,12,1],[15,12,16]])
    print(str(exhaustive_search(data,[-3,7,5])))
    print(str(nearest_neighbor(data,[-3,7,5])))
    tree = KDTree(data)
    min_distance, index = tree.query([-3,7,5])
    print(str(min_distance),str(index))
    print(tree.data[index])

    m, k = np.shape(data)
    A = KDT()
    for i in xrange(m):
        A.insert(data[i])
    print(str(A))


    b = np.array([[3,2,3],[4,5,6],[2,8,9],[11,8,3],[1,8,6]])
    m, k = np.shape(b)
    A = KDT()
    for i in xrange(m):
        A.insert(b[i])
    print(str(A))
    """
