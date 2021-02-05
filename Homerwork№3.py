#####################Задание№1#####################

value = int(input("Введите число "))

new_value = value/2 if value < 100 else - value

print(new_value)

#####################Задание№2#####################

value = int(input("Введите число "))

new_value = 1 if value < 100 else 0

print(new_value)

#####################Задание№3#####################

value = int(input("Введите число "))

new_value = True if value < 100 else False

print(new_value)

#####################Задание№4#####################

my_str = input("Введите строку: ")

print(my_str.upper())

#####################Задание№5#####################

my_str = input("Введите строку ")

print(my_str.lower())

#####################Задание№6#####################

my_str = input("Введите строку ")

if len(my_str) < 5:

    print(my_str*2)

else:

    print(my_str)

#####################Задание№7#####################

my_str = input("Введите строку")

if len(my_str) < 5:

    print(my_str + my_str[::-1])

else:

    print(my_str)



