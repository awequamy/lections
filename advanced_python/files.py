# работа с файлами 
# каретка -указатель 
# open(<путь к нашему файлу>)
# file=open(/Users/bermet/desktop/Python/summaries/files.py) #абсолютный путь
# file=open('files.py')#относительный путь
# print(file)


# режимы работы с файлами
# r/r+ (read)
# w/w+ (write)
# a/a+ (append)
# t,b,x



# file=open('/Users/bermet/desktop/Python/advanced_python/text.txt', 'r')
# data=file.read()
# print(type(data))
# data=data.split('\n')
# print(data)
# print(type(data))

# file=open('/Users/bermet/desktop/Python/advanced_python/text.txt')
# data=file.readlines(4)
# print(data)
# file.close

# file=open('text.txt', 'w+')
# file.write('Hello world!\nMy name is John snow')
# print(file.read())
# file.close

# file=open('text.txt','a')
# file.write('\nJohn snow bastard and king')
# file.close()


# file=open('text1.txt','x')
# file.close()


# контекстный менеджер
# with open('text.txt','r') as file:
#     data=file.read()
#     print(data)





# diffrence write writelines

# ls=['hello world!','My names is John Snow!','Im 35 years old!']
# with open('text.txt','w') as f:
#     f.writelines(line +'\n' for line in ls)
# file.tell() - возвращает индекс где находится указатель



# file.seek(<int>) - перемещает указатель на указанный integer index



from PIL  import Image
import pytesseract
import re 


# def get_imei_codes(list_images):
#     list_of_imeis=[]
#     for image in list_images:
#         string=pytesseract.image_to_string(image)
#         print(string)
#         list_of_imeis.append(re.findall(r'IME.\d.\s\d+',string))
#         print(list_of_imeis)
#     with open('imicodes.txt','w') as file:
#         for x in list_of_imeis:
#             for i in x:
#                 file.write(f'{i}\n')

        

# list_images=['imei.jpg']
# get_imei_codes(list_images)
















