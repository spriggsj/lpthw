from sys import argv

script, filename =argv
# need to include file name of a txt file
# in the command line when you run the script
# if you are writing or appending (but not reading)
# then a new file will be created with that name
# if one does not already exist

print "We're going to erase %r" % filename
print "if you dont want that hit CTRL-C (^C)"
print " if you dont want that hit RETURN"

raw_input("?")
# waiting for raw input
print "Opening the file"
target = open(filename, 'w')
# 'w' for write 'a' for append 'r' for read
# see pydoc file use space bar to scroll
# w = write
# r+ allows you to read and write
# w+ allows you to write and read
# r (read only) default

print "Truncating the file. Goodbye"
target.truncate()
# truncating erases the file if something is in there

print "now i'm going to ask you for three lines"

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "I'm going to write these to the file"

target.write(line1)
# function writes to line 1
target.write("\n")
# ("\n") new line and etc
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "and finally we close it"
target.close()