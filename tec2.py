def fibo(n: int):
    """
    """
    a = 0
    b = 1
    
    for i in range(n):
        c = a + b
        a = b 
        b = c
    return b

for x in range(20):
    print(fibo(x))

#Forma recursiva
# fn = f(n-1) + f(n-2)
def fib_r(n:int) -> int:
    if n < 2:
        return n
    return fib_r(n-1) + fib_r(n-2)
for x in range(20):
    print(fib_r(x))