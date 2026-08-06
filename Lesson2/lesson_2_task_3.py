import math

def square(side) -> float:
    area = side * side
    # Если результат не целый, округляем вверх
    if area != int(area):
        return math.ceil(area)
    return area

