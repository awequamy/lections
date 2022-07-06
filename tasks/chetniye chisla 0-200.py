 
start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))
list1 = []
for num in range(start, end + 1):
    if num % 2 == 0:
        list1.append(num)
        print(num, end = " ")
