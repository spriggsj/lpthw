# ordinal numbers == 12345
# cardinal numbers == 01234

animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platapus']
print animals

for i in animals:
	print i
	
print " "
print "first, second, third, are ordinal numbers but we"
print "Need to count by cardinal numbers: 1, 2, 3"
print "With lists you start at 0"
print " "

for i in range(len(animals)):
	print "index %d in the list is %s" % (i, animals[i])
	
#print animals[1] 
print "%s Rocks!!!" % animals[1]
 