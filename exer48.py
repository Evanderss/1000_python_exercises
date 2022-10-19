# Convertir una cadena de caracteres a un entero y un real

cadena = "3.1416"

entero = int(cadena.split(".")[0])
print(entero)

real = float(cadena)
print(real)