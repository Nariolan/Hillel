import json
import re


# Функция для считывания данных из json файла

def get_data(file_name):
    with open(f"{file_name}", "r", encoding='utf-8') as read_file:
        data = json.load(read_file)

    return data


# 2. Написать функцию сортировки данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).
# Например для Rene Descartes фамилия это Descartes, у Pierre de Fermat - Fermat и т.д.
# Если фамилии нет, то использовать имя, например Euclid.


def key_sort_name(obj_dict):
    return obj_dict.get("name").split()[-1]


# 3. Написать функцию сортировки по дате смерти из поля "years".

def key_sort_date(obj_dict):
    years = obj_dict.get("years")
    years_str_numb = re.findall(r'\d+', years)
    years_numb = [int(number) for number in years_str_numb]
    death_date = max(years_numb) if 'BC' not in years else -1*min(years_numb)
    return death_date


# 4. Написать функцию сортировки по количеству слов в поле "text"


def key_sort_text(obj_dict):
    return len(obj_dict.get("text").split())


json_data = get_data("data.json")

sorted_data = sorted(json_data, key=key_sort_text)
print(sorted_data)
sorted_data = sorted(json_data, key=key_sort_name)
print(sorted_data)
sorted_data = sorted(json_data, key=key_sort_date)
print(sorted_data)
