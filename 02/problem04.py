from scipy import matmul

def elimGJ(A, B):
    n = len(A)
    if n != len(A[0]):
        raise ValueError("Matrix A must be square")
        
    if n != len(B):
        raise ValueError("Matrix A and B are not compatible")
    
    try:
        bVectors = list(map(list, zip(*B)))
    except:
        bVectors = [B]
        
    xVectors = []
    
    for b in bVectors:
        m = [[A[i][j] for j in range(n)] for i in range(n)]
        
        for rowH, bItem in zip(m,b):
            rowH.append(bItem)
    
        h, w = len(m), len(m[0])
        
        for y in range(h):
            # Eliminamos la columna Y
            for y2 in range(y + 1, h):
                c = m[y2][y] / m[y][y]
                for x in range(y, w):
                    m[y2][x] -= m[y][x] * c
        for y in range(h-1, 0-1, -1): # Backsubstitute
            c    = m[y][y]
            for y2 in range(0,y):
                for x in range(w-1, y-1, -1):
                    m[y2][x] -=    m[y][x] * m[y2][y] / c
            m[y][y] /= c
            for x in range(h, w):             # Normalize row y
                m[y][x] /= c
        
        xVectors.append([])
        
        for row in m:
            xVectors[-1].append(row[-1]);
            
    if len(xVectors) == 1:
        return xVectors[0]
    
    return list(map(list, zip(*xVectors)))


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


def printVector(M, vector_name='M'):
    m = len(M)
    
    print("{0} = [".format(vector_name))
    for i in range(m):
        print("{0:11.6f}".format(M[i]))
    print("]")


def main():
    A = [
        [1.0,2.0,4.0],
        [1.0,3.0,0.0],
        [1.0,5.0,5.0]
    ]

    B = [
        [5.0, 8.0],
        [1.0, 2.0],
        [3.0, 3.0]
    ]

    X1, X2 = zip(*elimGJ(A,B))

    printMatrix(A, 'A')
    printMatrix(B, 'B')
    printVector(X1, 'X1')
    printVector(X2, 'X2')
    printVector(matmul(A, X1), 'A * X1')
    printVector(matmul(A, X2), 'A * X2')
    print("------------------------------")

    A = [
        [1., 2., 3.],
        [4., 5., 6.],
        [1., 0., 1.]
    ]

    B = [1., 1., 1.]

    X = elimGJ(A,B)

    printMatrix(A, 'A')
    printVector(B, 'B')
    printVector(X, 'X')
    printVector(matmul(A, X), 'A * X')
    

if __name__ == '__main__':
    main()