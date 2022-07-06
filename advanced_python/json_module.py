# JavaScript Object Notation
# единый формат хранения и передачи данных между компьютерами сервисами приложениями и языками програмирования через сеть Интеренет
# <filename.json>
# {
#     'id':1
#     'author':'john'
#     'posts':[]
# } это json
# JS object=={}
# Py dict=={}
# JSON={}


# процессы сериализации данных и их десериализация

# Сериализация(запись данных в JSON) = its a translation from python dictionary to json format(либо сохранить всё в файл либо сохраняем просто как текстовые данные)
# using  methods:
# 1) Dump - метод который записывает объект в pythone в файл в формате json
# 2) Dump - метод который записывает объект в pythone в string в формате json
# Десериализая(чтение данных из JSON) = traslation from json format to python dictionary
# using methods:
# 1) load - метод который считывает  файл в формате json и переводит его в python dictionary
# 2)loads - метод который считывает  string в формате json и переводит его в python dictionary


import json
from operator import truediv
# from json import load
from urllib.request import urlopen
# ----------------------------------------------
# пrоцесс десериализации
# data=urlopen('https://randomuser.me/api/')
# print(type(data))
# print(data)
# generate_to_dict=json.load(data)
# print(generate_to_dict)


# with open('downApi.json','r')as file:
#     # data=file.read()
#     # print(data)
#     print(type(data))
#     user=json.loads(data)
#     print(user)
    # print(type(data))


# процесс сериализации
# dict_={
#     'name':'john',
#     'last_name':'snow',
#     'status':True,
#     'wife':None,
#     'children':False
# }

# with open('new.json','w') as file:
#     json.dump(dict_,file)

dict_={
    'name':'john',
    'last_name':'snow',
    'status':True,
    'wife':None,
    'children':False
}


string=json.dumps(dict_)
print(string)
print(type(string))


