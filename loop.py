n = int(input("Enter Your Number:"))
isprime=True
for i in range(2,n):
   if(n%i==0):
     isprime=False
     print("Number is not a Prime number")
     break
if isprime==True:
  print("Number is a Prime number")

n = int(input("Enter Your Number:"))
for i in range(1,n+1):
    for j in range(1,i):
      print(j)
    print()  

total_sum = 0
n = 1 

while n <= 10:
  total_sum += n
  n += 1 

print(f"The sum of the first ten natural numbers is {total_sum}")  
 
n = int(input("Enter Your Number"))
for i in range(1,11):
   print(f"{n} x {i} = {n* i}")