# Add info in a file

NAME = "mynotes.txt"

# Open the file:
myfile = open(NAME, 'r')
print('File opened: {}'.format(myfile.name))
contents = myfile.read()

# Print contents
print('The file contents are: ', contents)
myfile.close()

f = open(NAME, 'a')
f.write("THIS IS A TEXT EXAMPLE FOR ADDING TO MY FILE!!!")
f.close()
print('The end')
