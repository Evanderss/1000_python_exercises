# Simular el funcionamiento de la operador in

def pertenece_a(lista: list, elemento) -> bool:
    for i in lista:
        if elemento == i:
            return True
    return False

if __name__ == "__main__":
    lista_comprobar = [5, 2, 4, 8]
    print(pertenece_a(lista_comprobar, 5))