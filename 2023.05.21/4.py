number = int (input ('Bведите число: '))
a = number // 100
b = (number % 100) // 10
c = number % 10
d = a + b + c
f = b * c * a

print (f"Cумма цифр = {d}\n"
            f"Произведение цифр = {f}")