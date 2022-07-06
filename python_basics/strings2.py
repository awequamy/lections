# методы строк
# dir() - функция которая вытаскивает методы типов данных
# print(dir(str))
# '<соединитель>' - .join(<массив который нужжно соединить) - осединяет массив из строк по соединителю в одну строку
# ls = ('milk', 'chocolate', 'water')
# joined = "!".join(ls)
# print(joined)
# split - разделитель
# text = ('milk, chocolate, water')
# splited = text.split('. ')
# print(splited)
# joined = ", ".join(splited)
# print(joined)

# replace(<old value>, <new value>, [count])
# text = 'ha ha ha ha'
# result = text.replace('ha', 'john')
# print(result)
# print(text)

# strip() - убирает пробелы в начале и в конце
# rstrip() - начало
# lstrip() - конец
# text = input("input fio")
# print(text.strip())



# count() - counts
# text = 'hello world! I\'m from Earth!'
# result = text.count('l')
# print(result)

# index(<value>, [ start], [ end]) - выводит индекс значения value в нашей строке
text = 'hello world!  This is Kima!'
result = text.index('!', 12)
print(result)



