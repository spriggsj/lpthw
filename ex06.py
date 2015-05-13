x = "There are %d types of people" % 10
binary = "binary"
do_not = "Don't"
y = "Those who know %s and those who %s" % (binary, do_not)

print x
print y

print "I said: %r" % x
print "I also said: '%s'." % y

hilarious = 'false'
joke_evaluation = "Isn't that joke funny?! %r" # %r is not defined until l15

print joke_evaluation % hilarious 

w = "this is the left side of ..."
e = "a string and this is the right"

print w + e