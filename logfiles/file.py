import random

def generate_ip_address():
    return str(random.randint(0, 255)) + '.' + str(random.randint(0, 255)) + '.' + str(random.randint(0, 255)) + '.' + str(random.randint(0, 255))

with open("logfile.txt", "w") as file:
    for i in range(2000): # change the range to generate more or fewer lines
        file.write(generate_ip_address() + '\n')
