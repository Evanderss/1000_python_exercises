# Crear una subcadena de n caracteres replicada n cantidad de veces
# ejemplo: "Python" -> "Py"; "PyPy"

def replicar_subcadena(cadena: str, n: int) -> str:
    
    # n_caracteres almacenará la cantidad de caracteres que queremos tomar de la cadena original 
    n_caracteres = n
    if n_caracteres > len(cadena):
        n_caracteres = len(cadena)
    
    # Aquí estamos indicando de donde partirá la subcadena y dondé terminará 
    subcadena = cadena[:n_caracteres]
    
    # Aquí vamos a replicar n cantidad de veces la subcadena, inicialmente la hacemos vacía
    resultado = ""
    
    for i in range(n):
        resultado += subcadena
    
    return resultado
if __name__ == "__main__":
    ver = replicar_subcadena("Python", 2)
    print(ver)
    