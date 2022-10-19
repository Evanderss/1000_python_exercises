def costum_max(n1: int, n2: int):
    """Dados dos números enteros, retornar el maximo

    Args:
        n1[int]: Primer número a comparar
        n2[int]: Segundo número a comparar
    Returns:
        Int: El mayor de ambos
    """
    if n2 > n1:
        return n2
    elif n1 > n2:
        return n1
    elif n1 == n2:
        raise Exception("Los valores no pueden ser iguales")
    else:
        raise Exception("Algo salió mal")
     
if __name__ == "__main__":
    maxi = costum_max(2, 5)
    print(maxi)