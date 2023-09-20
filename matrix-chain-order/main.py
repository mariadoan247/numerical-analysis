import sys


def matrix_chain_order(dim):
    n = len(dim)
    m = [[0 for x in range(n)] for x in range(n)]
    for i in range(1, n):
        m[i][i] = 0
    for l in range(2, n):
        for i in range(1, n-l+1):
            j = i + l - 1
            m[i][j] = 0
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + dim[i-1]*dim[k]*dim[j]
                if q > m[i][j]:
                    m[i][j] = q
    print(m)


if __name__ == '__main__':
    matrix_chain_order([10, 2, 5, 20, 5])
