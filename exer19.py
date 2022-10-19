# Comprobar si una cadena termina con .py, sino es así, ponlo así 

def validar_nombre_archivo(nombre_archivo: str) -> str:
    """Este programa identifica si un archivo termina en .py, de lo cntrario, se lo agrega"""
    if len(nombre_archivo) >= 3 and nombre_archivo[-3:] == ".py":
        return nombre_archivo
    else: 
        return nombre_archivo + ".py"

if __name__ == "__main__":
    print(validar_nombre_archivo("main.py"))
    print(validar_nombre_archivo("modulo"))