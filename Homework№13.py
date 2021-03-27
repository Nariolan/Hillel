import random, string


class EmailGenerator:

    def __init__(self, list_1, list_2, min_limit=100, max_limit=999):
        self.min_limit = min_limit
        self.max_limit = max_limit
        self.list_1 = list_1
        self.list_2 = list_2

    def generate_str(self):
        random_string = [random.choice(string.ascii_lowercase) for _ in
                         range(random.choice(range(self.min_limit, self.max_limit)))]
        return "".join(random_string)

    def generate_email(self):
        name_part = random.choice(self.list_1)
        int_part = str(random.randint(100, 999))
        string_part = self.generate_str()
        domain_part = random.choice(self.list_2)
        email = f"{name_part}.{int_part}@{string_part}.{domain_part}"
        return email


names = ["king", "miller", "kean"]
domains = ["net", "com", "ua"]
generator_1 = EmailGenerator(names, domains, 5, 7)
print(generator_1.generate_str())
print(generator_1.generate_email())
