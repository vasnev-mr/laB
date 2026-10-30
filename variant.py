numbers = []
for part in input("Целые числа через пробел: ").split():
    numbers.append(int(part))

selected = []
for number in numbers:
    if number % 3 == 0:
        selected.append(number)

print("Выборка:", selected)
print("Количество:", len(selected))
print("Сумма:", sum(selected))
print("Отсортированная копия:", sorted(selected))