import string
import random


class EmailGenerator:
    names = ["king", "miller", "kean"]
    domains = ["net", "com", "ua"]

    def __init__(self, min_limit, max_limit):
        self.min_limit = min_limit
        self.max_limit = max_limit

    def generate_str(self):
        random_string = [random.choice(string.ascii_lowercase) for _ in
                         range(random.choice(range(self.min_limit, self.max_limit)))]
        return "".join(random_string)

    def generate_email(self):
        name_part = random.choice(self.names)
        int_part = str(random.randint(100, 999))
        string_part = self.generate_str()
        domain_part = random.choice(self.domains)
        email = f"{name_part}.{int_part}@{string_part}.{domain_part}"
        return email


generator_1 = EmailGenerator(5, 7)
print(generator_1.generate_str())
print(generator_1.generate_email())
