
import json
import random
from webbrowser import get

FILE_PATH ='data.json'

def get_data():
    with open(FILE_PATH) as file:
        return json.load(file)
def list_of_products():
    data=get_data()
    return data
def retrieve_data():
    data=get_data()
    print(data,'----')
    id=int(input("enter product id:"))
    product=list(filter(lambda x: x["id"]==id, data))
    return product[0]

# print(retrieve_data())
def get_id():
    data=get_data()
    with open('id.txt','r') as file:
        id=int(file.read())
        # print(id)
        # print(type(id))
        id+=1
    with open('id.txt','w')as file:
        file.write(str(id))
    return id

def create_product():
    data=get_data()
    product={
        "id":get_id(),
        "title":input('vvedite title'),
        "price":input('vvedite price'),
        "description":input('vvedite description')
    }
    data.append(product)
    with open(FILE_PATH,'w') as file:
        json.dump(data,file)
    result={
        'message':"Created",
        'product':product
    }
    return result


def update_product():
    data=get_data()
    flag=False
    id=int(input('enter product id'))
    product=list(filter(lambda x:x['id']==id,data))
    if not product:
        return {'message':'invalid id! Product does not exist!'}
    print(product)

    index=data.index(product[0])
    choice=input('what do u wanna change/update?(title-1,price-2,description-3):')
    if choice=='1':
        data[index]['title']=input('enter new title')
        flag=True
    elif choice=='2':
        data[index]['price']=input('enter new price')
        flag=True
    elif choice=='3':
        data[index]['desciption']=input('enter new description')
        flag=True
    else:
        print('you entered invalid choice to update!')

    with open(FILE_PATH, 'w') as file:
        json.dump(data,file)
    if flag:
        return {'message':"Successfully Updated!",'product':data[index]}
    else:
        return{'message':'Not Updated!'}

def delete_product():
    data=get_data()
    id=int(input('enter product id:'))
    product=list(filter(lambda x: x["id"]==id,data))
    if not product:
        return {'message':'invalid id! Product does not exist!'}
    
    index=data.index(product[0])
    deleted=data.pop(index)
    json.dump(data, open(FILE_PATH, 'w'))
    return {'message':'Deleted!','product':deleted}














