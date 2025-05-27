"""Generates fake employee data"""
import random
import json
from faker import Faker

fake = Faker()

data = []
for i in range(1, 100):
    fn = fake.first_name()
    ln = fake.last_name()
    record = {}
    record["id"] = i
    record["name"] = fn + " " + ln
    record["phone"] = "".join([str(random.randint(0, 9)) for _ in range(10)])
    record["email"] = fn.lower() + ln.lower() + "@gmail.com"
    record["age"] = random.randint(20, 80)
    record["gender"] = random.choice(["male", "female"])
    data.append(record)
    
with open("employees.json", "w") as file:
    json.dump(data, file, indent=2)
