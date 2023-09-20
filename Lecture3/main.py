# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def evaluate_polynomial(coef, order, x):
    """
    Evaluates the value of a polynomial at x
    :param coef: coefficients of the polynomial
    :param order: order of the polynomial
    :param x: point at which the polynomial is evaluated
    :return: value of the polynomial at x
    """

    result = coef[order]
    for i in reversed(range(0, order)):
        result = coef... #More later in the pdf

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    evaluate_polynomial(1,1,1)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
