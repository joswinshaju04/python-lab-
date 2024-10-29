'''date:29/10/24
Author:Joswin Shaju
to count the no of vowels & consonants in a string(python)'''

str=input("enter the string:")
vowel_count=0
consonat_count=0
vowels="AEIOUaeiou"
for char in str:
    if char in vowels:
        vowel_count+=1
    else:
        consonant_count=+1
print(f"the string has {consonant_count} consonants")
print(f"the string has {vowel_count} vowels")

