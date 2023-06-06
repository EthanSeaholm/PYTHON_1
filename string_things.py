#

# subscript operator

name = "ethan"
print ("")

for index in range(len(name)):
    print (index, name[index])
print ("")

# substring slicing

print (name[0:3])

print (name[2:])            # endpoint not specified, will go to the end

print (name[0:3:1])         # a step?

print (name[-3])

# testing for a substring with the in operator

fileList = ["\nmyfile.txt", "myprogram.exe", "yourfile.txt"]
for fileName in fileList:
    if ".txt" in fileName:
        print (fileName)

# string methods

sentence = input("\nenter a sentence or phrase: ")
listOfWords = sentence.split()
print ("there are", len(listOfWords), "words")
sum = 0
for word in listOfWords:
    sum += len(word)
print ("the average word length is:", sum/len(listOfWords))
print ("")

#