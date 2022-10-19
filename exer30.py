# Calcular el máximo común divisor de dos números 
def mcd(x: int, y: int):
    mcd = 1
    if x % y == 0:
        return y
    for i in range(int(y/2), 0, -1):
        if x % i == 0 and y % i == 0:
            mcd = i
            break
    return mcd

if __name__ == "__main__":
    print(mcd(8, 4))
    print(mcd(13, 7))
