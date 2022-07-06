# functions - are created with 'def <name of function>'. there we can share the setting of it, then add ':'
    # <body>#some code
    # <return> its the ttging we give back
# <name of function> (<5,6> #argument)

# параметры функции это переменные которые будут принемать наша функция для того что бы мы сомгли работать с данными которые передабтся в юту функцию
# аргументы это данные которые мы передаем для парамаров при вызове функции
# return нужен для того чтобы функция что-то возващала и для того чтобымы могли с результатом действия функции. Является необязательным оператором 



# spisok=[]
# result = spisok.append(1)
# print(spisok)
# print('the result of an action is:', result)
# result2 = spisok.pop()
# print('the result of an action is:', result2)


# def sumTwonums(num1, num2): #paramerty
#     result = num1+num2
#     print(result)
#     # return result


# sumTwonums(5,5)


# def isEven(num):
#     # return True
#     if num%2==0:
#         return True
#     else:
#         return False
# print(isEven(5))
# # a = 10
# # b = int(input('enter any number'))
# # print(isEven(5))
# # print(isEven(a))
# # print(isEven(b))

# def isEven2(num: int) -> bool:
#     """
#     the given function check if the number entered is even or not
#     """
#     if num%2 ==0:
#         return True
#     return False 

# isEven
# isEven2


# the given function which return reverse of a string
 
# def isPalindrome(word):
#     return word == word[::-1]
#     """
#     the given function checks if the word entered is a pa lindrome or not
#     """
    
# word = input('enter any word')
# result = isPalindrome(word)
 
# if result:
#     print("Yes")
# else:
#     print("No")

from ast import Raise
from typing import List

# def isPalindrom(words):
#     result = []
#     for word in words:
#         if word.lower() == word[::-1].lower():
#             result.append(word)
#     return result

# any_words = ['apa','ono','hskvsjl;', ' john', 'dovod']
# print(isPalindrom(any_words))

# def func():
#     print('hello world')

# func()
# default parameteres
# def print_welcome(name: str = 'user') -> str:
#     print(f'welcome, {name}!')

# print_welcome('bermet')



# def getPercentage(money: float, period : int) -> float:
#     """The given function will return final amount of money after some years"""
#     if money < 30000:
#         raise Exception('the given amount of money is too small bro!  The minimum is 30 000 soms')
#     if period<3:
#         raise Exception('the given number of years is too small bro! Tghe minimum is 3 years!')
#     i = 0
#     while i < period:
#         money = money*1.1
#         i+=1
#     return money
    
# print(getPercentage(300000,5))

def reverseSentence(string):
    reversed_string = string.split()
    reversed_words = list(reversed(reversed_string))
    print(" ".join(reversed_words))

string = input('enter any sentence')
reverseSentence(string)

















