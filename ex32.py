the_test = [[1,2,3],[4,5,6]]
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'bananna']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
# lists aka arrays
#(for key word in python)
#(number could be anything just a temp variable
#(in key word directing python to list)
#(the_count list created above)
#(colon at the end tells python the next line will be indented 4 spaces for block)
#( function print "blah blah blah %d for numbers)
#(%s string, %r represent or raw data) 

for cork in the_test:
	print "This is: %r" % cork
	
for number in the_count:
	print "This is the count: %d" % number
	
for fruit in fruits:
	print "Fruit type: %s" % fruit
	
for i in change:
	print "I got %r" % i

elements = []

for i in range(0, 6):
	print "adding %d to the list" % i
	elements.append(i)
#(or range(6) 0 is implied
#(if range(6) you don't use elements.append)
#elements = range(6)	
for i in elements:
	print "Element was: %d" % i
	