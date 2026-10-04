import math

radius = float(input("Введите радиус: "))

length = 2 * math.pi * radius
area = math.pi * radius * radius

print("Длина окружности:", int(length * 100) / 100)
print("Площадь круга:", int(area * 100) / 100)