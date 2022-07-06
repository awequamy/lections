from ast import Raise
from typing import List

# def sum_of_arguments(a: int, b: int, c:int, d: int) -> int:
#     """
#     Given function returns sum of all four arguments
#     """
#     return a+b+c+d
# print(sum_of_arguments(1,2,3,4))


# # позиционные и именнованные аргументы
# def printParams(a=None,b=None,c=None):
#     print(a, 'is stored in a')
#     print(b, 'is stored in b')
#     print(c, 'is stored in c')

# print(printParams(c=2,b=3))



# def sum_of_arguments(a: int, b: int, c:int, d: int) -> int:
#     """
#     Given function returns sum of all four arguments
#     """
#     return a+b+c+d
# print(sum_of_arguments(1,2,3,4)) #позиционные аргументы
# print(sum_of_arguments(a=5,b=2,d=3,c=4))



# a=[1,2,3]
# b=[4,5,6]
# c=[*a,*b]
# print(c)
# print(*a end='*')



# args, kwargs in Functions

# def printScores(student, *scores):
#     print(f'Students name is: {student}')
#     # print(scores)
#     # print(type(scores))
#     for x in scores:
#         print(f'the score is: {x}')


# print(printScores('John Snow', 100,90,80,55))

# def printPetNames(owner, **pets):
#     print(f'Owner name {owner}')
#     print(pets)
#     print(type(pets))
#     for pet, name in pets.items():
#         print(f'{pets}: {name}')

# print(printPetNames('John Snow', dog = 'lolo', cat ='iuwiu', fish=['gavgav','dori']))

# def getSomeData(a,b,*args,**kwargs):
#     print('parametry a and b', a, b)
#     print(args[0])
#     print(args[-1])
#     print(kwargs['name'])
#     print('Argumenty', kwargs)
#     print('immenovannyi argumenty', kwargs)
# print(getSomeData(1,2,3,4,5, lang='python', name='johnSnow', car='bmw'))
import random
import string
# def conc_strings(str1,str2):
#     import random
#     res = random.randint(1,10)
#     return str1+str2+str(res)

# print(conc_strings('hello', ' world'))

# def generate_nickname(name, second_name):
#     random_num = random.randint(100000,999999)
#     return name + second_name + str(random_num)

# name = input('enter ur name')
# second_name = input('enter ur second name')
# generate_nickname(name, second_name)

# result = generate_nickname(name, second_name)
# print(result)



def generate_random_password(len_, lang):
    import string as s
    import random
    random_string = ''.join(
        random.choice(s.ascii_lowercase + s.digits) for i in range(0,len_)
        )
    return random_string

print(generate_random_password(15, 'eng'))


















