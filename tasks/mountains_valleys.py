N=int(input("enter number of steps"))
S=input("enter U or D")
L=0
V=0
for s in S:
    if s == 'U':
        L += 1
        if L == 0:
            V += 1
    else:
        L -= 1
        
print(V)


# or 



def counting_valleys(n, s):
    current_level = 0
    count = 0
    for i in range(n):
        if s[i] == 'U':
            current_level += 1
        elif s[i] == 'D':
            current_level -= 1
            if current_level == -1:
                count += 1
    return count

n = int(input().strip())
s = input().strip()
result = counting_valleys(n, s)
print(result)