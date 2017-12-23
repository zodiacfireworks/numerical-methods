import sys

from random import random
from scipy import matmul


def descompLU(A, b):
    """Realiza la descomposición LU
    
    El parametro b no es utulizado.
    """
    # Obtenemos el numero de filas
    n = len(A)

    # Llenamos la diagonal de la matriz L con 1
    L = [[0 if i!=j else 1 for j in range(n)] for i in range(n)]
    
    # Igualamos U a la matriz A
    # No copiamos directamente con U = A por que cualquier alteracion
    # en U tambien alterará las componentes de A
    U = [[A[i][j] for j in range(n)] for i in range(n)]
    
    for i in range(0, n):
        # Para cada fila i, accedemos a la columna i+1 hasta el final
        # y dividimos por el coefiente diagonal A(k ,k)
        for k in range(i+1, n):
            L[k][i] = U[k][i] / U[i][i]
            
            # Para cada fila desde i+i hasta el final, realizamos
            # eliminacion Gausiana. Al final preservaremos solo 
            # la diagonal superior de A.
            for l in range(i+1, n):
                U[k][l] = U[k][l] - L[k][i] * U[i][l]
                
    U = [[U[i][j] if i<=j else 0 for j in range(n)] for i in range(n)]
    
    return L, U


def printMatrix(M, matrix_name='M'):
    m = len(M)
    n = len(M[0])
    
    print("{0} = [".format(matrix_name))
    for i in range(m):
        print("    [", end='')
        for j in range(n):
            print("{0:11.6f}".format(M[i][j]), end='')
        print("]")
    print("]")


def main(n = 3):
    A = [[20*random() for j in range(n)] for i in range(n)]
    b = [20*random() for i in range(n)]

    L, U = descompLU(A, b)

    printMatrix(A, 'A')
    print()
    printMatrix(L, 'L')
    print()
    printMatrix(U, 'U')
    print()
    printMatrix(matmul(L, U), 'LU')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
        main(n)
    else:
        main()
