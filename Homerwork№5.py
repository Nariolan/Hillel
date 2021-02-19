# #1. Дано целое число (int). Определить сколько нулей в этом числе.
#
my_value = int(input("Введите число "))
string_value = str(my_value)
counter = 0

for symbol in string_value:
    if symbol == "0":
        counter += 1

print("Количество нулей в числе: ", counter)

#2. Дано целое число (int). Определить сколько нулей в конце этого числа.
#
my_value = int(input("Введите число "))
string_value = str(my_value)
counter = 0
for symbol in string_value[::-1]:
    if symbol == "0":
        counter += 1
    elif symbol != "0":
        break
print("Количество нулей в конце ввдённого числа: ", counter)

#3a. Даны списки my_list_1 и my_list_2.
#Создать список my_result в который вначале поместить
#элементы на четных местах из my_list_1, а потом все элементы на нечетных местах из my_list_2.

my_list_1 = [1, 2, "3", 4, 5, 6]
my_list_2 = [1, 2, 3, 4, 5]
my_result = []

for index in my_list_1[::2]:
    my_result.append(index)


for index_2 in my_list_2 [1::2]:
    my_result.append(index_2)


print(my_result)


# 3b. Даны списки my_list_1 и my_list_2. Создать список my_result в который
# вначале поместить четные элементы (ИМЕННО ЭЛЕМЕНТЫ) из my_list_1 и потом нечетные элементы из my_list_2.
# my_list_1 = [1,3,2,4,5], my_list_2 = [10, 20, 15, 25, 22] -> my_result [2, 4, 15, 25]
#
my_list_1 = [1, 3, 2, 4, 5]
my_list_2 = [10, 20, 15, 25, 22]
my_result = []

for element in my_list_1:
    if not element % 2:
        my_result.append(element)
for element_2 in my_list_2:
    if element_2 % 2:
        my_result.append(element_2)

print(my_result)

# 4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
# стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1]

my_list = [1, 2, 3, 4]
new_list = my_list[1:4]
new_list.append(my_list[0])
print(new_list)


# 5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
# [1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)
#
my_list = [1, 2, 3, 4]
my_list.append(my_list[0])
my_list.pop(0)

print(my_list)

# 6. Дана строка в которой есть числа (разделяются пробелами).
# Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
# Для данного примера ответ - 133.


my_str = "43 больше чем 34 но меньше чем 56"

splitted_string_list = my_str.split()

my_int_list = []

for str in splitted_string_list:
    if str.isdigit():
        my_int_list.append(int(str))

print(sum(my_int_list))

#7. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
#Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
#быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']

my_str = "2134567"
print(len(my_str))
my_list = []

if not len(my_str) % 2==0:
    my_str += "_"

for symbol in my_str[0:-1]:

    index = my_str.index(symbol)
    if index % 2 == 0:
        my_list.append(my_str[index]+my_str[index+1])

print(my_list)
print(my_str)


# 8. Дана строка my_str в которой символы не повторяются и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить часть строки между этими символами.
# my_str = "My_long str", l_limit = "o", r_limit = "t" -> sub_str = "ng s"

my_str = "asdfghjkl"

l_limit = "s"
r_limit = "l"
sub_string = my_str[my_str.find(l_limit):my_str.find(r_limit)]
print(sub_string)


# 9. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
# my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".

my_str="My long string"

r_limit = "g"
sub_str = ""
l_limit = "o"

sub_string = my_str[(my_str.find(l_limit)+1):my_str.rfind(r_limit)]
print(sub_string)

# 10. Дан список чисел. Определите, сколько в этом списке элементов,
# которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
# Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.

my_list = [2, 4, 1, 5, 3, 9, 0, 7]
counter = 0

for elem in my_list[1:-2]:
    index = my_list.index(elem)
    if elem > my_list[index - 1] + my_list[index + 1]:
        counter = counter + 1

print(counter)

