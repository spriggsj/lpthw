from sys import argv

script, filename = argv

print "to open hit return"

raw_input("?")

target = open(filename, 'r')

print "and close"

target.close()
# use ex15 for reference to read

