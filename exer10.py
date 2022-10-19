# Pedir al usuario un número y calcular n 
n = int(input("Ingresa un número entero: "))
nn = int("{}{}".format(n, n))
nnn = int("{}{}{}".format(n, n, n))
suma = n + nn + nnn
print(suma)