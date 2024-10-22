'''Author:Joswin Shaju
Date:22/10/1024'''

temp=int(input("Enter temperature:"))
ch=input("Is this in (C)elcius or (F)ahrenheit?")
if ch=="C":
    cof=(9/5*temp)+32
    print(temp, "Celcius is",cof, "Fahrenheit")
elif ch=="F":
    foc=5/9*(temp-32)
    print(temp, "Fahrenheit is",foc,"Celcius")
else:
    print("ivalid syntax")
