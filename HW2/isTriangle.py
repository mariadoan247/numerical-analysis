
def is_triangle(x, y, z):
    xy = x + y
    xz = x + z
    yz = y + z
    if (xy >= z and xz >= y and yz >= x and x > 0 and y > 0 and z > 0):
        return True
    else:
        return False

if __name__ == '__main__':
    print(f"is_triangle(1, 2, 3) returns {is_triangle(1, 2, 3)}")
    print(f"is_triangle(0, 0, 0) returns {is_triangle(0, 0, 0)}")
    print(f"is_triangle(1, 4, 9) returns {is_triangle(1, 4, 9)}")
    print(f"is_triangle(1, 1, 1) returns {is_triangle(1, 1, 1)}")
    print(f"is_triangle(-1, 4, 9) returns {is_triangle(-1, 4, 9)}")

