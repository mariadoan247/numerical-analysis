
def check_format(a, b, c, n):
    anbn = a**n + b**n
    cn = c**n
    if n <= 2:
        return
    elif anbn != cn:
        return True
    elif anbn == cn:
        return False

if __name__ == '__main__':
    print(f"check_format(1, 2, 3, 1) returns {check_format(1, 2, 3, 1)}")
    print(f"check_format(1, 2, 3, 2) returns {check_format(1, 2, 3, 2)}")
    print(f"check_format(1, 2, 3, 3) returns {check_format(1, 2, 3, 3)}")
    print(f"check_format(0, 0, 0, 3) returns {check_format(0, 0, 0, 3)}")


