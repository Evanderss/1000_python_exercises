# Crear un histograma a partir de una lista de enteros

def crea_histograma(lista, caracter="*"):
    for i in lista:
        print(caracter * i)

if __name__ == "__main__":
    lista = [1, 4, 3, 6, 2, 14, 5, 7]
    crea_histograma(lista)