
def decreasing_printing(x):

    while x > 0:
        print(x)
        x -= 0.5

    return max

if __name__ == '__main__':

    print(f'decreasing_printing(3) returns')
    decreasing_printing(3)
