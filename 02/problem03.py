from math import pi
from math import sin
from math import cos
from math import log
from math import exp


def iRich(f, a, b, e):
    R = []
    h = b - a
    R.append([0.5 * h * ( f( a ) + f( b ) )])
    E = [0]
    
    i = 0
    powerOf2 = 1

    while(True):
        i = i + 1
        
        # Calculamos la mitad del paso en x y usamos este valor para sumar la 
        # función en todos los nuevos puntos (en medio de los puntos ya
        # calculados)
        h = 0.5 * h
        sum = 0.0
        powerOf2 = 2 * powerOf2
        
        for k in range(1, powerOf2, 2):
            sum = sum + f(a + k * h)
        
        # Calculamos la regla compuesta del trapecio para el siguiente
        # nivel de subdivisión. Usamos la regla de Richarson para refinar 
        # estos valores en una forma mas adecuada.
        R.append([])
        R[-1].append(0.5 * R[i-1][0] + sum * h)
        
        # Verificar si el algoritmo fallará
        if i > 2:
            E[i-1] = (R[i-2][0] - R[i-1][0]) / (R[i-1][0] - R[i][0])
            # Hacer la condición explicita
            # if E[i-1]:
            #     break
            
        powerOf4 = 1
        for j in range(1, i + 1):
            powerOf4 = 4 * powerOf4
            R[-1].append(R[i][j-1] + (R[i][j-1] - R[i-1][j-1]) / (powerOf4 - 1))
        
        E.append(0)
            
        if i >= 5 and e >= abs(R[i][i] - R[i-1][i-1]):
            break 
            
    return E, R


def f(x):
    return 1.0 / ((x**2) + 1) + exp(-x) - 2**sin(5*x) + 2


def g(x):
    return log(1+x) - x**2 + abs(cos(x**4))


def main():
    print("f(x) = 1.0 / ((x**2) + 1) + exp(-x) - 2**sin(5*x) + 2")
    print("-----------------------------------------------------")
    print("From  : ", 0);
    print("To    : ", pi);
    print("Pec.  : ", 0.001);
    print("Table : ");
    ef, rf = iRich(f, 0, 2, 0.0001)
    
    for n, (t, row) in enumerate(zip(ef, rf)):
        print("{0:>3d} {1: >11.8f} ".format(n, t), end="")
        for item in row:
            print("{0: >11.8f} ".format(item), end="")
        print()
        
    print()
    print("f(x) = log(1+x) - x**2 + abs(cos(x**4))")
    print("---------------------------------------")
    print("From  : ", 0);
    print("To    : ", 2);
    print("Pec.  : ", 0.001);
    print("Table : ");
    eg, rg = iRich(g, 0, 2, 0.001);
    
    for n, (t, row) in enumerate(zip(ef, rf)):
        print("{0:>3d} {1: >11.8f} ".format(n, t), end="")
        for item in row:
            print("{0: >11.8f} ".format(item), end="")
        print()

if __name__ == '__main__':
    main()