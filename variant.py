n = int(input("Введите количество чисел: "))

count = 0
total = 0

for i in range(n):
    number = int(input("Введите число: "))
    if number % 3 == 0:
        count += 1
        total += number

print("Количество:", count)
print("Сумма:", total)