#

code = input("\nenter the coded text: ")
distance = int(input("enter distance value: "))
plainText = ""
for ch in code:
    ordvalue = ord(ch)
    cipherValue = ordvalue - distance
    if cipherValue < ord('a'):
        cipherValue = ord('z') - distance - (ord('a') - ordvalue - 1)
    plainText += chr(cipherValue)
print (plainText)
print ("")

#