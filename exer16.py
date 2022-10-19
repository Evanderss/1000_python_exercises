# Crear una función para evaluar un número y realizar una operación

def diferencia(n):
    if n <= 15: 
        return 15 - n
    else: 
        return  (15 - n) * 2

if __name__ == "__main__":
    print(diferencia(18))