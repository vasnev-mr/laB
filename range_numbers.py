a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

if a < b:
    for number in range(a, b + 1):
        print(number)
elif a > b:
    for number in range(a, b - 1, -1):
        print(number)
else:
    print(a)