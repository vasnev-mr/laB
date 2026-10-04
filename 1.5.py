#вроде как 6 вариант у меня

zak = input("Введите название заказа: ")
name = input("Введите ваше имя: ")

zak1 = input("Введите название первой позиции: ")
kolvo1 = int(input("Введите количество " + zak1 + ": "))
price1 = float(input("Введите цену в руб за " + zak1 + ": "))

zak2 = input("Введите название второй позиции: ")
kolvo2 = int(input("Введите количество " + zak2 + ": "))
price2 = float(input("Введите цену в руб за " + zak2 + ": "))

dos = float(input("Введите стоимость доставки: "))
money = float(input("Введите внесенную сумму: "))
skidka_proc = float(input("Введите скидку в процентах: "))

poz1 = kolvo1 * price1
poz2 = kolvo2 * price2
sum = poz1 + poz2
skidka_rub = sum * skidka_proc / 100
sum_so_skidkoy = sum - skidka_rub
dostavka = sum_so_skidkoy + dos
kolvo = kolvo1 + kolvo2
sdacha = money - dostavka

print()
print("=" * 40)
print("Заказ:", zak)
print("Заказчик:", name)
print("=" * 40)
print(zak1, "|", kolvo1, "|", price1, "|", poz1)
print(zak2, "|", kolvo2, "|", price2, "|", poz2)
print("-" * 40)
print("Стоимость товаров без доставки:", sum)
print("Скидка (%):", skidka_proc)
print("Скидка (руб.):", skidka_rub)
print("Стоимость товаров со скидкой:", sum_so_skidkoy)
print("Стоимость доставки:", dos)
print("Общая сумма с доставкой:", dostavka)
print("Общее количество единиц:", kolvo)
print("Внесено:", money)
print("Сдача:", sdacha)
print("=" * 40)