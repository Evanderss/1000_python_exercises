# Obtener la representación inversa de una cadena de cáracteres
# Usando la funcioón reversed 
cadena = "Python"

for i in reversed(cadena):
    print(i, end="")

# Con Slices
print()
print(cadena[::-1])