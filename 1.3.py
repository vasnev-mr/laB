first = 2 #2 и 3 считались строкой до исправления, результат 5
second = 3
print(first + second)

age = int(input("Возраст: ")) # отсутсвие int
print(age + 1)

first = 4
second = 7
third = 10
average = (first + second + third) / 3 #выполнялось деление на 3 последнего числа, а не суммы
print(average)