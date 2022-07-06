# SCOPES
# 1) Build in - ithe biggest one , includes 'print', 'len' etc
# 2) Global scope
# 3) Enclosed(non-local) - when in the fuction there is one or more functions
# 4) Local - the smallest one

# def printList(smth):
#     for x in smth:
#         print(x)
# x = 'q'
# # print(x)              wrong
# printList([1,2,3,4,5])
# print(x)

# a = 10  #GLOBAL SCOPE
# print() #build-in
# def hello(): #global
#     a = 'hello world' #local
#     print(a, 'local inside at func')

# hello()
# print(a, 'global')

# x = 'global'
# print(x)
# def enclosed():
#     x = 'enclosed'
#     def local():
#         x = 'local'
#         print(x)
#     print(x)
#     local()
#     print(x)
# enclosed()
# print(x)


# a = 'string'
# def func():
#     print(a)

# func()


# LEGB mean Local - enclosed - global - build in





# num = 10
# def func():
#     def innerFunc():
#         print(num)
#     innerFunc()

# func()



# variable = 100
# def increment():
#     variable+=1
#     print(variable)


# increment()
# variable = 100
# def increment():
#     gloal variable
#     var+=1

# print(variable)
# increment()
# increment()
# increment()
# print(variable)

# def counter():
#     num = 0 
#     def increment():
#         nonlocal num
#         num+=1
#         return num
#     return increment 

# c=counter() #<function counter.<locals>.increment at 0x1045f0670>
# print(c)
# print(c())
# print(c())
# print(c())
# c = counter()
# print(c())

# print(len(dir(__builtins__)))
# smth=abs(-15)
# print(smth)




# spisok = [[1,2,3],[3,3,5]]
# sums = []
# for x in spisok:
#     sums.append(sum(x))
# print(sums)
# print(max(sums))

# or

# res = max([sum(x) for x in spisok])
# print(res)




# alice=[13,15,1]
# john=[5,15,300]
# # res={'Alice':1, 'John':1}
# def compareScores(a,j):
#     score_a=0
#     score_j=1
#     for i in range(0,len(a)):
#         if a[i] > j[i]:
#             score_a+=1
#         if a[i] < j[i]:
#             score_j+=1
#         else:
#             pass 
#     return({'Alice':score_a,"John":score_j})
# print(compareScores(alice,john))



str_ = 'pythoniiist'
dcit_ = {key:str_.count(key) for key in str_}
print(dcit_)




















