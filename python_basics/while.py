# types =[str,int, float, list, tuple]
# for value in types:
#     print(value)
#     passprint(value, True if "_iter_"in dir (value) else False)
# name_lists = ['ermek', 'Aidana', 'tima']
# for name in name_lists:
#     if name== 'Aidana':
#         continue
#     print(f'Hi {name}')
# sred = len(name_lists)//2
# name_lists.insert(sred, 'ramazan')
# for name in name_lists:
#     if name == "ramazan":
#       break
#     print(f'hi {name}')


# a = bool(23)
# while a:
#     if input('enter your name ') in "war drugs black".split():
#         print('You are blocked')
#         b
# crud =  create read update delete

# EMAILS = []
# while True:
#         print('1) input email 2) show emails 3) delete email')
#         choices = int(input('enter ur choice 4) stop WHILE 5) rename'))
#         if choices == 1:
#             email = input('enter ur email')
#             if email.endswith('@gmail.com'):
#                 EMAILS.append(email)
#             else:
#                 print('invalid email')
#         elif choices == 2:
#             print(EMAILS)
#         elif choices == 3:
#             email = input('enter email that u wanna delete')
#             if email in EMAILS:
#                 # index = EMAILS.index(email)
#                 # EMAILS.pop(index)
#                 EMAILS.remove(email)
#                 print("u sucessfully deleted email")
#             else:
#                 print("email does not exist")
#         elif choices == 4:
#             break
#         elif choices == 5:
#             email == input('enter email')
#             if email in EMAILS:
#                 new_email = input("enter ur new email")
#                 if email.endswith('@gmail.com'):
#                     EMAILS.append(email)
#                     EMAILS.remove(new_email)
#         else:
            # print('error !!')
    
for i in range(5):
    if i == 3:
        break
    print(i)

