n = int(input("Введите целое число n >= 2: "))

divisor = 2
is_prime = True

while divisor * divisor <= n:
    if n % divisor == 0:
        is_prime = False
    divisor += 1

if is_prime:
    print("Простое")
else:
    print("Составное")