# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hello World!, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def absolute_value(x):
    """
        Computes absolute value of x
        input parameters
            x - real number
        outpute parameters
            absolute value of x
    """
    if x >= 0:
        result = x
    else:
        result = -x

    return result

# This takes n-1 operations which is too much
# ((n+1)n)/2 This is 3 operations and gives the same result
def sum_first_n_natural_numbers(n):
    result = 0
    for i in range(1, n):
        result += i
    return result

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Maria Doan')

    y = 5
    print('Absolute value of ', y, ' is ', absolute_value(y))

    y = -4
    print('Absolute value of ', y, ' is ', absolute_value(y))

    m = 5
    print('Sum of the first ', m, ' natural numbers is ', sum_first_n_natural_numbers(m))
    s = ((m + 1)*m)/2
    print(s)

    m = 12
    print('Sum of the first ', m, ' natural numbers is ', sum_first_n_natural_numbers(m))
    s = ((m + 1) * m) / 2
    print(s)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
