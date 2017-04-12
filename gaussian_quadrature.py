# gaussian_quadrature.py
"""Volume 2 Lab 12: Gaussian Quadrature.
<Name>
<Class>
<Date>

"""
import numpy as np
from matplotlib import pyplot as plt
import scipy as sp
import numpy as np
from scipy import sparse as spr
from math import sqrt
from scipy.stats import norm
from scipy import linalg as la
from scipy.stats import norm

# Problem 1
def shift(f, a, b, plot=False):
    """Shift the function f on [a, b] to a new function g on [-1, 1] such that
    the integral of f from a to b is equal to the integral of g from -1 to 1.

    Inputs:
        f (function): a scalar-valued function on the reals.
        a (int): the left endpoint of the interval of integration.
        b (int): the right endpoint of the interval of integration.
        plot (bool): if True, plot f over [a,b] and g over [-1,1] in separate
            subplots.

    Returns:
        The new, shifted function.
    """
    g = lambda u: f(((b-a)/2.)*u + (a+b)/2.)

    if plot == True:
        domain1 = np.linspace(a,b,100)
        domain2 = np.linspace(-1,1,100)
        plt.suptitle("Artistic Shift", fontsize=20)

        plt.subplot(121)
        plt.plot(domain1,f(domain1), 'b-', lw=1)
        plt.xlabel("x")
        plt.ylabel("f(x)")

        plt.subplot(122)
        plt.plot(domain2,g(domain2), 'r-', lw=1)
        plt.xlabel("x")
        plt.ylabel("g(x)")

        plt.show()
    return g


# Problem 2
def estimate_integral(f, a, b, points, weights):
    """Estimate the value of the integral of the function f over [a,b].

    Inputs:
        f (function): a scalar-valued function on the reals.
        a (int): the left endpoint of the interval of integration.
        b (int): the right endpoint of the interval of integration.
        points ((n,) ndarray): an array of n sample points.
        weights ((n,) ndarray): an array of n weights.

    Returns:
        The approximate integral of f over [a,b].
    """
    g = shift(f,a,b)
    result_ = ((b-a)/2.)*(weights.dot(g(points)))
    return result_


# Problem 3
def construct_jacobi(gamma, alpha, beta):
    """Construct the Jacobi matrix."""
    a = []
    b = []

    for i in xrange(len(gamma)):
        a.append(-float(beta[i])/alpha[i])

        if i < (len(gamma)-1):
            b.append((float(gamma[i+1])/(alpha[i] * alpha[i+1]))**.5)

    jacobi = spr.diags([b,a,b],[-1,0,1])
    return jacobi.toarray()


# Problem 4
def points_and_weights(n):
    """Calculate the points and weights for a quadrature over [a,b] with n
    points.

    Returns:
        points ((n,) ndarray): an array of n sample points.
        weights ((n,) ndarray): an array of n weights.
    """
    gamma = np.zeros(n)
    alpha = np.zeros(n)
    beta = np.zeros(n)
    for i in xrange(1,n+1):
        gamma[i-1] = ((i-1)/float(i))
        alpha[i-1] = ((2.*i-1)/float(i))

    jacobi = construct_jacobi(gamma, alpha, beta)
    x_i, eigvec = la.eigh(jacobi)
    row = eigvec[0,:]
    weights = 2*np.power(row,2)
    return x_i, weights



# Problem 5
def gaussian_quadrature(f, a, b, n):
    """Using the functions from the previous problems, integrate the function
    'f' over the domain [a,b] using 'n' points in the quadrature.
    """
    points, weights = points_and_weights(n)
    result = estimate_integral(f, a, b, points, weights)
    return result


# Problem 6
def normal_cdf(x):
    """Use scipy.integrate.quad() to compute the CDF of the standard normal
    distribution at the point 'x'. That is, compute P(X <= x), where X is a
    normally distributed random variable with mean = 0 and std deviation = 1.
    """
    func = lambda x: np.exp((-x**2)/2)*(1/sqrt(2*np.pi))
    integrado = sp.integrate.quad(func,-np.inf,x)[0]
    return integrado


if __name__ == "__main__":
    print points_and_weights(5)[1]
"""
    f = lambda x: np.cos(x)
    a = -np.pi
    b = np.pi
    s1 = 2 * sqrt(10. / 7.)
    points = np.array([-sqrt(5 + s1) / 3., -sqrt(5 - s1) / 3., 0., sqrt(5 - s1) / 3., sqrt(5 + s1) / 3.])

    s2 = 13 * sqrt(70)
    weights = np.array([(322 - s2) / 900., (322 + s2) / 900., 128 / 225., (322 + s2) / 900., (322 - s2) / 900.])
    print estimate_integral(f,a,b,points,weights)
    print points
    print weights

    f = lambda x: x**2
    a = -5
    b = 5
    shift(f,a,b,plot=True)

    print normal_cdf(1)

    points_and_weights(5)
    s1 = 2 * sqrt(10. / 7.)
    points = np.array([-sqrt(5 + s1) / 3., -sqrt(5 - s1) / 3., 0., sqrt(5 - s1) / 3., sqrt(5 + s1) / 3.])

    s2 = 13 * sqrt(70)
    weights = np.array([(322 - s2) / 900., (322 + s2) / 900., 128 / 225., (322 + s2) / 900., (322 - s2) / 900.])
    weights

    #test problem 5
    a = 0
    b = np.pi
    n = 10
    sin = lambda x: np.sin(x)
    print gaussian_quadrature(sin,a,b,n)


    f = lambda x: x**2
    a = -5
    b = 5



    s2 = 13 * sqrt(70)

    weights = np.array([(322 - s2) / 900., (322 + s2) / 900., 128 / 225., (322 + s2) / 900., (322 - s2) / 900.])
    cos = lambda x: np.cos(x)
    sin = lambda x: np.sin(x)
    print estimate_integral(cos,-np.pi,np.pi,points,weights)
    alpha = np.array([1,1,1,1,1,1])
    beta = 2*np.array([1,1,1,1,1,1])
    gamma = 3*np.array([1,1,1,1,1,1])
    print construct_jacobi(gamma, alpha, beta)
    """
