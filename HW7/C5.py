import numpy as np


def taylor_higher_order(f_derivatives, order, a, b, alpha, steps):
    """
    Fourth order Taylor approximation of an ODE
    :param f_derivatives:  function that provides the derivatives
    of the solution at each value (x,t)
    :param order:  the order the Taylor series will be computed to
    :param a:  initial time
    :param b:  final time
    :param alpha:  initial condition
    :param steps:  number of steps to be used
    :return:
        x_approximation - the approximate values of the problem
    """
    x_approximation = np.zeros(steps + 1)
    h = (b - a)/steps
    x_approximation[0] = alpha
    for i in range(steps):
        t = a + i*h
        derivatives = f_derivatives(x_approximation[i], t, order)
        for n in reversed(range(order)):
            x_approximation[i+1] += derivatives[n]
            x_approximation[i+1] *= h/(n+1)
        x_approximation[i+1] += x_approximation[i]
    return x_approximation


def derivatives_for_ode_a(x, t, order):
    """
    This function returns the first four derivatives of the
    solution x of the ODE x'=1+(t-x)^2 at the point x, t
    :param x:  value of the solution
    :param t:  time
    :param order:  the order the function will be derived to
    :return:  derivatives of the solution x
    """
    derivatives = np.zeros(order)
    derivatives[0] = 1 + (t - x)**2
    derivatives[1] = 2*t - 2*x - 2*t*derivatives[0] + 2*x*derivatives[0]
    if order == 4:
        derivatives[2] = 2 - 4*derivatives[0] - 2*t*derivatives[1] + 2*derivatives[0]**2 + 2*x*derivatives[1]
        derivatives[3] = -6*derivatives[1] - 2*t*derivatives[2] + 6*derivatives[0]*derivatives[1] + 2*x*derivatives[2]
    return derivatives


def derivatives_for_ode_b(x, t, order):
    """
    This function returns the first four derivatives of the
    solution x of the ODE x'=t^-2(sin(2t)-2tx) at the point x, t
    :param x:  value of the solution
    :param t:  time
    :param order:  the order the function will be derived to
    :return:  derivatives of the solution x
    """
    derivatives = np.zeros(order)
    derivatives[0] = t**(-2)*np.sin(2*t) - 2*t**(-1)*x
    derivatives[1] = -2*t**(-3)*np.sin(2*t) + t**(-2)*2*np.cos(2*t) + 2*t**(-2)*x - 2*t**(-1)*derivatives[0]
    if order == 4:
        derivatives[2] = -6*t**(-4)*np.sin(2*t) - 8*t**(-3)*np.cos(2*t) - 4*t**(-2)*np.sin(2*t) - 4*t**(-3)*x \
            + 4*t**(-2)*derivatives[0] - 2*t**(-1)*derivatives[1]
        derivatives[3] = 24*t**(-5)*np.sin(2*t) + 12*t**(-4)*np.cos(2*t) + 24*t**(-3)*np.sin(2*t) \
            - 8*t**(-2)*np.cos(2*t) + 12*t**(-4)*x - 12*t**(-3)*derivatives[0] + 6*t**(-2)*derivatives[1] \
            - 2*t**(-1)*derivatives[2]
    return derivatives


if __name__ == '__main__':
    # C5a
    steps_a = int((3-2)/0.05)
    print(f"""
The approximate solution for x'=1+(t-x)^2 for
2<=t<=3, x(2)=1, and h=0.05 will be 
Second Order Taylor Series Method:
{taylor_higher_order(derivatives_for_ode_a, 2, 2, 3, 1, steps_a)}
Fourth Order Taylor Series Method:
{taylor_higher_order(derivatives_for_ode_a, 4, 2, 3, 1, steps_a)}""")

    # C5b
    steps_b = int((2-1)/0.025)
    print(f"""
The approximate solution for x'=t^(-2)(sin(2t)-2tx) for
1<=t<=2, x(1)=2, and h=0.025 will be 
Second Order Taylor Series Method:
{taylor_higher_order(derivatives_for_ode_b, 2, 1, 2, 2, steps_b)}
Fourth Order Taylor Series Method:
{taylor_higher_order(derivatives_for_ode_b, 4, 1, 2, 2, steps_b)}""")
