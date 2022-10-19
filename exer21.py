# Generar los n primeros números pares positivos

def generar_numeros_pares(n: int):
    pares = []
    contador = 0
    numero = 0
    while contador < n:
        if numero % 2 == 0:
            pares.append(numero)
            contador += 1
        numero += 1
    return pares

if __name__ == "__main__":
    n = int(input("Ingresa la cantidad de pares a generar: "))
    if n > 0:
        print(generar_numeros_pares(n))
    else: 
        print("Ingresa números positivos")