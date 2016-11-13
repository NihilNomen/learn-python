#exercise 35
from sys import exit

def gold_room():
	print "This room is full of gold. How much do you take?"

	choice = raw_input("> ")
	if "0" in choice or "1" in choice:
		how_much = int(choice)
	else:
		dead("Would you like to take a number typing class?.")

	if how_much < 50:
		print "You're not greedy, you win!"
		exit(0)
	else:
		dead("You greedy bastard!")

def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False

	while True:
		choice = raw_input("> ")

		if "take" or "honey" in choice:
			dead("The bear looks at you, then slaps your face off.")
		elif "taunt" in choice and not bear_moved:
			print ("The bear has moved from the door, you can go through it now.")
			bear_moved = True
		elif "taunt" in choice and bear_moved:
			print ("The bear gets pissed off and chews your legs off.")
		elif "open door" in choice and bear_moved:
			gold_room()
		else:
			print ("I have no idea what that means.")

def cthulhu_room():    
	print "Here you see the great evil Cthulhu."
	print "He, She, Xe, whatever it is stares you down and you start going insane."
	print "Do you flee for your life or eat your head?"

	choice = raw_input("> ")

	if "flee" in choice:
		start()
	elif "eat head" or "head" in choice:
		dead("Mmmm...self-cannibalism!")
	else:
		cthulhu_room()

def dead(why):
	print why, "Good Job!"
	exit(0)

def start():
	print "You are in a dark room."
	print "There is a door to your left and right"
	print "Which do you take?"

	choice = raw_input("> ")

	if choice == "left":
		bear_room()
	elif choice == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")



start()