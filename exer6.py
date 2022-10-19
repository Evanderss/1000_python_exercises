# Obtener un conjunto de números separados por coma y crear una lista

entrada = list(input("Escribe los números que estarán en la lista: "))

print(entrada)

# Otra forma de hacerlo es que el usuario ingrese todo y convertirlo a lista con split

entrada2 = input("Ingresa los números con comas: ")

print(type(entrada))
print(entrada)

numero = entrada2.split(",")
print(type(numero))
print(numero)