import numpy as np


def eulers_method(f, a, b, alpha, steps):
    """
    Euler's method for approximating solution of the
    initial value problem x' = f(x,t) for t in [a,b]
    with x(a) = alpha using n steps
    :param f:  right hand side of the ODE
    :param a:  initial time
    :param b:  final time
    :param alpha:  initial value
    :param steps:  number of steps to reach b
    :return:  approximation of the solution at the mach points
    """

    approximation = np.zeros(steps + 1)
    approximation[0] = alpha
    h = (b - a)/steps
    t = a
    for i in range(steps):
        approximation[i + 1] = approximation[i] + h*f(approximation[i], t)
        t = a + (i + 1)*h
    return approximation

