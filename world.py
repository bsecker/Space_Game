"""main module for controlling game state etc"""
import gen.gen as gen

class World:
	def __init__(self):
		self.game_state = "state_galaxy"

		self.galaxy = gen.Galaxy()

	def update(self):
		state = getattr(self, self.game_state)
		state()

	def draw(self):
		pass

	def state_galaxy(self):
		pass

	def state_sytem(self):
		print "im a solar system!"

	def state_planet(self):
		pass

	def state_terrain(self):
		pass