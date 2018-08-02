# this line is for using argv argument
from sys import argv

# TODO: need to lean what's os.path for
from os.path import exists

# declare some parguments
script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we coud do these two on one line, how?
in_file = open(from_file, 'r')
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()
