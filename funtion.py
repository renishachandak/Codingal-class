def recur_factorial(n):
  if n == 1:
    return n
  else:
    return n*recur_factorial(n-1)
num = int(input("Enter Your Number"))
if num < 0:
    print("There is no recur factorial of negative number")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print("The Factorail of ",num," is ",recur_factorial(num))

def add(x,y):
  return x + y
def subtraction(x,y):
  return x - y
def multiply(x,y):
  return x*y
def divide(x,y):
  return x / y

num1 = int(input("Enter Your First Number:"))
num2 = int(input("Enter Your Second Number"))

print("Sum:", add(num1,num2))
print("Subtraction", subtraction(num1,num2))
print("Multiply:", multiply(num1,num2))
print("Divide:", divide(num1,num2))

num=123

rev=0
temp=num
while(temp>0):
   rem=temp%10
   rev= rev*10+rem
   temp=temp//10

print(rev)   