# print("welcome to calculator")
# x=float(input("input a number"))
# y=float(input("input a number"))
# z=input("input an action")
# if z == "+":
#   print (x+y)
# elif z == "-":
#   print (x-y)
# elif z == "/":
#   if y == 0:
#     print ("Sorry, you cant devide by zero")
#   else: 
#     print(x/y)
# elif z == "*":
#   print (x*y)
# elif z == "^":
#   print(pow(x,y))
# else: 
#   print ("error")



# or



def add(n1,n2): return n1+n2
def substract(n1,n2): return n1-n2
def multiply(n1,n2): return n1*n2
def divide(n1,n2):
  try:
    return n1/n2
  except ZeroDivisionError:
    return "you cant divide by zero"

def main():
  try:
    n1=float(input("input a number"))
    n2=float(input("input a number"))
  except ValueError:
    print('you entered wrong type of data')
    main()

  operator = input('enter an action(+,-,*,/):')

  result = None
  if operator == '+': result = add(n1,n2)
  elif operator == '-': result = substract(n1,n2)
  elif operator == '*': result = multiply(n1,n2)
  elif operator == '/': result = divide(n1,n2) 
  else:
    print('you entered wrong type of data')
  
  print(f'the result is {result}')
  q = input('do u wanna continue using our PERFECT calculator? \n(Yes/No)')
  if q.lower() == "1":
    main()
  elif q == "no":
    print('Thanks for using our PERFECT calculator! BYE BYE!')

main()



    


