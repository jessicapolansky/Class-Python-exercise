#Exercise 1. Uppercase a string.
string1 = input("Tell me something and I'll yell it.  ")
print(string1.upper() + "!!!")

#Exercise 2. Capitalize a string.
string2 = input("Enter a lower case word.  ")
print(string2.capitalize())

#Exercise 3. Reverse a string.
string3 = input("I'll turn your words around: ")
print(string3[::-1])

#Exercise 4. Leetspeak
string4 = input("Let's make your speech L337!: ")
string4 = string4.upper()

for x in range(len(string4)):
    if string4[x] == "A":
        print("4", end = '')
    elif string4[x] == "E":
        print("3", end = '')
    elif string4[x] == "G":
        print("6", end = '')
    elif string4[x] == "I":
        print("1", end = '')
    elif string4[x] == "O":
        print("0", end = '')
    elif string4[x] == "S":
        print("5", end = '')
    elif string4[x] == "T":
        print("7", end = '')
    else:
        print(string4[x], end = '')
print(" ")

#Exercise 5. Long-long vowels
string5 = input("Let's elongate our vowels.  ")
for x in range(len(string5)):
    if x + 1 == len(string5):
        print(string5[x])
    elif string5[x] + string5[x + 1] == "aa" or string5[x] + string5[x + 1] == "ee" or string5[x] + string5[x + 1] == "oo":
        print((string5[x] + string5[x + 1]) * 2 + string5[x], end = '')
    else:
        print(string5[x], end = '')

#Exercise 6. Caesar Cipher
#To decrypt your message, the key must be 13. Message reads: "you must unlearn what you have learned"
from pycipher import Caesar
codeMessage = input("Enter your commands and I'll encrypt them.  ")
oneUseKey = int(input("Enter a number to use as the key: "))
print(Caesar(key=oneUseKey).encipher(codeMessage))
decodeMessage = input("I can decrypt any replies you receive:  ")
print(Caesar(key=oneUseKey).decipher(decodeMessage))
