# zip(iterables) - соединяет каждый элемент итерируемых элементов между собой в тип данныx
# ls=[1,2,3]
# ls2=[100,200,300]
# result=list(zip(ls,ls2))
# print(result)

# a=[1,2,3,4,5]
# b=[10,20,20,40,50]
# c=[100,200,300]
# result=list(zip(a,b,c))
# print(result)

# Zip for creating dictionaries
# d_keys=['host_name','location','vendor','model','ios', 'ip']
# d_values=['london_r1','Bishkek', 'cisco','3351','15.4', '10.225.02.443']
# result=(dict(zip(d_keys, d_values)))
# print(result)
# data={
#     'r1':['london_r4','Bishkek', 'cisco','3351','15.4', '10.225.02.543']
#     'r2':['london_r2','Bishkek', 'cisco','3351','15.4', '10.225.02.483']
#     'r3':['london_r1','Bishkek', 'cisco','3351','15.4', '10.225.02.543']
# }
# london_data={}
# for key in data.keys:
#     london_data[key]=dict(zip(d_keys,data[key]))
# print(london_data)

        
# all and any
# all gives back True if all the element in object are true
# ls=[False,1,'stroka',True]
# print(all(ls))

# ip='10.221.313.1'
# result=all(i.isdigit() for i in ip.split('.'))
# print(result)

# any gives back true if 1 or moe elements are true



# from operator import truediv


# def igone_commmand(command):
#     ''''
#     the given function check if there ayn word from the ingore list. True if there is, False if thhere is not
#     '''
#     ignore=['rm -rf','alias','reset']
#     for word in ignore:
#         if word in command:
#             return True
#     return False
# print(igone_commmand('sudo rm -rf user'))

# ignore=['rm -rf','alias','reset']
# command='sudo rm -rf configurations'
# if any([word in command for word in ignore]):
#     raise Exception('invalid command')
# print('vse ok')



from random import choices
from string import letters, digits
from itertools import repeat
quantity_pass=int(input('enter quantity of passwords u want'))
print({
    f for f in repeat(lambda x,y: ''.join(),quantity_pass) 
})

















































