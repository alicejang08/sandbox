from sys import argv

script, filename = argv

# opening the filename - must 1
target = open(filename, 'w+')

print "This is the first lab: \n Enter 3 lines of text"
a = raw_input("line 1: ")
b = raw_input("line 2: ")
c = raw_input("line 3: ")

target.write(a)
target.write('\n')
target.write(b)
target.write('\n')
target.write(c)

# closing the file - must 2
target.close()

# reading nd printing file data
source = open(filename, "r")
print "Now let's print what we read from the file: "
print source.readline()
source.close()

print "Now let's close the file."
