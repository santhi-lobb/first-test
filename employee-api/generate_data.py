import psycopg2
import random
import datetime
from faker import Faker
from random import randint, choice

fake = Faker()

conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5433"
)
cur = conn.cursor()
truck_types = ["Container", "Tank", "Cylindrical", "Refrigerated", "Small", "Trailer", "Flatbed"]
num_cities = 5000
data = []
try:
    for i in range(1000000, 2000000):
        # cur.execute(
        #     "INSERT INTO trucks VALUES (%s, %s, %s, %s, %s)",
        #     (
        #         f"truck{i}",
        #         "xxxxxxxxxx",
        #         "9999999999",
        #         random.choice(truck_types),
        #         [f"city{random.randint(1, 100000)}" for _ in range(random.randint(3, 20))]
        #  ))
        # cur.execute(
        #     "INSERT INTO cities VALUES (%s, %s, ST_POINT(%s, %s, 4326))",
        #     (f"city{i}", "random_name", random.randint(68, 97) + random.random(),
        #      random.randint(8, 37) + random.random())
        # )
        # cur.execute(
        #     "INSERT INTO demand VALUES (%s, %s, %s, %s)",
        #     (
        #         f"demand{i}",
        #         f"city{random.randint(1, num_cities)}",
        #         f"city{random.randint(1, num_cities)}",
        #         f"type{random.randint(1, len(truck_types))}"
        #     )
        # )
        cur.execute(
            "INSERT INTO pings VALUES (%s, %s, ST_POINT(%s, %s, 4326), %s, %s)",
            (
                f"ping{i}",
                f"truck{random.randint(10, 1000000)}",
                random.randint(68, 97) + random.random(),
                random.randint(8, 37) + random.random(),
                "random_city",
                datetime.datetime(2025, 6, randint(3, 4), randint(0, 23), randint(0, 59), randint(0, 59))
            )
        )
        # cur.execute(
        #     "UPDATE demand SET destination_city=%s, source_city=%s where demand_id=%s",
        #     (f"city{random.randint(1, num_cities)}", f"city{random.randint(1, num_cities)}", f"demand{i}")
        # )
        print(i)

    conn.commit()
finally:
    conn.close()