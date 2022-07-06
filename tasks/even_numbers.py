ls = []
for i in range(0,101):
    if i%2==0:
        ls.append(i**2)
    elif i%2!=0:
        ls.append(i)
print(ls)