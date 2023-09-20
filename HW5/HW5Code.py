import math
import mpmath
import numpy as np


def newtons_method(f, df, x, n_max, epsilon, delta):
    fx = f(x)

    print(f'0, {x}, {fx}')

    for n in range(1, n_max + 1):
        fdx = df(x)

        if abs(fdx) < delta:
            print("Small derivative")
            return

        h = fx/fdx

        # Refinements for c6
        # fx_h = f(x - h)
        # if abs(fx_h) >= abs(fx):
        #     h = h/2

        x = x - h
        fx = f(x)

        print(f'{n}, {x}, {fx}')

        if abs(h) < epsilon:
            print("Converges")
            return

    print("Does not converge")

    return


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


def f_c1(x):
    return x**5 - 9*x**4 - x**3 + 17*x**2 - 8*x - 8


def df_c1(x):
    return 5*x**4 - 36*x**3 - 3*x**2 + 34*x - 8


def f_c2(x):
    return x - math.tan(x)


def df_c2(x):
    return 1 - mpmath.sec(x)**2


def f_c3(x):
    return x**4 + 2*x**3 - 7*x**2 + 3


def df_c3(x):
    return 4*x**3 + 6*x**2 - 14*x


def f_c4(x):
    return x**2 - 2*x + 1


def df_c4(x):
    return 2*x - 2


def f_c5(x):
    return math.cos(x) - math.e**(-x**2) + 1


def df_c5(x):
    return -math.sin(x) + 2*x*math.e**(-x**2)


def f_c6(x):
    return math.sin(x)


def df_c6(x):
    return math.cos(x)


if __name__ == '__main__':

    # Problem c1
    print("\nProblem c1:")
    newtons_method(f_c1, df_c1, 0.0, 10, 0.001, 0.001)

    # Problem c2
    print("\nProblem c2:")
    newtons_method(f_c2, df_c2, 98.95, 10, 0.001, 0.001)
    print(bisection(f_c2, 98.94, 98.96, 10, 0.001))

    # Problem c3
    print("\nProblem c3:")
    newtons_method(f_c3, df_c3, 1.0, 10, 0.00001, 0.001)
    newtons_method(f_c3, df_c3, 2.0, 10, 0.00001, 0.001)

    # Problem c4
    print("\nProblem c4:")
    newtons_method(f_c4, df_c4, 1.1, 10, 0.001, 0.01)
    newtons_method(f_c4, df_c4, 1.1, 10, 0.001, 0.001)
    newtons_method(f_c4, df_c4, 1.1, 10, 0.00001, 0.00001)

    # Problem c5
    print("\nProblem c5:")
    newtons_method(f_c5, df_c5, 0, 10, 0.001, 0.001)
    newtons_method(f_c5, df_c5, 1, 20, 0.001, 0.001)

    # Problem c6
    print("\nProblem c6:")
    newtons_method(f_c6, df_c6, math.pi/4, 10, 0.001, 0.001)
