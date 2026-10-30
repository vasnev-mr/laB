numbers = []
for part in input("Целые числа через пробел: ").split():
    numbers.append(int(part))

result = []
for number in numbers:
    if number < 0:
        result.append(-number)
    else:
        result.append(number)

print("Исходный список:", numbers)
print("Новый список:", result)