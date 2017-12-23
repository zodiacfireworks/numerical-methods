from math import pi
from math import sin
from math import ceil
from matplotlib import pylab


def dRich(f, x, s, n, h):
    # Llenamos la matriz de extrapolacion con ceros
    D = [[0 for j in range(n+1)] for i in range(n+1)]

    # Llenamos la primera columna con las formulas 
    # de diferencias centrales
    for i in range(n+1):
        D[i][0] = (f(x + h) - 2 * f(x) + f(x-h)) / (h**2)
        
        if s == 'central':
            powerOf4 = 1
            
            for j in range(1, i+1):
                powerOf4 = 4 * powerOf4
                D[i][j] = D[i][j-1] + ( D[i][j-1] - D[i-1][j-1] ) / ( powerOf4 - 1 )

        elif s == 'forward':
            powerOf2 = 1

            for j in range(1, i+1):
                powerOf2 = 2 * powerOf2
                D[i][j] = D[i][j-1] + ( D[i][j-1] - D[i-1][j-1] ) / ( powerOf2 - 1 )
        else:
            raise(ValueError("Value of `s' parameter must be one of `cental' or `forward'"))
        h = 0.5 * h

    return D[n][n]


def f(x):
    s = sin(x)  
    return s - s**2 + s**3


def main():
    m = 3001
    Xmin = 0
    Xmax = 5*pi
    Xstep = (Xmax - Xmin) / (m - 1)
    X = [Xmin + i*Xstep for i in range(0, m)]
    Y = [f(x) for x in X]

    n = 10
    h = Xstep

    s = 'central'
    DC2Y = [dRich(f, x, s, n, Xstep) for x in X]

    s = 'forward'
    DF2Y = [dRich(f, x, s, n, Xstep) for x in X]

    pylab.figure(figsize=(7,7))
    pylab.plot(X,DC2Y, 'g--', label='Richardson Second Derivative (Central Scheme)')
    pylab.plot(X,DF2Y, 'r--', label='Richardson Second Derivative (Forward Scheme)')
    pylab.plot(X,Y, 'b-', label='f(x) = sin(x) - sin(x)^2 + sin(x)^3')
    pylab.gca().set_aspect('equal', 'datalim')
    pylab.xlabel('x')
    pylab.xlim([0,ceil(Xmax)])
    pylab.ylabel('y')
    pylab.ylim([-4,8])
    pylab.legend()
    pylab.grid()
    pylab.show()


if __name__ == '__main__':
    main()