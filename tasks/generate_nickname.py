import random
def generate_nickname(name, second_name):
    random_num = random.randint(100,99)
    return name + second_name + str(random_num)

name = input('enter ur name')
second_name = input('enter ur second name')
# generate_nickname(name, second_name)

result = generate_nickname(name, second_name)
print(result)