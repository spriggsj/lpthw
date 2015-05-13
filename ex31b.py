print """
 There once was a princess named Zoe Fae. She was the most beautiful, 
 intelligent, kind, and special child"""
 
print """ One day as she was addressing her royal court she noticed
three small beggars at the bottom of her stairwell. She decided that 
She must help them but which one? Should she pick number 1, number 2,
or number 3"""

beggar = raw_input("> ")

if beggar == "1":
	print """ You have chosen wisely. Number 1 was the most deserving 
	as the other two were just pretending to be poor and had a regular
	scam going outside of all the royal Wallmarts\n
	What should we do your majesty?\n Should we 1 kick them out of the kingdom 
	or \n2 make them clean the royal stables."""
	choice = raw_input("> ")
	
	if choice == "1":
		print "They have been sent away your majesty"
		
	elif choice == "2":
		print "Excellent choice the stables could use a good scrubbing"
	else:
		print "It is a very difficult decision"
		
		
elif beggar == "2":
	print """You have chosen wisely. Number 2 was the most deserving 
	as the other two were evil witches trying to raise money for botox.
	Which they needed because they were very old witches. Number 2 was 
	actually a witch also but a kind good witch. As a reward for you act 
	of kindness she has given you a pony. What will you call your new pony?"""
	
	pony = raw_input("> ")
	print """ %s is a beautiful name for a pony. You two will live hapily
	ever after""" % pony
	
	
	
	
elif beggar == "3":
	print """You have chosen wisely. Number 3 was the most deserving 
	as the other two were neighboring spies from the next kingdom.
	The guards captured the other 2 and has presented them to you for
	your decision on what they should do with them. \n
	Decision 1 give them false information.\n
	Decision 2 grant them a pardon and ask them to stay"""
	
	decision = raw_input("> ")
	
	if decision == "1":
		print """They take their new information back to their kingdom
		where it is received by their king. He decides that they are
		not very good spies and orders them to apologize to you and your
		royal court"""
	elif decision == "2":
		print """ They accept your offer and become loyal subjects.
		They eventually decide on a way to repay you for your kindness.
		They buy you a pony. What will you call your new pony?"""
		
		gift = raw_input("> ")
		print "%s and you ride away knowing you truely are the best princess" % gift
	else:
		print "Of course you can choose anything you like you are the princess"
		
else:
	print """Exactly. Who wants to help beggars anyway. We have a kingdom 
	to run and you can't just help everyone who comes here looking for
	handouts"""
