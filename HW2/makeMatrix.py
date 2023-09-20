import numpy as np

def make_matrix(m, n):

    size = m*n
    A = np.array([0]*size).reshape(m, n)

    for i in range(m):
        for j in range(n):
            A[i][j] = 2*i + j

    return A

if __name__ == '__main__':

    print(f'make_matrix(4, 3) returns \n {make_matrix(4, 3)}')
