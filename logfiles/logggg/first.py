import random
from datetime import datetime

def generate_ip_address():
    return str(random.randint(0, 255)) + '.' + str(random.randint(0, 255)) + '.' + str(random.randint(0, 255)) + '.' + str(random.randint(0, 255))

with open("router_log.txt", "w") as file:
    for i in range(2000):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{now}] Router: New connection from {generate_ip_address()}\n")
