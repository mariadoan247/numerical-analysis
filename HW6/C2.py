import math


# Problem C2
def ln_taylor(x, n):
    t = x
    s = t
    for k in range(n):
        t *= -x/(k+2)
        s += t
    return s


if __name__ == '__main__':
    # Problem C2
    x = 10  # 0.01, 0.1, 1, 10
    n = 100  # 5, 10, 20, 50, 100
    print(f"""
For x = {x} and n = {n},
T_{n}({x}) = {ln_taylor(x, n)} and ln(1+{x}) = {math.log(1 + x, math.e)}""")
