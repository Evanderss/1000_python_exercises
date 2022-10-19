# Emular el funcionamiento de join para concatenar una lista

def concatenar_lista(lista):
    resultado = ""
    for i in lista:
        resultado += str(i)

    return resultado

if __name__ == "__main__":
    numeros = [2, 4, 0, 3, 5, 12]
    print(concatenar_lista(numeros))