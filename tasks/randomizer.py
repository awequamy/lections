import random
import string

letter1 = random.choice(string.ascii_uppercase)
letter2 = random.choice(string.ascii_uppercase)
number = random.randint(1,10)
symbol = random.choice(string.punctuation)
print(letter1, letter2, number, symbol)
password = random.shuffle([letter1, letter2, symbol, number])