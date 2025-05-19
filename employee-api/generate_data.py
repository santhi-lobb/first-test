"""Generates fake employee data"""
import random
import json

first_names = [
    "Ravi", "Santhi", "Tony", "Pushpa", "Ram", 
    "Ramesh", "Suresh", "Charles", "Hemanth", "John"
]
last_names = [
    "Kumar", "Reddy", "Sai", "Krishna", "Smith",
    "Rao", "Bro", "Script", "Python", "Raj"
]

data = []
for i, fn in enumerate(first_names):
    for j, ln in enumerate(last_names):
        record = {}
        record["id"] = (i * 10) + j
        record["name"] = fn + " " + ln
        record["phone"] = "".join([str(random.randint(0, 9)) for _ in range(10)])
        record["email"] = fn.lower() + ln.lower() + "@gmail.com"
        record["age"] = random.randint(20, 80)
        record["gender"] = random.choice(["male", "female"])
        data.append(record)
    
with open("employees.json", "w") as file:
    json.dump(data, file, indent=2)
