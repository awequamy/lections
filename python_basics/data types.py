# -*- coding: utf-8 -*-
# Типы данных в питоне 
# from sqlite3 import IntegrityError
# from tokenize import String
# from types import NoneType
# from typing import Set
# from xmlrpc.client import Boolean


# 1. NoneType - ничего пустота
# 2. Boolean - False True
# 3. Числовые типы данных:
#                         a. Integer(int) - целое число
#                         b. float() - не целые числа
#                         c. complex() - комплексные числа
# 4. списковые типы данных:
#                         a. list(список) - [1, 3, True, None]
#                         b. tuple(кортеж) - (1,2, False)
#                         c. Range(1,3)
# 5. String(str) - строки "hello world"
# 6. Set() - множество 
# 7. Dictionary(dict) - словарь, содержит данные в виде ключа значения{1: - 'one'}
# Mutable(изменяемые типы данных):
#                         a. list
#                         b. set
#                         c. dict
# Immutable(неизменяемые):
#                         a. Boolean()
#                         b. NonType()
#                         c. Integer, float, complex(),
#                         d. Str()
#                         e. tuple()
#                         f. range()

# """"стандартный вывод данных"""

# from turtle import clear


# print("hello world")
# a = input("введите число")
# print(a)
# # type() - выводит тип данных
# print(type(a))
# b = int(input("введите число номер 2"))
# print(b)
# print(type(b))
# print(a,b, "salam")
# min(), max()

# a = [1,2,3]
# print(max(a))
# print(min(a))

# a=2
# b=5
# c=7
# print(pow(a,b,c))

# divmod(a,b) выводит 2 числа. Первое число это рузультат челочисленного деления//'a' на 'b'
# a = 5
# b = 2
# print(12 // 5)
# abs() - выводит абсолютное значение числа
# import math
# a = 5
# print(math.sqrt(a))