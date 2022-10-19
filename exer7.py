# Obtener la extensión del archivo específicado por el usuario

nombre_archivo = input("Ingrese el nombre del archivo completo: ")

partes_del_archivo = nombre_archivo.split(".")
print(partes_del_archivo)
print(partes_del_archivo[-1])