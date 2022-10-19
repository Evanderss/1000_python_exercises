# Calcular el mínimo común múltiplo de dos números 

def mcm(x: int, y: int):
    z = max(x, y)

    while True:
        if (z % x == 0) and (z % y == 0):
            return z

        z += 1

print(mcm(2, 4))
print(mcm(32, 13))
print(mcm(17, 15))
