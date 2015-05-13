i = 0
numbers = []

while i < 6:
	print "At the top i is %d" % i
	numbers.append(i)
	
	i = i + 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i
	
print "The numbers: "

for num in numbers:	
	print num
	
# (Control C will force quit if needed)
#(study drills)
print "\nConverting while loop to function. drill_1"
#(def name(variable):)
#(indent 4 spaces then variable = 0)
#(variable = [list]
#(while variable less then (n)variable:)
#(indent 4 spaces print "what ever: %d" % i)
#(variable.append(i))
#(i = i + 1)
#(print variable)
def drill_1(n): 
	i = 0
	numbers1 = [ ]
	while i < n:
		print "Item: %d" % i
		numbers1.append(i)
		i = i + 1
#or i = i + 4 or what ever
	print numbers1
	
#2 drill
#(needed function drill_1(upper limit))
#(this is where drill_1 gets its value cap and runs until it hits it)

print "\nUsing drill_1 with n = 3"
drill_1(3)

print "\nUsing drill_1 with n = 8"
drill_1(8)

print "\nUsing drill_1 with n = 20"
drill_1(20)

print "\nUsing function drill_3 to allow variable step size"
def drill_3(n, s):
	i = 0
	numbers3 = [ ]
	while i < n:
		print "Item: %d" % i
		numbers3.append(i)
		i = i + s
	print numbers3
	
print "\nUsing drill_3 with n = 12 and s = 3"
print "\n12 being the upper limit and 3 being the step size"
drill_3(12, 3)

#(using a for loop instead of a while loop. Use while loop sparingly)
print "\n drill_5 converting to a for loop"

def drill_5(n, s):
	numbers5 = range(0, n, s)
	for i in numbers5:
		print "Item %d" % i
	print numbers5
	
drill_5(14, 4)

	




