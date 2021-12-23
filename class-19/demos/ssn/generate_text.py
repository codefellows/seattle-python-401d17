from faker import Faker
from random import shuffle

fake = Faker()

texts = [fake.text() for _ in range(10)]

good_nums = [fake.ssn() for _ in range(10)]

bad_nums = ["666-01-1234", "665-00-1234", "901-01-1234", "555-22-0000"]

addresses = [fake.address() for _ in range(10)]

content_list = texts + good_nums + bad_nums + addresses

shuffle(content_list)

text_with_soc = " ".join(content_list)


with open("./text_with_soc_sec_nums.txt", "w") as f:
    f.write(text_with_soc)
