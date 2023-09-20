
def middle(t):

    midList = []

    for i in range(1, len(t) - 1):
        midList.append(t[i])

    return midList

if __name__ == '__main__':
    t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f'middle(t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) returns {middle(t)}')
    t = [1, 2, 3]
    print(f'middle(t = [1, 2, 3]) returns {middle(t)}')
    t = ["one", "two", "three"]
    print(f'middle(t = ["one", "two", "three"]) returns {middle(t)}')


