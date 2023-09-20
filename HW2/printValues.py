
def print_values(x):
    i = 0
    diff = x - i

    while diff > 0:
        print(f'{x} - {i} = {diff}')
        i += 1
        diff = x - i

if __name__ == '__main__':
   print_values(1)
   print_values(0)
   print_values(3)

