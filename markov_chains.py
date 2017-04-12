# markov_chains.py
"""Volume II: Markov Chains.
<Name>
<Class>
<Date>
"""

import numpy as np
from numpy import random as rand
from numpy import linalg as la


# Problem 1
def random_markov(n):
    """Create and return a transition matrix for a random Markov chain with
    'n' states. This should be stored as an nxn NumPy array.
    """
    A = 10*rand.random((n, n))
    S = np.sum(A,axis=0)
    for i in xrange(n):
        for j in xrange(n):
            A[i,j] = A[i, j] / float(S[j])
    return A

# Problem 2
def forecast(days):
    """Forecast tomorrow's weather given that today is hot."""
    transition = np.array([[0.7, 0.6], [0.3, 0.4]])
    day_weather = []
    day_weather.append(rand.binomial(1, transition[1, 0]))
    for i in xrange(days-1):
        day_weather.append(rand.binomial(1, transition[1, day_weather[i]]))

    return day_weather


# Problem 3
def four_state_forecast(days):
    """Run a simulation for the weather over the specified number of days,
    with mild as the starting state, using the four-state Markov chain.
    Return a list containing the day-by-day results, not including the
    starting day.

    Examples:
        >>> four_state_forecast(3)
        [0, 1, 3]
        >>> four_state_forecast(5)
        [2, 1, 2, 1, 1]
    """
    day_weather = []
    transition = np.array([[0.5, 0.3, 0.1, 0], [0.3, 0.3, 0.3, 0.3], [0.2, 0.3, 0.4, 0.5], [0, 0.1, 0.2, 0.2]])
    fut_ind = list(rand.multinomial(1, transition[:,1]))
    for i in xrange(days):
        day_weather.append(fut_ind.index(1))
        fut_ind = list(rand.multinomial(1, transition[:,day_weather[i]]))
    return day_weather

# Problem 4
def steady_state(A, tol=1e-12, N=40):
    """Compute the steady state of the transition matrix A.

    Inputs:
        A ((n,n) ndarray): A column-stochastic transition matrix.
        tol (float): The convergence tolerance.
        N (int): The maximum number of iterations to compute.

    Raises:
        ValueError: if the iteration does not converge within N steps.

    Returns:
        x ((n,) ndarray): The steady state distribution vector of A.

    """
    n,m = np.shape(A)
    rand_state = np.random.rand(n,1)
    S = np.sum(rand_state)
    for j in xrange(n):
        rand_state[j] = rand_state[j] / float(S)
    error = tol + 1
    while error > tol:
        if N > 0:
            N-1
            x_new = A.dot(rand_state)
            error = la.norm(x_new - rand_state)
            rand_state = x_new
        else:
            raise ValueError("it does not want to get close enough")

    return rand_state


# Problems 5 and 6
class SentenceGenerator(object):
    """Markov chain creator for simulating bad English.

    Attributes:
        (what attributes do you need to keep track of?)

    Example:
        >>> yoda = SentenceGenerator("Yoda.txt")
        >>> print yoda.babble()
        The dark side of loss is a path as one with you.
    """

    def __init__(self, filename):
        """Read the specified file and build a transition matrix from its
        contents. You may assume that the file has one complete sentence
        written on each line.
        """
        words = []
        with open(filename,'r') as readingfile:
            self.contents = []
            lines = readingfile.read().split("\n")
            for line in lines:
                words += line.split()
            words_uni = ["start"]

            for word in words:
                if word not in words_uni:
                    words_uni.append(word)

            words_uni.append("stop")

            n = len(words_uni)

            indices = [x for x in xrange(n)]
            matriz = np.zeros((n,n))

            for line in lines:
                this_sentence = line.split()

                for i in xrange(len(this_sentence)):
                    word_ind = words_uni.index(this_sentence[i])
                    if i != (len(this_sentence)-1):
                        wordplus_ind = words_uni.index(this_sentence[i+1])

                    if i == 0:
                        matriz[word_ind][0] += 1
                        matriz[wordplus_ind][word_ind] += 1

                    elif i == (len(this_sentence)-1):
                        matriz[n-1][word_ind] += 1

                    elif  0 < i < (len(this_sentence)-1):
                        matriz[wordplus_ind][word_ind] += 1
                matriz[n-1][n-1] += 1
            S = np.sum(matriz,axis=0)
            for i in xrange(n):
                for j in xrange(n):
                    if float(S[j]) != 0:
                        matriz[i,j] = matriz[i, j] / float(S[j])
        self.matrix = matriz
        self.reference = words_uni


    def babble(self):
        """
        Begin at the start state and use the strategy from
        four_state_forecast() to transition through the Markov chain.
        Keep track of the path through the chain and the corresponding words.
        When the stop state is reached, stop transitioning and terminate the
        sentence. Return the resulting sentence as a single string.
        """
        word_index = []
        sentence = []
        transition = self.matrix
        fut_ind = list(rand.multinomial(1, transition[:,0]))
        i = 0
        while fut_ind.index(1) !=  (len(self.reference)-1):
            word_index.append(fut_ind.index(1))
            sentence.append(self.reference[fut_ind.index(1)])
            fut_ind = list(rand.multinomial(1, transition[:,word_index[i]]))
            i += 1
        line = ' '.join(sentence)
        return line




if __name__ == "__main__":
    """

    A = random_markov(4)
    print steady_state(A)
    print four_state_forecast(5)
    """
    swift = SentenceGenerator("yoda.txt")
    for _ in xrange(50):
        print(swift.babble())
