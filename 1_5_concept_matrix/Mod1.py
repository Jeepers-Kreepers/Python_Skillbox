import sympy as sp

A = sp.Matrix([[3, 1], [-5, 2]])
B = sp.Matrix([[-2, 1], [3, 4]])

D = sp.Matrix([[1, 2, 0], [3, 45, 6]])
E = sp.Matrix([7, 8, 0])




if __name__ == '__main__':
    print(A * B)
    print(2*A - 3*B + sp.eye(2))
    print(D)
    print(E)
    print(D * E)