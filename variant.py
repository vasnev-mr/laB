text = input("Введите текст: ")

count = 0

for word in text.split():
    cleaned = word.strip(".,!?;:").lower()
    if cleaned == "":
        continue
    if len(cleaned) == 4:
        print(cleaned)
        count += 1

if count == 0:
    print("Нет совпадений")

print("Количество:", count)