#Exercise 16
"""
WARNING: THE FOLLOW PROGRAM DELETES A FILE AND WRITES
A NEW ONE IN ITS PLACE!!!!!!!!!!!!!!!
"""
#Erase file
from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CRTL-C."
print "If you do want that, hit ENTER."

raw_input("?")

print "Opening file..."
target = open(filename, 'w')

print "Truncating file...Goodbye!"
target.truncate()

#write file
print "Now I'm going to ask for 3 lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "Writing to file."

target.write(line1)
target.write("\n")
target.write(line2) 
target.write("\n")
target.write(line3)
target.write("\n")

print "Closing file..."
target.close()