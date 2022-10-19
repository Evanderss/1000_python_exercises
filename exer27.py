# Generar un conjunto de números aleatorios y determinar cuales son impares
from random import randint

numeros_aletorios = [randint (1, 100) for _ in range(50)]

print(numeros_aletorios)

numeros_impares = filter(lambda n: n % 2 == 1, numeros_aletorios)

print()

print(list(numeros_impares))