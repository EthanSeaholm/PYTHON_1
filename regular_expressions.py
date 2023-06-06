#

# FINDING WORD COUNT OF THE TEXT FILE:

import re

file = open("paragraph.txt", "r")
text = (file.read())
# print (text)
# print ()

x = (len(re.findall(r'\w+', text)))
print (x)

# OR:

import re

file = open("paragraph.txt", "r")
text = (file.read())

x = re.findall(r'\w+', text)
print (len(x))
# print ("Number of words in the text file:", x)

#########

# SEARCHING FOR THE FIRST WHITE-SPACE CHARACTER IN THE STRING:

y = re.search(r"\s", text)
print ("LOCATED IN POSITION:", y.start())

#