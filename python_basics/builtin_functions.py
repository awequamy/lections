# map()
# filter()
# lambda()
# enumerate()

from ast import Lambda
from hashlib import new
from typing import Iterable


# Lambda function- анонимная функция которая без названия. Могут принимать сколько угодно аргументов но всегда возвращают только одно выражение
# def sum_args(a,b):
#     result=a+b
#     return result


# def sum_args2(a,b): return a+b

# print(sum_args2(1,2))
# print(sum_args(1,2))

# sum_arg = lambda a,b: a+b
# print(sum_arg(1,2))



# x = lambda a,b,c: a+b+c
# print(x(2,3,4))


# def Fuct(n):
#     return lambda a: a*n

# multiplyer = Fuct(2)
# print(multiplyer(11))


# ls = ['def','ivan', 'john', '',' ']
# ls2 = sorted(ls,key=len)
# print(ls2)


# map(function, iterable) -> применяет функцию к каждому элементу в последовательности и возвращает mapobject(итератор) с результатами
# for ex c помощью map можно выполнять преобразования элементов. перевести все строки в верхний регистр
# ls  = ['one','two','three', 'dict']
# result =list(map(str.upper, ls))
# print(result)

# ls = ['1','2','3','4']
# result = list(map(int, ls))
# print(result)

# names=['john','naruto','sasuke','aibek']
# result = list(map(lambda x: f'hello mr/mrs {x}', names))
# print(result)
# numbers =[1,2,3,4,5]
# numbers2=[100,200,300,400,500]
# result =list(map(lambda x,y: x*y, numbers,numbers2))
# print(result)
# dc = {1:2,3:4,5:6}
# result = dict(map(lambda items: (items[0], str(items[1])), dc.items()))
# print(result)



# filter(function, Iterable) применяет функцию ко всем элементам iterable object и возвращает filter object () с теми объектами для которых функция вернула true
#  
# list_of_strings = ['one','two','list','', '10','1','johnsnow']
# result=list(filter(str.isdigit, list_of_strings))
# print(result)

# ls = [10,11,102,211,512]
# result = list(filter(lambda x:x%2!=0,ls))
# print(result)


# ls =  ['john','one','two','yoyo']
# result = list(filter(lambda x: len(x)>=4,ls))
# print(result)

# enumerate(iterable)
# ls = ['str1','str2','str3']
# # i = 0
# # for x in ls:
# #     print(f'element {x}, index: {i}')
#     # i+=1

# for i, x in enumerate(ls):
#     print(f'element {x}, index: {i}')


# new_list=list(enumerate(ls))
# print(new_list)





















