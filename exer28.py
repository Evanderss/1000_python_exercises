# Calcular la diferencia, la unión, la intersección y la diferencia simétrica de conjuntos con colores

colores_lista_1 = ["Negro", "Rojo", "Verde", "Blanco", "Cáfe"]
colores_lista_2 = ["Blanco", "Azul", "Verde", "Gris", "Amarillo"]

colores_lista_conjunto_1 = set(colores_lista_1)
colores_lista_conjunto_2 = set(colores_lista_2)

diferencia = colores_lista_conjunto_1.difference(colores_lista_conjunto_2)
union = colores_lista_conjunto_1.union(colores_lista_conjunto_2)
intersección = colores_lista_conjunto_1.intersection(colores_lista_conjunto_2)
diferencia_sim = colores_lista_conjunto_1.symmetric_difference(colores_lista_conjunto_2)

print(diferencia)
print(union)
print(intersección)
print(diferencia_sim)