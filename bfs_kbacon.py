# bfs_kbacon.py
"""Volume 2A: Breadth-First Search (Kevin Bacon).
<Juan>
<345>
<Today>
"""

from collections import deque
import networkx as nx
from matplotlib import pyplot as plt


# Problems 1-4: Implement the following class
class Graph(object):
    """A graph object, stored as an adjacency dictionary. Each node in the
    graph is a key in the dictionary. The value of each key is a list of the
    corresponding node's neighbors.

    Attributes:
        dictionary: the adjacency list of the graph.
    """

    def __init__(self, adjacency):
        """Store the adjacency dictionary as a class attribute."""
        self.dictionary = adjacency

    # Problem 1
    def __str__(self):
        """String representation: a sorted view of the adjacency dictionary.

        Example:
            >>> test = {'A':['B'], 'B':['A', 'C',], 'C':['B']}
            >>> print(Graph(test))
            A: B
            B: A; C
            C: B
        """
        total = list()
        for i in xrange(len(self.dictionary)):
            letters = str()
            self.dictionary[self.dictionary.keys()[i]].sort()
            for j in xrange(len(self.dictionary[self.dictionary.keys()[i]])):
                if j == 0:
                    letters += str(self.dictionary[str(self.dictionary.keys()[i])][j])
                else:
                    letters += "; " + str(self.dictionary[str(self.dictionary.keys()[i])][j])
            total.append(str(str(self.dictionary.keys()[i]) + ": " + letters))
        total.sort()
        return '\n'.join(total)

    # Problem 2
    def traverse(self, start):
        """Begin at 'start' and perform a breadth-first search until all
        nodes in the graph have been visited. Return a list of values,
        in the order that they were visited.

        Inputs:
            start: the node to start the search at.

        Returns:
            the list of visited nodes (in order of visitation).

        Raises:
            ValueError: if 'start' is not in the adjacency dictionary.

        Example:
            >>> test = {'A':['B'], 'B':['A', 'C',], 'C':['B']}
            >>> Graph(test).traverse('B')
            ['B', 'A', 'C']
        """
        if start not in self.dictionary:
            raise ValueError("That is not in the adjacency")
        current = start

        marked = set()
        visited = list()
        visit_queue = deque()

        adjacency_dictionary = self.dictionary
        marked.add(current)

        for n in xrange(len(self.dictionary)-1):
            for neighbor in adjacency_dictionary[current]:
                if neighbor not in marked:
                    visit_queue.append(neighbor)
                    marked.add(neighbor)
            # print current
            visited.append(current)
            current = visit_queue.popleft()
            n -= 1
        visited.append(current)

        return (visited)


    # Problem 3 (Optional)
    def DFS(self, start):
        """Begin at 'start' and perform a depth-first search until all
        nodes in the graph have been visited. Return a list of values,
        in the order that they were visited. If 'start' is not in the
        adjacency dictionary, raise a ValueError.

        Inputs:
            start: the node to start the search at.

        Returns:
            the list of visited nodes (in order of visitation)
        """
        raise NotImplementedError("Problem 3 Incomplete")

    # Problem 4
    def shortest_path(self, start, target):
        """Begin at the node containing 'start' and perform a breadth-first
        search until the node containing 'target' is found. Return a list
        containg the shortest path from 'start' to 'target'. If either of
        the inputs are not in the adjacency graph, raise a ValueError.

        Inputs:
            start: the node to start the search at.
            target: the node to search for.

        Returns:
            A list of nodes along the shortest path from start to target,
                including the endpoints.

        Example:
            >>> test = {'A':['B', 'F'], 'B':['A', 'C'], 'C':['B', 'D'],
            ...         'D':['C', 'E'], 'E':['D', 'F'], 'F':['A', 'E', 'G'],
            ...         'G':['A', 'F']}
            >>> Graph(test).shortest_path('A', 'G')
            ['A', 'F', 'G']
        """
        if start not in self.dictionary:
            raise ValueError(start, "is not in the adjacency")

        if target not in self.dictionary:
            raise ValueError(target," is not in the adjacency")

        current = start

        new_dict = dict()

        marked = set()
        visited = list()
        visit_queue = deque()

        adjacency_dictionary = self.dictionary
        marked.add(current)
        while current != target:
            for neighbor in adjacency_dictionary[current]:
                if neighbor not in marked:
                    visit_queue.append(neighbor)
                    new_dict[neighbor] = current
                    marked.add(neighbor)
            # print current
            visited.append(current)
            current = visit_queue.popleft()

        visited.append(current)

        #path
        last = target
        path = []
        while last != start:
            path.append(last)
            last = new_dict[last]
        path.append(start)
        path.reverse()
        return path

# Problem 5: Write the following function
def convert_to_networkx(dictionary):
    """Convert 'dictionary' to a networkX object and return it."""
    nx_graph = nx.Graph()
    for x in dictionary.keys():
        for y in dictionary[x]:
            nx_graph.add_edge(x, y)

    return nx_graph


# Helper function for problem 6
def parse(filename="movieData.txt"):
    """Generate an adjacency dictionary where each key is
    a movie and each value is a list of actors in the movie.
    """

    # open the file, read it in, and split the text by '\n'
    with open(filename, 'r') as movieFile:
        moviesList = movieFile.read().split('\n')
    graph = dict()

    # for each movie in the file,
    for movie in moviesList:
        # get movie name and list of actors
        names = movie.split('/')
        title = names[0]
        graph[title] = []
        # add the actors to the dictionary
        for actor in names[1:]:
            graph[title].append(actor)

    return graph


# Problems 6-8: Implement the following class
class BaconSolver(object):
    """Class for solving the Kevin Bacon problem."""

    # Problem 6
    def __init__(self, filename="movieData.txt"):
        """Initialize the networkX graph and with data from the specified
        file. Store the graph as a class attribute. Also store the collection
        of actors in the file as an attribute.
        """
        actores = set()
        self.filename = filename
        dictionary = parse(filename)
        for x in dictionary.keys():
            for y in dictionary[x]:
                actores.add(y)
        self.actors = actores
        self.graph = convert_to_networkx(dictionary)


    # Problem 6
    def path_to_bacon(self, start, target="Bacon, Kevin"):
        """Find the shortest path from 'start' to 'target'."""
        if start not in self.actors:
            raise ValueError(start, "sucks and is not a friend of Kevin")
        if target not in self.actors:
            raise ValueError("Coder: you should have stayed with Kevin")

        return nx.shortest_path(self.graph, start, target)


    # Problem 7
    def bacon_number(self, start, target="Bacon, Kevin"):
        """Return the Bacon number of 'start'."""
        number = (len(nx.shortest_path(self.graph, start, target))-1)/2.
        return number

    # Problem 7
    def average_bacon(self, target="Bacon, Kevin"):
        """Calculate the average Bacon number in the data set.
        Note that actors are not guaranteed to be connected to the target.

        Inputs:
            target (str): the node to search the graph for
        """
        number = 0
        not_friends = 0
        for actor in self.actors:
            try :
                number += self.bacon_number(actor, target)
            except :
                not_friends += 1

        average = number/float(len(self.actors)-not_friends)
        return average, not_friends


# =========================== END OF FILE =============================== #

"""
if __name__ == "__main__":
    #prob1
    test = {'F':['G', 'E', 'A'],'B':['A', 'Z', 'C'], 'C':['T', 'R', 'B', 'D'],'D':['C', 'E'], 'A':['B', 'F'],  'E':['D', 'F'],
     'G':['A', 'F']}
    graph = Graph(test)
    #print graph

    #prob2
    test = {'A':['B', 'C', 'D', 'E'], 'B':['A', 'C'],
'C':['B', 'A', 'D'], 'D':['A', 'C'], 'E':['A']}
    #print Graph(test).traverse('B')

    #prob3
    Graph(test).shortest_path("D", "D")

    #prob4
    convert_to_networkx(test)

    #prob5
    movie_graph = BaconSolver("movieData.txt")
    movie_graph.path_to_bacon('Stark, Peter')
    movie_graph.bacon_number('Stark, Peter')
    movie_graph.average_bacon()

    my_dictionary = {'A':['C', 'B'], 'C':['A'], 'B':['A']}
    graph = Graph(my_dictionary)
    print(graph)
    print
    test =  {'A':['B', 'C', 'D', 'E'], 'B':['A', 'C'],
'C':['B', 'A', 'D'], 'D':['A', 'C'], 'E':['A']}
    print Graph(test).traverse('D')
    print


    test = {'A':['B', 'F'], 'B':['A', 'C'], 'C':['B', 'D'],'D':['C', 'E'], 'E':['D', 'F'], 'F':['A', 'E', 'G'],'G':['A', 'F']}
    print Graph(test).shortest_path('A','G')


    bacon = BaconSolver()

    movie_graph = BaconSolver("movieData.txt")
    print(movie_graph.path_to_bacon("Lee, Reggie"))
    print(movie_graph.bacon_number("Lee, Reggie"))
    print(movie_graph.average_bacon())

"""
