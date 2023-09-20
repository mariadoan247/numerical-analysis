
def newts_method(a, Xo):
    Xn = Xo
    Xni = (Xn + a/Xn)/2
    n = 0

    while Xni != Xn:
        Xn = Xni
        n += 1
        Xni = (Xn + a / Xn)/2

    return n, Xn

if __name__ == '__main__':
   print(f'newts_method(2, 6) returns {newts_method(2, 6)}')
   print(f'newts_method(1, 1) returns {newts_method(1, 1)}')

