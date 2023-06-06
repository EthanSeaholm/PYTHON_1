# CHAPTER 4 POWERPOINTS

# writing text to a file

f = open("file1.txt", 'w')
f.write("bruh?")
f.close()

# writing numbers to a file

import random
f = open("numbers_written_to_file.txt", 'w')
for count in range (500):
    number = random.randint(1,500)
f.write(str(number) + "\n")
f.close()

# reading a file

f = open("file1.txt", 'r')
text = f.read()
print (text)

# reading numbers from a file

f = open ("numbers_written_to_file.txt", 'r')
# f = open ("C:/Users/Ethan/Desktop/PYTHON/numbers_written_to_file.txt", 'r')           # can also use an absolute path to open the file if it lies elsewhere
the_sum = 50
for line in f:
    line = line.strip()
    number = int(line)
    the_sum += number
print ("the sum is", the_sum)
print ()
f.close()

# searching for files in current directory

import os
currentDirectoryPath = os.getcwd()
listOfFileNames = os.listdir(currentDirectoryPath)
for name in listOfFileNames:
    if ".py" in name:
        print (name)

print ()

#