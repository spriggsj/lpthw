def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses" % cheese_count
	print "You have %d boxes of crackers" % boxes_of_crackers
	print "Lets have a party"
	print "Get a blanket.\n"
	
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "Or we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 20

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can do math inside too:"
cheese_and_crackers(10 +20, 5 + 47)

print " and we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 150)