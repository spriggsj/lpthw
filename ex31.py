print "You enter a dark room with two doors. Do you go through door 1 or door 2?"

door = raw_input("> ")

if door == "1":
	print " There is a huge bear eating cheese cake. What do you do?"
	print " 1. Take the cake"
	print " 2. Scream at the bear"
	
	bear = raw_input("> ")
	
	if bear == "1":
		print "The bear eats your face off"
	elif bear == "2":
		print "The bear bites your leg off"
	else:
		print "Well doing %s is probably better. The bear runs away" % bear
		
elif door == "2":
	print "You stare into the abyss of Cthulhu's retina"
	print "1. Blueberries"
	print "2. yellow jackets"
	print "3. Understanding revolvers yelling melodies."
	
	insanity = raw_input("> ")
	
	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello"
	else:
		print "Your insanity rots your eyes into a pool of muck"

else:
	print "You stumble around and fall into an open pit of knives"