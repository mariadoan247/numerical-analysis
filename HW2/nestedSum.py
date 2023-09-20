
def nested_sum(t):

    sum = 0

    for i in range(len(t)):
        for j in range(len(t[i])):
            sum += t[i][j]

    return sum

if __name__ == '__main__':
    t = [[1, 4], [3, 8, 3, ], [1], [2, -5]]
    print(f'nested_sum(t = [[1, 4], [3, 8, 3, ], [1], [2, -5]]) returns {nested_sum(t)}')

