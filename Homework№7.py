# 1) Создать список из 20 случайных целых чисел в диапазоне от 1 до 100.
# Задание можно выполнить и через обычный цикл и через генератор списков.
from random import randint

my_list = []

for _ in range(20):
    my_list.append(randint(1, 100))

print(my_list)

# 2) Создать словарь triangle в который записать точки A B C (ключи),
# и их координаты - кортежи (значения), созданные случайным образом с помощью модуля random в диапазоне от -10 до 10 по каждой оси.

triangle = {
    "A": [randint(-10, 10), randint(-10, 10)],
    "B": [randint(-10, 10), randint(-10, 10)],
    "C": [randint(-10, 10), randint(-10, 10)]
}

print(triangle)


# 3) Создать функцию my_print, которая принимает в виде параметра строку и печатает ее
# с тремя символами * вначале и в конце строки.
# Пример:
# my_str = 'I'm the string'
# Печатает ***I'm the string***

def my_print(my_str=""):
    print("***" + my_str + "***")


my_print("Тестовая строка")

# 4) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена.
# б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.
# в) Посчитать среднее количество лет всех людей из списка

persons = [{"name": "John", "age": 15}, {"name": "Jack", "age": 45}, {"name": "David", "age": 54},
           {"name": "Jason", "age": 15}]

ages_list = []

for person in persons:
    ages_list.append((person.get("age")))

minimal_age = min(ages_list)

for person in persons:
    if person.get("age") == minimal_age:
        print(person.get("name"))

########################################################################################################################
# б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.
len_of_names_list = []

for person in persons:
    len_of_names_list.append(len(person.get("name")))

for person in persons:
    if len(person.get("name")) >= max(len_of_names_list):
        print(person.get("name"))

########################################################################################################################
# в) Посчитать среднее количество лет всех людей из списка

ages_list_ = []

for person in persons:
    ages_list_.append(person.get("age"))

print(sum(ages_list_) / len(ages_list_))

# 5) Даны два словаря my_dict_1 и my_dict_2.
# а) Создать список из ключей, которые есть в обоих словарях.
# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},


my_dict_1 = {"age": 27, "name": "Denis", "country": "Ukraine", "city": "Kharkiv"}

my_dict_2 = {"age": 54, "name": "Valerii", "country": "Ukraine"}

common_keys_list = []

my_set_1 = set(my_dict_1.keys())
my_set_2 = set(my_dict_2.keys())

common_keys_list = list((my_set_1.intersection(my_set_2)))
print(common_keys_list)

# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.

unique_keys_list = list(my_set_1.difference(my_set_2))
print(unique_keys_list)

# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.

my_dict_result = {}

my_set_3 = my_set_1.difference(my_set_2)
#
for key in my_dict_1:
    for elem in my_set_3:
        if key == elem:
            my_dict_result[key] = my_dict_1[key]

print(my_dict_result)

# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},

my_keys_set = set(my_dict_1.keys()).union(set(my_dict_2.keys()))
result_dict = {}

for key in my_keys_set:
    if key in set((my_dict_1.keys())).difference(set(my_dict_2.keys())):
        result_dict[key] = my_dict_1[key]
    else:
        result_dict[key] = [my_dict_1[key], my_dict_2[key]]

print(result_dict)


