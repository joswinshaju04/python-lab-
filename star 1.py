'''author=Joswin Shaju
date:20/11/24'''

r=int(input("enter the row:"))
for i in range(r):
    for j in range(1+i):
        print("*",end=" ")
    print()
print()

for i in range(r-1,-1,-1):
    for j in range(1+i):
        print("*",end=" ")
    print()
print()

for i in range(r+1):
    for j in range(r-i):
        print(' ',end=" ")
    for k in range((2*i)-1):
        print("*",end=" ")
    print()
print()

for i in range(r,-1,-1):
    for j in range(r-i):
        print('',end="  ")
    for k in range((2*i)-1):
        print("*",end=" ")
    print()
print()
