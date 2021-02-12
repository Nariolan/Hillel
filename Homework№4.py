###############Задание№1###############
my_list = [1, 2, 220, 1330, 1480, 2754]

for item in my_list:
    if item > 100:
        print(item)

###############Задание№2###############

my_list = [1, 2, 220, 1330, 1480, 2754]

my_result = []

for item in my_list:
    if item > 100:
        my_result.append(item)

print(my_result)

###############Задание№3###############

my_list = [1, 2, 220, 1330, 1480, 2754]

if len(my_list) < 2:
    my_list.append(0)
else:
    value = my_list[-1] + my_list[-2]
    my_list.append(value)

print(my_list)

###############Задание№4###############

my_value = input("Введите число ")

try:
    my_value_2 = float(my_value)
except (TypeError, ValueError):
    print("Произошла ошибка")
    my_value_2 = float(input("Введите число с плавающей запятой"))

print(my_value_2 ** -1)

###############Задание№5###############
my_list = [1, 3, 5, 8, 6, 10]

my_result = []

for i in range(len(my_list)):
    if (i + my_list[i]) % 2 == 0:
        value = my_list[i]
        my_result.append(value)

print(my_result)

###############Задание№6###############

my_list_1 = [2, 7]

my_list_2 = [5, 4]

for item in range (len(my_list_1)):
    print(my_list_1[item], my_list_2[item])

###############Задание№7###############

my_string="0123456789"
my_list=[]

for elem_1 in my_string:
    for elem_2 in my_string:
        new_value = elem_1 + elem_2
        my_list.append(new_value)
        print(new_value)

print(my_list)
