import numpy as np
from C1 import eulers_method
from C2 import function_c2a, function_c2b


def get_error(actual, approx, a, h, steps):
    errors = np.zeros(steps + 1)

    for i in range(steps + 1):
        errors[i] = abs(actual(a + i*h) - approx[i])

    return errors


def actual_c2a(t):
    return t + 1/(1 - t)


def actual_c2b(t):
    return (4 + np.cos(2) - np.cos(2*t))/(2*t**2)


if __name__ == '__main__':

    # C3a
    approximation = eulers_method(function_c2a, 2, 3, 1, 20)
    print(f"""
The error at each step of the Euler's method
obtained in problem C2a is 
{get_error(actual_c2a, approximation, 2, 0.05, 20)}""")

    # C3b
    approximation = eulers_method(function_c2b, 1, 2, 2, 40)
    print(f"""
The error at each step of the Euler's method
obtained in problem C2b is 
{get_error(actual_c2b, approximation, 1, 0.025, 40)}""")
