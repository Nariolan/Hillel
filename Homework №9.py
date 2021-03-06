# 1. Считать данные из файла names.txt и поместить в список только фамилии из файла.
# Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии).
# Фамилия находится всегда на одной и той же позиции в строке.

import random
import string
import json


def get_names(filename):
    with open(filename, "r") as file:
        list_of_names = []
        for line in file.readlines():
            splitted_line = line.split()
            list_of_names.append(splitted_line[1])
        return list_of_names


print(get_names("Names.txt"))


# 2. Создать функцию для записи в файл json.
# Создает и возвращает словарь со случайным количеством ключей (не менее 5 но не более 20 ключей).
# Ключи - уникальные случайные строки длинны 5 символов из маленьких букв английского алфавита
# (можно с повторениями символов).
# Значения - или целое число в диапазоне от -100 до 100, или число типа float в диапазоне от 0 до 1,
# или True/False. Выбор значения должен быть равновероятным. Т.е. вероятность того, что значение будет целым
# такая же, как и вероятность того, что будет типа float или типа bool.

def random_string_generate():
    random_str = [random.choice(string.ascii_lowercase) for _ in range(5)]
    return "".join(random_str)


def create_dict():
    dict_size = random.randint(5, 20)
    boolean_list = [True, False]
    choice = random.choice([1, 2, 3])
    result_dict = {}

    if choice == 1:
        for _ in range (dict_size):
            random_string = random_string_generate()
            random_value = random.randint(-100, 100)
            result_dict[random_string] = random_value
    elif choice == 2:
        for _ in range(dict_size):
            random_string = random_string_generate()
            random_value = random.uniform(0, 1)
            result_dict[random_string] = random_value
    else:
        for _ in range(dict_size):
            random_string = random_string_generate()
            random_value = random.choice(boolean_list)
            result_dict[random_string] = random_value

    return result_dict


print(create_dict())


# 3. Написать функцию generate_and_write_json которая принимает один параметр - полный путь к файлу.
# Cгенерировать данные для записи с помощью функции из пункта 2 и записать в данный файл.
#
def write_json_file(file_path):
    data = create_dict()
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file)


file_path = "/home/nariolan/PycharmProjects/Hillel/HW9.json"
write_json_file(file_path)
#
#
#
#
#
#
#
