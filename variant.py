total = int(input("Введите количество файлов: "))
capacity = int(input("Введите вместимость одного каталога: "))

full = total // capacity
remainder = total % capacity
min_units = (total + capacity - 1) // capacity

print("Полностью заполненных каталогов:", full)
print("Остаток файлов:", remainder)
print("Минимальное число каталогов:", min_units)