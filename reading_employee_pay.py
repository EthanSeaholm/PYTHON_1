#

file = input("\nName of the file you would like to read from: ")
print ()
opened_file = open(file, 'r')
text = opened_file.read()
print (text)
print ()

#