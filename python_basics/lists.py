# list - mutable последовательный тип данных который из себя представляет коллекцию каких либо символов
# my_list = [1, 'string', False, [1,2,3]]
# print(my_list)
# print(type(my_list))
# 1. list(<>)
# my_list = list('hello world')
# print(my_list)
# 2. range - возвращает последовательность элементов (числа)
# a = list(range(5,15))
# print(a)
# 3. []
# my_list = []
# print(type(my_list))
# print(my_list)
# print(dir(list))
# append(element) = добавляет элемент в конец списка
# list_ = [1,2,3]
# print(list_)
# list_.append(5)
# list_.append([1,2,3])
# print(list_)
# extend(element[iterable]) - расширяет список добавляя элемент
# list_ = [1,2,3]
# list_.extend('hello')
# print(list_)
# insert(<index>, <element>) - добавляет элемент по указанному индексу
# list_ = ["string", 2, 3, False]
# list_.insert(1, [1,2,3,None])
# list_.insert(2,1)
# print(list_)
# print(list_[5])
# print(list_[1] [3])
# print(list_[1:5])
# print(len(list_)
# index.(element, [start], [end]) - овзвращает индекс элемента
# ls = [1,2,33, 3, 4, 4, 5, 'hello']
# print(ls.index(4, 5))
# if 'hello' in ls:
#     print("hello in in ls with index:", ls.index('hello'))
# count(element) = колличество вхождений element в спискe
# ls = [1,2,3,4,5,5,5,5,5,5,5,5,5,1]
# result = ls.count(5)
# print(result)
# remove(Element) = удаляет элемент
# pop([index]) = тоже удаляет по индексу но если индекс не указан то удаляет последний элемент
# ls = [5,1,2,3,4,5]
# ls.remove(5)
# ls.remove(5)
# deleted = ls.pop(0)
# print(deleted)
# print(ls)
# sort([reverse =True/False], [key=<>]) = сортирует список
# ls = [5,1,2,3,4,5]
# print(ls)
# ls.sort ()
# print(ls)
# ls = ['hi', 'lol', 'London']
# ls.sort(key=len)
# print(ls)


ls = [1, 'hi', 3]
ls[1] = 1
print(ls)
