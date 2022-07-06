def generate_random_password(len_, lang):
    import string as s
    import random
    random_string = ''.join(
        random.choice(s.ascii_lowercase + s.digits) for i in range(0,len_)
        )
    return random_string

print(generate_random_password(20, 'eng'))