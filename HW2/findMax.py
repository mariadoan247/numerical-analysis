
def find_maximum(x, y, z):
    max = x

    if max < y:
        max = y
    if max < z:
        max = z

    return max

if __name__ == '__main__':

    print(f'find_maximum(1, 2, 3) returns {find_maximum(1, 2, 3)}')
    print(f'find_maximum(3, 2, 1) returns {find_maximum(3, 2, 1)}')
    print(f'find_maximum(1, 3, 2) returns {find_maximum(1, 3, 2)}')


