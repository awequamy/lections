 
# start = int(input("Enter the start of range: "))
# end = int(input("Enter the end of range: "))
# list1 = []
# for num in range(start, end + 1):
#     if num % 2 == 0:
#         list1.append(num)
#         print(num, end = " ")


# a = list(range(0,200))
# list1= []
# for i in a:
#     if i%2==0 and i%3==0:
#         list1.append(i)
# print(list1)



# ls = []
# for i in range(0,101):
#     if i%2==0:
#         ls.append(i**2)
#     elif i%2!=0:
#         ls.append(i)
# print(ls)


# new_list = [expressions, for item iterable <if conodition == True>]

# list - comprehention - это упрощенный подход к созданию списков который задействует цикл for а такжe инструкции if  для определения того чтобы окажется добавлено в наш список

 
# start =0 #int(input("Enter the start of range: "))
# end =100 #int(input("Enter the end of range: "))
# list1 = []
# for num in range(start, end, 2):
#     list1.append(num)
# print(list1)

# new_list = [i for i in range(0,100,2)]
# print(new_list)

# ls = [i**2 for i in range(0,11)]
# print(ls)

# fruits = ['apple', 'banana', 'kiwi', 'mango', 'limon']
# ls = [x.capitalize() for x in fruits]
# print(ls)
# ls = [x for x in fruits if 'a' in x]
# print(ls)

# lls = []
# list_ = [[1,2,3], [4,5,6], [7,8,9]]
# for innerlist in list_:
#     for num in innerlist:
#         lls.append(num)
# print(lls)




# ls=[x for innerlist in list_ for x in innerlist]
# print(ls)

# import datetime
# start = datetime.datetime.now()
# ls = []
# for x in range(1,100_000_000):
#     ls.append(x)
# finish = datetime.datetime.now()
# diffrence = finish-start
# print(diffrence)
# ls = [x for x in range(0,200) if x%2==0 and x%3==0]
# print(ls)

 


# ls = [x+10 if x==8 else x+1 for x in range(0,10)]
# print(ls)

