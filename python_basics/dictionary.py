# dictionary() - словарь это упорядочная коллекция элементов. каждый элемент в словаре содержится в паре ключ: значение
# ключи - они  unique + immutable(str,int,tuple etc) Тогда как значениеями могут выступать любые тыипы данных
# dict = {
#     'brand': 'ford',
#     'mode': 'mustang',
#     'year' : '1964'
# }
# print(dict)
# print(type(dict))
# hash tables, aссоцивтиный массив, dictionary, объекты

# any_tuple = (1,2,3)
# print(type(any_tuple))

# any_dict = {}
# print(type(any_dict))
# key_values = {'key': 'value', 'key2' : 'value2'}



user_info = {
    'first_name': 'john',
    'last_name' : 'snow',
    'age': 24,
    'email': 'johnsnow@gmail.com',
    'role': 'moderator',
    'list': [1,2,3],
}
    # 'first_name': "Raychel"

# print(user_info)
print(user_info['first_name'])
print(user_info.get('age'))
# print(dir(user_info))
# for items in user_info.items():
#     print(items)
# print(user_info.keys())
# user_info['height'] = 185
# print(user_info.keys())
# for keys in user_info.keys():
#     print(keys)
# for value in user_info.values():
#     print(value)

# pop() - удалет элемент по определенному ключу

# popitem() - удаляет последнию пару 
# print(user_info)
# user_info.pop('list')
# user_info.pop('email')
# user_info.pop('list')
# user_info.popitem()
# user_info.popitem()
# print(user_info)

# setdefault(key, [default value]) - работает так же как и get но если акого ключа нет то он создает новую пару ззначений
# 1) способ применения это получение значений
# dict = {'name' : 'john', 'age':23}
# result = dict.setdefault('age')
# print(result)
# 2) способ
# dict = {'name' : 'john', 'age':23}
# result = dict.setdefault( 'address', 'toktogula street')
# print(dict)




# print(user_info)
# user_info.update({'first_name': "raychel"})
# user_info.update({'height': 185})
# print(user_info)


# from logging import exception


# roles = {
#     0:'Admin',
#     1:'moderator',
#     2:'vendor',
#     3:'customer',
#     4:'guest'
# }

# users =[
#     {
#         'id' : 0,
#         'name':'john',
#         'role':roles[0]
#     },
#        {
#         'id' : 1,
#         'name':'raychel',
#         'role':roles[3]
#     },
#        {
#         'id' : 2,
#         'name':'aibek',
#         'role':roles[4]
#     }
# ]
# product = {
#     'id': 1,
#     'title':'samsung',
#     'descriptioin':"lorem",
#     'price': 1000

# }
# # print(users)
# # print(product)
# user_id = int(input("введите ваш id"))

# if users[user_id]['role']==roles[0]:
#     product["description"]=input('enter new description of a product')
# else: 
#     raise Exception('u dont have enough power')
# print(product)