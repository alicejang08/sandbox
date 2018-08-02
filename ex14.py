from sys import argv

script, user_name, first, second = argv
prompt = '*** '

print "Hi %s, I'm the %s script." % (user_name, script)
print "You will be the %s." % first
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)
print "Hm...city please"
second = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r comuter. Nice.
Plus these two words: %r and %r.
""" % (likes, lives, computer, first, second)
