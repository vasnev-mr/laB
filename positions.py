numbers = []
for part in input("Целые числа через пробел: ").split():
    numbers.append(int(part))

if len(numbers) == 0:
    print("Нет данных")
else:
    maximum = max(numbers)
    positions = []
    for index, value in enumerate(numbers):
        if value == maximum:
            positions.append(index)
    print(positions)