def sum_digits(number):
    """Сумма цифр модуля числа. Для нуля — 0."""
    number = abs(number)
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total


def average(numbers):
    """Среднее списка или None, если список пуст."""
    if len(numbers) == 0:
        return None
    return sum(numbers) / len(numbers)


def normalize_text(text):
    """Нижний регистр, без пробелов по краям, один пробел между словами."""
    return " ".join(text.lower().split())


def select_numbers(numbers, threshold):
    """Новый список чисел, равных порогу. Порядок и повторы сохраняются."""
    result = []
    for number in numbers:
        if number == threshold:
            result.append(number)
    return result