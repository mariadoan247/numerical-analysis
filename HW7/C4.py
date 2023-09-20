import math
from C1 import eulers_method
from C3 import get_error


def function_c4(x, t):
    return -x + t + 1


def actual_c4(t):
    return math.exp(-t) + t


if __name__ == '__main__':

    a, b, alpha, h1, h2, h3 = 0, 5, 1, 0.2, 0.1, 0.05
    steps1 = int((b-a)/h1)
    steps2 = int((b-a)/h2)
    steps3 = int((b-a)/h3)

    # C4a
    approx_h1 = eulers_method(function_c4, a, b, alpha, steps1)
    approx_h2 = eulers_method(function_c4, a, b, alpha, steps2)
    approx_h3 = eulers_method(function_c4, a, b, alpha, steps3)

    print(f"""
The approximate solution for x'=-x+t+1 for 0<=t<=5, x(0)=1

with h={h1}  
{approx_h1}

with h={h2}
{approx_h2}

with h={h3}
{approx_h3}""")

    # C4b
    error1 = get_error(actual_c4, approx_h1, 0, h1, steps1)
    error2 = get_error(actual_c4, approx_h2, 0, h2, steps2)
    error3 = get_error(actual_c4, approx_h3, 0, h3, steps3)

    print(f"""
The error in approximation of x(5) for

h={h1}
{error1[steps1 - 1]}

h={h2}
{error2[steps2 - 1]}

h={h3}
{error3[steps3 - 1]}""")
