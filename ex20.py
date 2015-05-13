from sys import argv

script, input_file = argv
# script=python input_file 16.txt (two arguments)
def print_all(f):
	print f.read()
	
def rewind(f):
	f.seek(0)
	# the 0 means go to 0 bytes with seek
def print_a_line(line_count, f):
	print line_count, f.readline()
	
current_file = open(input_file)

print "first lets print the whole file:\n"

print_all(current_file)

print "Now lets rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line =  1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

# to run python ex20.py 16.txt

