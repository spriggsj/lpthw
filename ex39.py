#create a mapping of state to abbreviation
states = {
	'oregon': 'or',
	'florida': 'fl',
	'California': 'ca',
	'new york': 'ny',
	'michigan': 'mi'
}

#create a basic set of states and some cities in them
cities = {
	'ca' : 'hanford',
	'mi' : 'detroit',
	'fl' : 'jacksonville'
}

#add some more cities
cities['ny'] = 'new york'
cities['or'] = 'portland'

#print out some cities
print '_' * 10
print "ny state has: ", cities['ny']
print "or state has: ", cities['or']

#print some states
print '_' * 10
print "michigans abbreviation is: ", states['michigan']
print "floridas abbreviation is: ", states['florida']

#now do it by using the state then cities dictionary
print '_' * 10
print "michigan has: ", cities[states['michigan']]
print "florida has: ", cities[states['florida']]

#print every state abbreviation
print '_' * 10
for state, abbrev in states.items():
	print "%s is abbreviated %s and has %s" % (
		state, abbrev, cities[abbrev])
		
print '_' *10
#safely get an abbreviation from state that might not be there
state = states.get('texas', None)

if not state:
	print "sorry no texas"
	
#get a city with a default value
city = cities.get('tx', 'does not exist')
print "the city for the state 'tx' is: %s" % city