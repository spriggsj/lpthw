ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there is not 10 things in this list. Let's fix that"

stuff = ten_things.split(' ')
more_stuff = ["day", "night", "song", "frisbe", "corn", "banana", "girl", "boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "adding", next_one
	stuff.append(next_one)
	print "there's %d items now" % len(stuff)
	
print "there we go: ", stuff

print "lets do some things with stuff"

print stuff[1]
print stuff[-1] #whoa fancy
print stuff.pop()
print ' '.join(stuff) #what cool
print '#'.join(stuff[3:5]) #supper stellar
	 