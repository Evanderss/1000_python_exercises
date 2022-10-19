# Exponiendo el uso básico de la función print

# Usemos el argumento separador = separator = sep, podremos observar que el texto será separado por el simbolo 
# que pongamos, en este caso "-"
print("Python", "es", "fántastico")
print("Python", "es", "fántastico", sep="-")
# Usamos {} para especificar que es un espacio que está pendiente por llenar en esa cadena
# Invocamos la función .format para llenar los {} según su orden
print("{} es {}".format("Python", "íncreible"))