
t = []
# Don't actually need t as a parameter to make changes, but the problem
# stated that a list must be passed as an argument :)
def chop(t):
    del t[0]
    del t[len(t) - 1]
    return

if __name__ == '__main__':
    t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    chop(t)
    print(f'chop(t) changes t to {t} when t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
    t = [1, 2, 3]
    chop(t)
    print(f'chop(t) changes t to {t} when t = [1, 2, 3]')
    t = ["one", "two", "three"]
    chop(t)
    print(f'chop(t) changes t to {t} when t = ["one", "two", "three"]')


