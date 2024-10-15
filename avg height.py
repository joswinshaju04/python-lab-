'''author: Joswin Shaju
date:15/10/2024'''

n=int(input("enter the no of students:"))
btotl=0
tbh=0
gtotl=0
tgh=0
for i in range (1,n+1):
    gender=input("enter the gender:")
    height=int(input("enter the height in cm:"))
    if gender=="M":
        btotl+=1
        tbh=tbh+height
    else:
        gtotl+=1
        tgh=tgh+height
bavg=tbh/btotl
gavg=tgh/gtotl
print("the average height of boys:",bavg)
print("the average height of girls:",gavg)