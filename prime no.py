'''date:29/10/24
Author:Joswin Shaju'''

num=int(input("enter the number:"))
for i in range (2,(num//2)+1):
    if num%i==0:
        break
if i==num//2:
    print (f"the given number {num} is prime")
else:
    print(f"the given number {num} is not prime")
