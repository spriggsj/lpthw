from sys import exit
from random import randint

class Scene(object):
	def enter(self):
		print "This scene is not yet configured. Subclass it and implement enter()."
			#exit(1)
		
class Engine(object):
	def __init__(self, scene_map):
		self.scene_map = scene_map
		
	def play(self):
		current_scene = self.scene_map.opening_scene()
		
		while True:
			print "\n---------------------"
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)

class Death(Scene):
	
	quips = [
		"You died, you kinda suck at this",
		"You really suck at this",
		"Oh man your not good at all",
		"Holy crackers you are bad"
	]
	
	def enter(self):
		print Death.quips[randint(0, len(self.quips)-1)]
		exit(1)	
		
class CentralCorridor(Scene):
	def enter(self):
		print " The Gorthons have invaded your ship"
		print " You are the last surviving member"
		print " Get the neutron bomb from the armory"
		print " Put it into the bridge and blow up the ship"
		print " After getting into an escape pod"
		print "\n"
		print "You are running down the central corridor when a Gorthon jumps"
		print "Out at you. He is blocking the door to the armory"
		print " He is about to blast you. What do you do?"
		
		action = raw_input("> ")
		
		if action == "shoot":
			print " Quick to draw, but he was quicker"
			print " Your dead"
			return 'death'
		
		elif action == "run":
			print "Nice try but he is much faster then you with his 8 legs"
			print " He pulls off your leg and beats you with it until you die"
			return 'death'
			
		elif action == "tickle":
			print "How could you have known the Gorthons were extremely tickleish"
			print " He laughs so hard he pees and falls to the floor."
			print " You jump past him and go through the laser armory door"
			return 'laser_weapon_armory'
			
		else:
			print "Does not compute"
			return 'central_corridor'
		
class LaserWeaponArmory(Scene):
	def enter(self):
		print " You dive into the armory"
		print " You see the neutron bomb but it has a keypad that requires"
		print " A 3 digit code. You only have 10 guesses or it locks forever"
		code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
		guess = raw_input("[keypad]> ")
		guesses = 0
		
		while guess != code and guesses < 10:
			print "BZZZT"
			guesses += 1
			guess = raw_input("[keypad]> ")
			guesses = 0
			
		if guess == code:
			print "The container clicks open"
			print "You grab the bomb and run to the bridge"
			return 'the_bridge'
			
		else:
			print " The lock buzzed for its last time"
			print " The Gothons find you and you are killed"
			return 'death'
			
			
		
class TheBridge(Scene):
	def enter(self):
		print " you burst into the bridge with the bomb under one arm"
		print " The Gothons don't shoot because the bomb is in your arms"
		print " What do you do?"
		
		action = raw_input("> ")
		
		if action == "throw the bomb":
			print " The bomb goes off and you die"
			return 'death'
		
		elif action == "set down bomb":
			print " You point your gun at the bomb and slowly move to the pod"
			return 'escape_pod'
			
		else:
			print " does not compute"
			return 'the_bridge'	
		
class EscapePod(Scene):
	def enter(self):
		print " You try to find the escape pod before the ship explodes"
		print " you see 5 pods but which one do you pick?"
		
		good_pod = randint(1,5)
		guess = raw_input("[pod #]> ")
		
		if int(guess) != good_pod:
			print " You jump into %s pod" % guess
			print " The pod explodes"
			return 'death'
			
		else:
			print " You jump into %s pod" % guess
			print " You escape and have clearly won"
			return 'finished'
		
class Map(object):
	scenes = {
		'central_corridor' : CentralCorridor(),
		'laser_weapon_armory' : LaserWeaponArmory(),
		'the_bridge' : TheBridge(),
		'escape_pod' : EscapePod(),
		'death' : Death()
	}
	def __init__(self, start_scene):
		self.start_scene = start_scene
		
	def next_scene(self, scene_name):
		return Map.scenes.get(scene_name)
		
	def opening_scene(self):
		return self.next_scene(self.start_scene)
		
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()