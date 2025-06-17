import psycopg2
import random
import datetime
import faker
from random import randint, choice

fake = faker.Faker()

conn = psycopg2.connect(
    database="e-commerce",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5433"
)
cur = conn.cursor()
try:
    for i in range(1000, 2000):
        # cur.execute(
        #     """INSERT INTO customer 
        #         (customer_name, profile_pic, email, password)
        #         VALUES (%s, %s, %s, %s)""",
        #     (fake.name(), fake.image_url(), fake.email(), fake.password())
        # )
        # cur.execute(
        #     """INSERT INTO seller 
        #         (seller_name, phone_number)
        #         VALUES (%s, %s)""",
        #     (fake.name(), fake.phone_number())
        # )
        # cur.execute(
        #     """INSERT INTO address 
        #         (address, latitude, longitude)
        #         VALUES (%s, %s, %s)""",
        #     (fake.address(), fake.latitude(), fake.longitude())
        # )
        # cur.execute(
        #     """INSERT INTO product 
        #         (category_id, image_link, price, stock, seller_id)
        #         VALUES (%s, %s, %s, %s, %s)""",
        #     (random.randint(1, 6), fake.image_url(), random.randint(1, 5000), random.randint(0, 10), random.randint(5, 999))
        # )
        # cur.execute(
        #     """INSERT INTO review
        #         (product_id, customer_id, rating, review)
        #         VALUES (%s, %s, %s, %s)""",
        #     (random.randint(1, 999), random.randint(2, 999), random.choice([None, 1, 2, 3, 4, 5]), fake.text())
        # )
        # cur.execute(
        #     """INSERT INTO cart (products, customer_id) VALUES (%s, %s)""",
        #     ([random.randint(2, 999) for _ in range(random.randint(1, 10))], i)
        # )
        # cur.execute(
        #     """INSERT INTO payment
        #        (customer_id, amount, payment_status, payment_method, created_at)
        #        VALUES (%s, %s, %s, %s, %s)
        #     """,
        #     (random.randint(1, 999), random.randint(1, 5000), random.choice(["success", "failed"]),
        #      random.choice(["UPI", "Cash"]), fake.date_time())
        # )
        cur.execute(
            """INSERT INTO "orders" (cart_id, address_id, payment_id, customer_id, created_at, status)
            values (%s, %s, %s, %s, %s, %s)""",
            (randint(1, 999), randint(1, 999), randint(1, 999), randint(1, 999),
             fake.date_time_between(start_date=datetime.date(2025, 1, 1)), choice(["pending", "delivered", "shipped"]))
        )
        print(i)
    conn.commit()
finally:
    conn.close()