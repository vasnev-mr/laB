a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
op = input("Введите операцию (+, -, *, /): ")

if op == "+":
    result = a + b
    print("Результат:", int(result * 100) / 100)
elif op == "-":
    result = a - b
    print("Результат:", int(result * 100) / 100)
elif op == "*":
    result = a * b
    print("Результат:", int(result * 100) / 100)
elif op == "/":
    if b == 0:
        print("Деление на ноль запрещено")
    else:
        result = a / b
        print("Результат:", int(result * 100) / 100)
else:
    print("Неизвестная операция")