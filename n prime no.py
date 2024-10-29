'''date:29/10/24
Author:Joswin Shaju'''

lim=int(input("enter the number:"))
for i in range(2,lim+1):
    isPrime=True
    for j in range (2,(i//2)+1):
        if i%j==0:
            isPrime=False
        break
    if isPrime:
        print(i,end=" ")

