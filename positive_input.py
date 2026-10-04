number = int(input("Введите число: "))
rejected = 0

while number <= 0:
    rejected += 1
    number = int(input("Введите число: "))

print("Квадрат:", number * number)
print("Отклонённых попыток:", rejected)