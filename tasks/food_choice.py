import random

ls = ['plov','manty','kuurdak', 'lagman','rolls']
p=0
m=0
k=0
l=0
r=0
for i in range(0,10000):
    choice = random.choice(ls)
    print(choice)
    if choice.lower() == 'plov':
        p += 1
    elif choice.lower() == 'kuurdak':
        k += 1
    elif choice.lower() == 'manty':
        m += 1
    elif choice.lower() == 'lagman':
        l+=1
    elif choice.lower() == 'rolls':
        r+=1
# print(f'plov; {p},\nmanty: {m}, \nlagman {l}, \nkuurdak {k}')
dc ={'plov': p, 'manty':m,'kuurdak':k,'lagman':l, 'rolls':r}
# print(dc.items())
result = sorted(dc.items(), key=lambda x:x[1])
# print(result)
winner= result[-1]
print(f'the winner is {winner[0]}, it got {winner[1]}')
