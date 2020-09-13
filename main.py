# Librerías usadas

import numpy
import math


# ========================
#  Aproximación discreta
# ========================

# Funciones (cambian con cada ejercicio)

f1_expresion = 'ln(x)'
f2_expresion = 'e^(-x)'

# Cálculo de cada una

def calc_f1(x):
    return math.log(x)


def calc_f2(x):
    return math.exp(x * (-1))


# Valores de Entrada

x = [1.00, 1.20, 1.40, 1.60, 1.80]

y = [0.242, 0.1942, 0.1497, 0.1109, 0.079]

# Para c/ función se recorre la x correspondiente a los valores de entrada

f1 = []

for k in x:
    f1.append(calc_f1(k))

f2 = []

for k in x:
    f2.append(calc_f2(k))

# Se muestran dichos resultados

print('Valores de Entrada')
print()
print("x: %s" % str(x))
print("y: %s" % str(y))
print("f1: %s" % str(f1))
print("f2: %s" % str(f2))
print()
print()

# Cáculo de las Matrices A, B y C

f1_f2 = 0
f1_f1 = 0
f2_f2 = 0

f_f1 = 0
f_f2 = 0

for k in range(5):
    f1_f1 = f1_f1 + (f1[k] * f1[k])
    f2_f2 = f2_f2 + (f2[k] * f2[k])
    f1_f2 = f1_f2 + (f1[k] * f2[k])

    f_f1 = f_f1 + (y[k] * f1[k])
    f_f2 = f_f2 + (y[k] * f2[k])

print('Productos Escalares:')
print("<f1,f1>: %f" % f1_f1)
print("<f2,f2>: %f" % f2_f2)
print("<f1,f2>: %f" % f1_f2)
print("<f,f1>: %f" % f_f1)
print("<f,f2>: %f" % f_f2)

A = [
    [f1_f1, f1_f2],
    [f1_f2, f2_f2]
]

print()
print("Matriz A: %s" % str(A))
print()

B = [f_f1, f_f2]

print()
print("Matriz B: %s" % str(B))
print()

C = [0, 0]

A_inv = numpy.linalg.inv(A)

print()
print("Matriz A-1: %s" % str(A_inv))
print()

C[0] = (A_inv[0][0] * B[0]) + (A_inv[0][1] * B[1])
C[1] = (A_inv[1][0] * B[0]) + (A_inv[1][1] * B[1])

print()
print("Matriz C: %s" % str(C))
print()

print("y = %f %s + %f %s" % (C[0], f1_expresion, C[1], f2_expresion))
print(
    "Es la función que mejor representa a los datos respecto del subespacio dado, por el método de los mínimos cuadrados."
)
print()

# Según los valores que me den para calcular cambia el resultado

x1 = 1.30
f_x1 = (C[0] * calc_f1(x1)) + (C[1] * calc_f2(x1))

print("f(%f) = %f" % (x1, f_x1))

x2 = 2.00
f_x2 = (C[0] * calc_f1(x2)) + (C[1] * calc_f2(x2))

print("f(%f) = %f" % (x2, f_x2))

# Cálculo del Error del Método

print("Cálculo del Error del Método")

sumatoria_raiz = 0

for k in range(5):
    sumatoria_raiz = sumatoria_raiz + (y[k] * y[k])

error = math.sqrt(abs(sumatoria_raiz - ((C[0] * f_f1) + (C[1] * f_f2))))

print("Error del método: %f" % error)
