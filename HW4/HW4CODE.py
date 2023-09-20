import numpy as np
import math
from decimal import Decimal

# Problem C1
def c1(x, n):
    '''
    This function will compute f(x) = x-sin(x) based on the Taylor
    series expansion to achieve better accuracy
    :param x: A number to be plugged into the function f(x)
    :param n: The number of times to expand the Taylor series
    :return: The results of the computation
    '''

    # Initialize a variable to hold the result of the expansion
    result = 0

    # Continue to expand n-times
    for i in range(1, n+1):
        numerator = Decimal((-1)**(i+1)*(x**(2*i+1)))
        denominator = Decimal(math.factorial(2*i+1))
        result += numerator/denominator

    return result


# Problem C2
def c2(x, n):
    '''
    This function will compute f(x) = e^x-e^(-2x) based on the
    Taylor series expansion
    :param x: A number to be plugged into the function f(x)
    :param n: The number of times to expand the Taylor series
    :return: The results of the computation
    '''

    # Initialize a variable to hold the result of e^x
    ex = 0
    # Initialize a variable to hold the result of e^(-2x)
    e2x = 0

    # Compute e^x
    for i in range(n):
        numerator = Decimal(x**i)
        denominator = Decimal(math.factorial(i))
        ex += numerator/denominator

    # Compute e^(-2x)
    for j in range(n):
        numerator = Decimal((-2*x)**j)
        denominator = Decimal(math.factorial(j))
        e2x += numerator/denominator

    return ex-e2x


# Problem C3
def c3(x):
    '''
    This function will compute f(x) = (x-sin(x))/x^3 based on
    the Taylor series expansion to achieve better accuracy
    :param x: A number to be plugged into the function f(x)
    :return: The results of the computation
    '''

    # Initialize a variable to hold the result of the expansion
    result = 0

    # Continue to expand n-times
    for i in range(100):
        numerator = Decimal((-1)**i*(x**(2*i)))
        denominator = Decimal(math.factorial(2*i+3))
        result += numerator / denominator

    return result


# Problem C4-C7
def bisection(f, a, b, max_iter, tolerance):
    """
    Approximates a root r in [a,b] of the function f with error smaller
    than a given tolerance
    Note that f(a)f(B) has to be negative for this method to work
    :param f: function whose root is to be found
    :param a: left bound on the position of the root
    :param b: right bound on the position of the root
    :param max_iter: maximum number of iterations to reach the tolerance
    :param tolerance: maximal allowed error
    :return: converged - flag indicating if the method reached the precision
             root - approximation of the root
    """

    fa = f(a)
    fb = f(b)

    if np.sign(fa) == np.sign(fb):
        return False, 0

    error = b-a
    for n in np.arange(max_iter):
        error /= 2
        c = a + error
        fc = f(c)
        print('n = ', n, 'c = ', c, 'f(c) = ', fc)

        if fc == 0:
            return True, c
        if error < tolerance:
            return True, c
        if np.sign(fa) == np.sign(fc):
            a = c
            fa = fc

    return False, c


# Problem C5
def intersection(x):
    return x**3 - x + 1


# Problem C6
def c6(x):
    return 9*x**4 + 18*x**3 + 38*x**2 - 57*x + 14


# Problem C7
def tan_minus_x(x):
    return np.tan(x) - x


if __name__ == '__main__':

    # Problem C1
    n = 10
    # n = 100
    x = 0.01
    # x = 1
    # x = 100
    print(f"For n = {n}\n"
          f"if x = {x},\n"
          f"with the Taylor series expansion x-sin(x)={c1(x,n)}\n"
          f"without the Taylor series expansion x-sin(x)={x-np.sin(x)}\n\n")

    # Problem C2
    n = 2
    # n = 10
    # n = 100
    x = 0.001
    print(f"For n = {n}\n"
          f"if x = {x}, then\n"
          f"with the Taylor series expansion e^x-e^(-2x)={c2(x,n)}\n"
          f"without the Taylor series expansion e^x-e^(-2x)={np.exp(x)-np.exp(-2*x)}\n\n")

    # Problem C3
    n = 16
    x = 10**(-n)
    print(f"For n = {n}\n"
          f"if x = 10^(-n), then\n"
          f"with the Taylor series expansion (x-sin(x))/x^3={c3(x)}\n"
          f"without the Taylor series expansion (x-sin(x))/x^3={(x-np.sin(x))/(x**3)}\n\n")

    # Problem C4
    print(bisection(tan_minus_x, -1, 1, 100, 0.001))

    # Problem C5
    print(bisection(intersection, -1.5, -1, 100, 0.00001))

    # Problem C6
    print(bisection(c6, 0, 0.5, 100, 0.00001))

    # Problem C7
    print(bisection(tan_minus_x, 4, 5, 100, 0.001))
    print(bisection(tan_minus_x, 1, 2, 100, 0.001))
