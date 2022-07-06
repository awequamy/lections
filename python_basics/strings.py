# -*- coding: utf-8 -*-
# string = строки, набор последовательных символов, которые мы используем для хранения и представления текстовой информации
# 'Меня зовут Санжар. Мне 20 лет' - str()
# name1 = 'john'
# name2 = """"
# john
# """
# name3 = str('john')

# """"Сейчас мы всё это выведем в терминал"""
# print(name1, name2, name3)
# print(type(name1))
# print(type(name2))
# print(type(name3))
# экранирование - механизм при помощи которого можно вставлять символы которые сложно ввести с клавиатуры
# \n - перенос строки
# \t - горизонтальная табуляция
# \f - перевод страницы
# \r - возврат указателя
# \v - вертикальная табуляция
# name = 'John\nSnow'
# last_name = '\vSnow'
# lastName = '\tSnow'
# print(name, last_name, lastName)
# name = 'Raychel'
# print(name*3)
# print(name + ' John')
# Индексация символов в строке
# name = 'john'
    # h = 3, -3
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# срезы по индексам
# string[start:end:step]
# len() - выводит длину строки
# print(len('hello'))
# name = 'john'
# print(len(name))
# text = 'hello world my name is john snow'
# print(text[0:5])
# print(text[11:])
# print(text[:13:-1])
  
# контратенация строк(соединение)
# word1 = 'hello'
# word2 = 'world'
# probel = ' '
# result = word1 + probel + word2
# print(result)
# print(word1 + probel + word2 + '!!!')

# форматирование строк
#  1. с помощью %
#  2. с .format
#  3. интерполяция строк(f - строки)
# 
# 
# name = input('enter your name: ')
# last_name = input('enter your last name: ')
# print('Hello, mr/ms %s %s' %(name, last_name))


# f- строки
# name = input('enter your name: ')
# last_name = input('enter your last name: ')
# print(f'Hello, mr/ms {name} {last_name}')

