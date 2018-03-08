#!/usr/bin/env python

import random
import pygame
import base64
def play_music(music_file):
	"""
	stream music with mixer.music module in blocking manner
	this will stream the sound from disk while playing
	"""
	clock = pygame.time.Clock()
	try:
		pygame.mixer.music.load(music_file)
		print "loaded"
	except pygame.error:
		print "File %s not found! (%s)" % (music_file, pygame.get_error())
		return
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy():
		# check if playback has finished
		clock.tick(30)



print("Welcome to blood adventure!!!")

name = raw_input("What is your name? ")

seed = raw_input( "enter a seed, unless you want a random game: " )
if len(seed) > 0:
	seed = int(seed)
	random.seed( seed )

prompt = "Are you brave enough to make this journey, " + name + "? "
brave = raw_input( prompt )

if brave == "no":
	print( "That was a wise choice." )
	quit()

print( "Well, I sure hope you are right." )

print( """


You are sitting on your sofa. You hear a bang, turn around
and there is blood dripping from the mirror.

BBB     L        OOOO    OOOO   DD
B  B    L        O  O    O  O   D D
B  B    L        O  O    O  O   D  D
BBB     L        O  O    O  O   D  D
B  B    L        O  O    O  O   D  D
B  B    L        O  O    O  O   O O
BBB     LLLLLL   OOOO    OOOO   DD
.             .     .
.             .
.
.             .


What do you do?
1 - Go take a closer look
2 - Run out of the house
3 - Hide under the blanket

""" )

choice = int( raw_input("Your choice? ") )

if choice == 1:
	# play_music("./jaws.mid")
	print( """

A monster jumps out of the mirror! You get a quick glimpse
of the monster and you see a piston that made you realize that's
why you heard the bang (the piston made the bang when it hit
the wall).

You teleport to a house in the middle of the wasteland.

What do you do?
1-You run.
2-You go into the house.
3-You hesitate.

""" )
	choice = int( raw_input("Your choice? ") )

	if choice == 1:
		print("You run into the forest. A monster kills you. You die.")
		quit()
	elif choice == 2:
		print("You go into the house. There are no monsters so far. There is a die that says die on three faces and live on three faces. You roll it.")
		foo = [ 'die', 'live' ]
		choice = random.choice(foo)
		if choice == "die":
			print("You rolled die! You are dead. Thanks for playing.")
			quit()
		else:
			print("""
You live! You keep moving forward.

You find a lava pit; and then see a monster. What do you do?

1-you push it into the lava pit.
2-you hesitate.
3-you start punching it.

			""")

			choice = int( raw_input("Your choice? ") )
			if choice == 1:
				print("You miss. You fall into the lava pit. You die.")
				quit()
			elif choice ==2:
				print("It is freindly. It gives you a key. You feel it could be important. You keep it. You move forward.")
			else:
				print("You miss and swing your self into the lava pit. You die.")
				quit()





	else:
		print("It's too late. A monster kills you. You die.")
		quit()

elif choice == 2 or choice == 3:
	print( """You die.""" )
	quit()

	print('You see a door. You walk in. It is a room of riddles! The first one is "what has more lives than a cat?"')
	riddle_1 = raw_input("Your answer?")
	if choice == "a frog" or choice == "frog":
		print("correct!")
	else:
		print("that was not the correct answer. A lazer hits you. You die.")
		quit()
		print "You get a key."
		print 'The next riddle is "what is black and white, and red all over?".'
		riddle_2 = raw_input("Your answer?")
		if choice == "a blushing zebra" or "blushing zebra":
			print "Correct!"
		else:
			print "That was the incorrect answer. Five knives stab you. You die."
			quit()
			print '''You get a key. The next riddle is "There was a ship with 20 people. It sinks. Twenty-four heads pop up. How?"'''
			riddle_3 = raw_input("Your answer?")
if choice == "twenty for heads" or "for heads":
	print "Correct!"
else:
	print "Incorrect."
	quit()
	print "You get a key. A door opens. You are out of the room of riddles!"
	print "You get a door. None of the keys fit!"
	print "What do you do?"
	print """
	1-you wait here until it opens
	2-you pound on it
	3-you try all the keys again
	"""
	if choice == 1:
		print "After a few hours, it opens."
	else:
		print "You die."
		quit()
		print "You walk in."
