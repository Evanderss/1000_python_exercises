# Emular el funcionamiento del producto de cadenas
def producto_cadena(cadena: str, repetición: int) -> str:
    resultado = ""

    for i in range(repetición):
        resultado += cadena
    
    return resultado

if __name__ == "__main__":
    print(producto_cadena("Python", 4))