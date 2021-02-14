#1. Дано целое число (int). Определить сколько нулей в этом числе.

# my_value = int(input("Введите число "))
# string_value = str(my_value)
# counter = 0
#
# for symbol in string_value:
#     if symbol == "0":
#         counter += 1
#
# print("Количество нулей в числе: ", counter)

#2. Дано целое число (int). Определить сколько нулей в конце этого числа.

# my_value = int(input("Введите число "))
# string_value = str(my_value)
# counter = 0
# for symbol in string_value[::-1]:
#     if symbol == "0":
#         counter += 1
#     elif symbol != "0":
#         break
# print("Количество нулей в конце ввдённого числа: ", counter)

#3a. Даны списки my_list_1 и my_list_2.
#Создать список my_result в который вначале поместить
#элементы на четных местах из my_list_1, а потом все элементы на нечетных местах из my_list_2.

# my_list_1 = [1, 2, 3, 4, 5, 6]
# my_list_2 = [1, 2, 3, 4, 5]
# my_result = []
#первый вариант, который работает с
#my_list_1 = [1, 2, 3, 4, 5, 6]
#my_list_2 = [1, 2, 3, 4, 5] но при этом не выводит 1 как нечётный элемент и если выставить одинаковую
#размерность список сыпется с index out of range

# for index in my_list_1[::2]:
#     my_result.append(my_list_1[index])
#
#
# for i in my_list_2 [1::2]:
#     my_result.append(my_list_2[i])


# тут та же история, если не подогнать размерность списка - сыпется
# for index in my_list_1:
#     if  index % 2:
#         my_result.append(my_list_1[index])
#
# for index in my_list_2:
#     if index % 2 == 0:
#         my_result.append(my_list_2[index])

# print(my_result)


# 3b. Даны списки my_list_1 и my_list_2. Создать список my_result в который
# вначале поместить четные элементы (ИМЕННО ЭЛЕМЕНТЫ) из my_list_1 и потом нечетные элементы из my_list_2.
# my_list_1 = [1,3,2,4,5], my_list_2 = [10, 20, 15, 25, 22] -> my_result [2, 4, 15, 25]

# my_list_1 = [1, 3, 2, 4, 5]
# my_list_2 = [10, 20, 15, 25, 22]
# my_result = []
#
# for element in my_list_1:
#     if not element % 2:
#         my_result.append(element)
# for element_2 in my_list_2:
#     if element_2 % 2:
#         my_result.append(element_2)
#
# print(my_result)


#7. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
#Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
#быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']

my_str = "yappidoor"
print(len(my_str))
i=0
my_list = list(my_str)
result_list = []

if not len(my_str) % 2 == 0:
    my_list.append("_")
    for elem in my_list:
        try:
            result_list.append(my_list[i]+my_list[i+1])
            i+=2
        except:
            pass
print(result_list)
