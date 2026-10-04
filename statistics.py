n = int(input("Введите количество чисел: "))

first = int(input("Введите число: "))
total = first
positive = 0
maximum = first

if first > 0:
    positive = 1

for i in range(2, n + 1):
    number = int(input("Введите число: "))
    total += number

    if number > 0:
        positive += 1

    if number > maximum:
        maximum = number

print("Сумма:", total)
print("Положительных:", positive)
print("Максимум:", maximum)