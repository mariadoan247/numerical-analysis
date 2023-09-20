import math


# Problem C1
def e_taylor(x, n):
    t = 1
    s = t
    for k in range(n):
        t *= x/(k+1)
        s += t
    return s


if __name__ == '__main__':
    # Problem C1
    x = 10  # 0.1, 1, 10
    n = 100    # 5, 10, 20, 50, 100
    print(f"""
For x = {x} and n = {n},
T_{n}({x}) = {e_taylor(x, n)} and e^{x} = {math.exp(x)}""")
