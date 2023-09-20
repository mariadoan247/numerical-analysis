import numpy as np
from C1 import eulers_method


def function_c2a(x, t):
    return 1 + (t - x)**2


def function_c2b(x, t):
    return t**(-2)*(np.sin(2*t) - 2*t*x)


if __name__ == '__main__':

    # C2a
    print(f"""
The approximate solution for x'=1+(t-x)^2 for
2<=t<=3, x(2)=1, and h=0.05 will be 
{eulers_method(function_c2a, 2, 3, 1, 20)}""")

    # C2b
    print(f"""
The approximate solution for x'=t^(-2)(sin(2t)-2tx) for
1<=t<=2, x(1)=2, and h=0.025 will be 
{eulers_method(function_c2b, 1, 2, 2, 40)}""")
