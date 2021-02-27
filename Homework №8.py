# 1. Написать функцию, которая генерирует и возвращает строку случайной длинны.
# Минимальную и максимальную длину строки ограничить с помощью параметров min_limit, max_limit, передаваемых в функцию.

import string
import random


def random_string_generate(min_limit=1, max_limit=10):
    random_str = [random.choice(string.ascii_lowercase) for _ in range(random.choice(range(min_limit, max_limit)))]

    return "".join(random_str)


my_str = random_string_generate()

print(my_str)

# 2. Даны списки names и domains (создать самостоятельно).
# Написать функцию create_email для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен

names = ["king", "miller", "kean"]
domains = ["net", "com", "ua"]


def generate_random_email(my_list_1, my_list_2):
    name_part = random.choice(my_list_1)
    int_part = str(random.randint(100, 999))
    string_part = random_string_generate(5, 7)
    domain_part = random.choice(my_list_2)
    final_email = f"{name_part}.{int_part}@{string_part}.{domain_part}"
    return final_email


print(generate_random_email(names, domains))
