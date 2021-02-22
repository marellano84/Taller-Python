import math
radio = 5
PI = 3.141592

def area_circulo(radio):
    #area = PI*(radio**2)
    area = (math.pi)*math.pow(radio, 2)
    return area

print(area_circulo(radio))