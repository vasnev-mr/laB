numbers = []
for part in input("Целые числа через пробел: ").split():
    numbers.append(int(part))

if len(numbers) == 0:
    print("Нет данных")
else:
    total = sum(numbers)
    average = total / len(numbers)
    print("Количество:", len(numbers))
    print("Сумма:", total)
    print("Минимум:", min(numbers))
    print("Максимум:", max(numbers))
    print("Среднее:", int(average * 100) / 100)