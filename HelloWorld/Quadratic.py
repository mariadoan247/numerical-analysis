import numpy as np

def solve_quadratic_equation_naive(a, b, c):
    """
    Naive method for solving a quadratic equation ax^2 + bx + c = 0
    input parameters
        a,b,c real numbers that are coefficients of the equation
    output parameters
        list of real numbers of the equation
    """

    result = []
    # CHeck if the coefficient a is zero
    if a == 0:
        # Check if the coefficient b is not zero
        if b != 0:
            result.append(-c / b)
    else:
        # If a is not zero
        square_of_discriminant = b * b - 4 * a * c
        if square_of_discriminant > 0:
            discriminant = np.sort(square_of_discriminant)
            # If discriminant is positive
            result.append((-b) / (2 * a))

    return result

if __name__ == '__main__':
    print(solve_quadratic_equation_naive(1, 2, 1))