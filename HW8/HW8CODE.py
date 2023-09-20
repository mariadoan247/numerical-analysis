a = [[]]    # global matrix a
b = []      # global vector b


def forward_elimination():
    """
    This is the forward elimination python implementation. It will make use
    of the global variables a and b.
    """
    n = len(a) - 1
    for k in range(n):  # outer-loop to go through matrix
        for i in range(k+1, n+1):  # middle-loop to go through rows
            mult = a[i][k]/a[k][k]
            for j in range(k, n+1):  # inner-loop to update columns
                a[i][j] -= mult*a[k][j]
            b[i] -= mult*b[k]  # update RHS vector


def back_substitution():
    """
    This is the back substitution Python implementation. It will make use
    of the global variables a and b.
    :return: x, the solution of Ax=b
    """
    n = len(a) - 1
    x = [0]*(n+1)
    x[n] = b[n]/a[n][n]
    for i in reversed(range(n)):
        summed = b[i]
        for j in range(i+1, n+1):
            summed -= a[i][j]*x[j]
        x[i] = summed/a[i][i]
    return x


def gaussian_elimination():
    forward_elimination()
    return back_substitution()


if __name__ == '__main__':

    # C2
    a = [[6, -2, 2, 4], [12, -8, 6, 10], [3, -13, 9, 3], [-6, 4, 1, -18]]
    b = [16, 26, -19, -34]
    print(gaussian_elimination())

    # C3
    n = 4  # 4, 5, 6, 7, 8, 9, 10, 11
    a_temp = [[0]*n for i in range(n)]  # substitute into a once initialized
    b_temp = [0]*n                      # substitute into b once initialized
    for i in range(1, n+1):  # fill matrix a
        b_temp[i - 1] = ((1 + i) ** n - 1) / i  # fill vector b
        for j in range(1, n+1):
            a_temp[i-1][j-1] = (i+1)**(j-1)
    a = a_temp
    b = b_temp
    print(f"""
for n = {n} where A equals
{a}
and b equals
{b}
x in Ax=b will equal
{gaussian_elimination()}
""")

    # C4
    n = 15
    a_temp = [[0] * n for i in range(n)]  # substitute into a once initialized
    b_temp = [0] * n  # substitute into b once initialized
    x = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    for i in range(1, n + 1):  # fill matrix a
        for j in range(1, n + 1):
            a_temp[i - 1][j - 1] = -1 + 2*min(i, j)
            b_temp[i - 1] += a_temp[i-1][j-1]*x[j-1]  # fill vector b

    a = a_temp
    b = b_temp
    print(f"""
for n = {n} where A equals
{a}
and b equals
{b}
x in Ax=b will equal
{gaussian_elimination()}
""")
