# обработка искючений try and except
# from tarfile import TarError


# ошибки
# IndentationError
# TarError
# TabError




# exceptions
# ZeroDivisionError
# ArithmeticError
# NameError
# IndexError
# KeyError
# ValueError
# ImportError
# BaseException



# try except =

# try: 
#     <body> try>
# except:
#     <body except>

# num1 = int(input('enter any number'))
# print(num1)
# print('smth important')
# try:
#     num1 = int(input('enter any number'))
#     print(num1)
# except:
#     print('u enterred wrong data')
    

# print('smth important')

# import sys
# list_ = [1,2,3,4,5]
# index = int(input('enter any index'))
# try:
#     res = list_[index]
#     print(res)
# except:
#     import sys
#     print(f'oops there is an {sys.exc_info()[1]} error')






# import sys
# list_ = [1,2,3,4,5]
# index = int(input('enter any index'))
# try:
#     res = list_[index]
#     print(res)
# except Exception as e:
#     print(f'oops, we found {e.__class__} error')

# else v try except:
# сработает если в операторе трай ошибка не случилась
# finally cрабатывает всегда

# try:
#     num1 = int(input('enter any number'))
#     num2 = int(input('enter any number'))
#     result = num1/num2
# except ZeroDivisionError:
#     print('we cant divide by zero')
# except ValueError:
#     print('enter correct data')
# else:
#     print(result)


