#exercise 18
#this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg: %r" % (arg1, arg2)

#*args is pointless!!!
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

#takes no arguments
def print_none():
    print "I got nothing."


print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

#Exercise19
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of a crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"	
    print "Get a blanket.\n"


print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)


print "OR, we can use variables from from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the, variable and math: "
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)