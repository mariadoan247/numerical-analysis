

def nRangeMin():

    n = 0

    while n < 2**(n/8.0):
        n += 1

    return n

def nRangeMax(n):

    while n > 2**(n/8.0):
        n += 1

    return n


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    min = nRangeMin()
    max = nRangeMax(min)

    print(f"The range of n is {min} < n < {max}")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
