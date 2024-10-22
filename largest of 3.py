'''Author:Joswin Shaju
Date:22/10/1024'''

num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
num3=int(input("enteer third number:"))
if num1>num2 and num1>num3:
    print("the largest number is:",num1)
elif num2>num3 and num2>num1:
    print("the largest number is:",num2)
else :
    print("the largest number is:",num3)