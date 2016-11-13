#exercise 31
print "You enter a dark room with two doors. Do you go through door #1 or #2"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheesecake, What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."

	bear = raw_input("> ")

	if bear == "1":
		print "I would make a cake joke, but you're already mauled by the bear, also THE CAKE" 
		print "IS A LIE!!!!!!"
	elif bear == "2":
		print "The bear eats your legs off. Good Job!"
	else:
		print "The bear is so frighten by %s, it runs aways screaming!" % bear

elif door == "2":
	print "You stare into the endless abyss that is Cthulhu's retinas."
	print "1. Proceed to beat the crap out of Cthulhu."
	print "2. Flip off Cthulhu"
	print "3. Romance Cthulhu"

	cthulhu = raw_input("> ")

	if cthulhu == "1": 
		print "ARE YOU CRAZY?!?!?! Why in the world would you beat up Cthulhu?"

	elif cthulhu == "2": 
		print "Cthulhu invites you to a rigged game of....Russian Roulette!"
		print "Do you play with Cthulhu? Y/N"
		rigged_game = raw_input("> ")
		if rigged_game == "Y":
			print "Cthulhu aims the revolver at you and begins cycling..."
			print "1...Click"
			print "2...Click"
			print "3...Click"
			print "4...Click"
			print "5...Click"
			print "Cthulhu notes that you have one cylinder left,"
			print "does the last cylinder contain the bullet? Y/N"
			last = raw_input("> ")
			if last == "Y":
				print "Cthulhu pulls the trigger, but then realises the you are holding a mirror up,"
				print "the bullet ricochets of the mirror and hits Cthulhu, who dissolves into darkness..."
				print "Leaving behind milk and cookies..."

			if last == "N":
				print "Cthulhu pulls the trigger, the bullet strikes and hits you, dissolving your body"
				print "and killing you."
				
				print "Cthulhu: GG"

			elif last == " ":
				print "Cthulhu is NOT impressed by your hestitation."

		if rigged_game == "N":
			print "Cthulhu proceeds to mock you relentlessy..."

	elif cthulhu == "3": 
		print "Cthulhu thinks we've had enough of this trope already and" 
		print "slowly backs away closing the door...."
		print "STOP ROMANCING Cthulhu!!!"
	else:
		print "Cthulhu is NOT impressed by your hestitation."

else:
	print "You stumble around and fall in an abyss..."