name = input ('Введите имя: ')
surname = input ('Введите фамилию: ')
year_of_birth = input ('Введите год гождения: ')
year_of_birth = int(year_of_birth)
current_year = 2023
age = current_year - year_of_birth  

print (surname, " ", name, ",", " ", age, sep = '')