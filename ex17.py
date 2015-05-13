from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)


in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready hit return to continue, CTRL-C to abort"
raw_input()


out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright all done"

out_file.close()
in_file.close()
# to run write python ex17.py 16.txt 16b,txt
# 16.txt is the from file
# 16b.txt is the new file
# 16 and 16b can be any file or new file