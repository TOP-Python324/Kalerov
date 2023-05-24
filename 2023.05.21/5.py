integer = int (input ('Bведите число: '))
fractional_part = int (input ('Bведите число: '))
private_number = fractional_part / 10
summa = private_number + integer
result = summa * 1.61
translat = round(result, ndigits=1)
print (f"{summa} миль = {translat} км")
