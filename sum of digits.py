'''author: Joswin Shaju
date:15/10/2024'''

num=int(input("enter the digit:"))
sum=0
while num>0:
    dig=num%10
    sum+=dig
    num=num//10
print(sum)