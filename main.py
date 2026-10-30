from functions import sum_digits, average, normalize_text, select_numbers


def main():
    number = int(input("Введите целое число: "))

    numbers = []
    for part in input("Введите числа через пробел: ").split():
        numbers.append(int(part))

    text = input("Введите текст: ")
    threshold = int(input("Введите порог: "))

    print("Сумма цифр:", sum_digits(number))

    avg = average(numbers)
    if avg is None:
        print("Среднее: Нет данных")
    else:
        print("Среднее:", avg)

    print("Нормализованный текст:", normalize_text(text))
    print("Выборка:", select_numbers(numbers, threshold))


if __name__ == "__main__":
    main()