from functions import average, normalize_text, sum_digits, select_numbers

assert sum_digits(0) == 0
assert sum_digits(507) == 12
assert sum_digits(-507) == 12
assert average([]) is None
assert average([2, 4, 6]) == 4
assert normalize_text("  ПРИВЕТ   Мир  ") == "привет мир"
assert normalize_text("   ") == ""

# Вариант 6: числа, равные порогу
assert select_numbers([-5, 0, 2, 5], 2) == [2]
assert select_numbers([], 2) == []

# Границы условия: 1 — не равно, 2 — равно, 3 — не равно
assert select_numbers([1, 2, 3], 2) == [2]
assert select_numbers([1, 3], 2) == []

# Повторы подходящего значения сохраняются
assert select_numbers([1, 2, 2, 3, 2], 2) == [2, 2, 2]

# Исходный список не изменяется
source = [-5, 0, 2, 5]
before = source.copy()
select_numbers(source, 2)
assert source == before

# Дробное среднее — сравнение с допуском
actual = average([1, 2])
expected = 1.5
assert abs(actual - expected) < 1e-9

print("Базовые проверки пройдены")