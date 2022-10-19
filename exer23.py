# Comprobar si un caracter es una vocal 

def es_vocal (c: str) -> str:
    """
    Comprueba si es una vocal la letra dada
    """
    vocales = ["a", "e", "i", "o", "u"]
    c = c.lower()
    return c in vocales

if __name__ == "__main__":
    print(es_vocal("a"))
    print(es_vocal("z"))
    