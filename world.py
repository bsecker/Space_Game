"""main module for controlling game state etc"""
import gen

class World:
	def __init__(self):
		self.game_state = "state_galaxy"

	def update(self):
		state = getattr(self, self.game_state)
		state()

	def draw(self):
		pass

	def state_galaxy(self):
		print "im a star weee"

	def state_sytem(self):
		print "im a solar system!"

	def state_planet(self):
		pass

	def state_terrain(self):
		pass