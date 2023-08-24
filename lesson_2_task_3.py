import math

def square(side):
    s = side * side
    return math.ceil(s)

side_length = float(input("Введите длину стороны квадрата: "))
result = square(side_length)
print(f"Площадь квадрата: {result}")