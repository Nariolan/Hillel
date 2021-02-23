# # 1. Дан список строк my_list. Создать новый список в который поместить
# # элементы из my_list по следующему правилу:
# # Если строка стоит на нечетном месте в my_list, то ее заменить на
# # перевернутую строку. "qwe" на "ewq".
# # Если на четном - оставить без изменения.
# # Задание сделать с использованием enumerate.
#
# my_list = ["qwe", "asd", "zxc", "zcc"]
# my_result = []
# for index, value in enumerate(my_list):
#     if not index % 2 == 0:
#         my_result.append(my_list[index][::-1])
#     else:
#         my_result.append(my_list[index])
#
# print(my_result)
#
# # 2. Дан список строк my_list. Создать новый список в который поместить
# # элементы из my_list у которых первый символ - буква "a".
#
# my_list = ["qwe", "asd", "zxc"]
# result_list = []
#
# for string in my_list:
#      if string[0] == 'a':
#         result_list.append(string)
#
# print(result_list)
#
#
# # 3. Дан список строк my_list. Создать новый список в который поместить
# # элементы из my_list в которых есть символ - буква "a" на любом месте.
#
# my_list = ["qwe", "asd", "zxc", "sas"]
# new_list = []
#
# for string in my_list:
#     if "a" in string:
#         new_list.append(string)
#
# print(new_list)
#
#
# # 4. Дан список my_list в котором могум быть как строки (type str) так и целые числа (type int).
# # Создать новый список в который поместить только строки из my_list.
#
# my_list = ["qwe", 1, "asd", 2, "zxc", 993]
# result_list = []
#
# for element in my_list:
#     if type(element) == str:
#         result_list.append(element)
#
# print(result_list)
#
#
# # 5. Дана строка my_str. Создать список в который поместить те символы из my_str,
# # которые встречаются в строке только один раз.
#
# my_str = "qqweertyy"
# result_list = []
#
# my_set = set(my_str)
#
# for char in my_set:
#     if my_str.count(char)==1:
#         result_list.append(char)
#
# print(result_list)
#
#
# # 6. Даны две строки. Создать список в который поместить те символы,
# # которые есть в обеих строках хотя бы раз.
#
# my_string_1 = "qwertyzxc"
# my_string_2 = "qghjkzxc"
#
# set_1 = set(my_string_1)
# set_2 = set(my_string_2)
#
# result_list = list(set_1.intersection(set_2))
# print(result_list)
#
# # 7. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# # но в каждой только по одному разу.
#
my_string_1 = "aasddfgghjjkllw"

my_string_2 = "qqweerttyuuioops"

set_1 = set(my_string_1)
set_2 = set(my_string_2)
result_set_1 = set()
result_set_2 = set()

for char in set_1:
    if my_string_1.count(char) == 1:
        result_set_1.add(char)

for char in set_2:
    if my_string_2.count(char) == 1:
        result_set_2.add(char)

my_result = list(result_set_1.intersection(result_set_2))
print(my_result)

# # 8. Описать с помощью словаря следующую структуру для конкретного человека (можно придумать):
# # Фамилия
# # Имя
# # Возраст
# # Проживание
# #     Страна
# #     Город
# #     Улица
# # Работа
# #     Наличие
# #     Должность
#
# human_dict = {"Фамилия": "Ларичев",
#               "Имя": "Aлександр",
#               "Возраст": "20",
#               "Проживание": {"Страна": "Украина",
#                              "Город": "Днепр",
#                              "Улица": "Пaрус"},
#               "Работа": {"Наличие": False,
#                          "Должность": "Отсутствует"}
#               }
#
# print(human_dict)
#
# # 9. Описать с помощью словаря следующую структуру (рецепт ненастоящего торта,
# # придумать и указать граммы для продуктов):
# # Составляющие
# #     Коржи
# #         Мука
# #         Молоко
# #         Масло
# #         Яйцо
# #     Крем
# #         Сахар
# #         Масло
# #         Ваниль
# #         Сметана
# #     Глазурь
# #         Какао
# #         Сахар
# #         Масло
#
#
# cake_recipe_dict = {"Составляющие": {"Коржи": {"Мука": "350г",
#                                                "Молоко": "100мл",
#                                                "Масло": "100мг",
#                                                "Яйца": "10шт",
#                                                },
#                                      "Крем": {"Сахар": "150г",
#                                               "Масло": "100мг",
#                                               "Ваниль": "2 пачки(60мг)",
#                                               "Сметана": "200г"},
#                                      "Глазурь": {"Какао": "2 упаковки",
#                                                  "Сахар": "200г",
#                                                  "Масло": "100мг"}}
#                     }
#
# print(cake_recipe_dict)
