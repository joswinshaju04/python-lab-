'''name:Joswin Shaju
date:03-12-2024'''

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
f=factorial(7)
print(f)