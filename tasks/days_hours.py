# seconds = int(input('enter number of seconds'))
# minutes = seconds/60
# seconds = seconds%60
# hours = minutes/60
# minutes = minutes%60
# days = hours/24
# hours = hours%24
# print(days:, hours :, )

fib1 = fib2 = 1
 
n = int(input())
 
print(fib1, fib2, end=' ')
 
for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')

    