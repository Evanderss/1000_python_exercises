# def custom_max(n1: int, n2: int) -> int:
#     """Given two numbers, compare and return the bigger numbers
    
#     Args: 
#         n1(int): First comparison number
#         n2(int): Second comparison number

#     Returns:
#         n(int): The bigger number
#     """
#     if n1 > n2:
#         return n1
#     elif n2 > n1: 
#         return n2
#     elif n1 == n2:
#         raise Exception("Put different numbers to compare")
#     else: 
#         raise Exception("Something was wrong")


# if __name__ == '__main__':
#     print(custom_max(15, 10))

# def max_of_three(n1: int, n2: int, n3: int) -> int:
#     """Take three numbers to compare and return the bigger number

#     Args:
#         n1(int): First comparison number
#         n2(int): Second comparison number
#         n3(int): Third comparison number

#     Returns:
#         n(int): the bigger number
#     """
#     a > b > c
#     b > c
#     a > c
#     if n1 > n2 and n1 > n3:
#         return n1
#     elif n2 > n1 and n2 > n3:
#         return n2
#     elif n3 > n1 and n3 > n2:
#         return n3

# if __name__ == '__main__':
#     print(max_of_three(5, 10, 3))

# def vocal(x: str) -> bool:
#     """Given a caracter, is or is not a vocal

#     Args:
#         x(str): Letter to compare

#     Returns:
#         bool: True if is a vocal, False otherwise
#     """
#     caracter = ["a", "e", "i", "o", "u"]
#     if x in caracter:
#         return True
#     else:
#         return False

# if __name__ == '__main__':
#     print(vocal("a"))

# def sum(x: int, y: int) -> int:
#     sumar = x + y 
#     return sumar 

def histograma(lista) -> str:
    for i in lista:
        barra = i * "*"
        print(f"{barra}")

print(histograma([4, 5, 7]))