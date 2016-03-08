#strings review, exercise 6
#prints There are 10 types of people. %d is a placeholder. %10 says the placeholder should be 10
x = "There are %d types of people." %10
binary = "binary"
do_not = "don't"
#placeholders print the value of the varibles binary and do_not
y = "Those who know %s and those who %s." %(binary, do_not)

print x
print y

print "I said: %r." %x
print "I also said: %s" %y

hilarious = False
joke_evaluation = "Isn't that funny? %r "

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e 