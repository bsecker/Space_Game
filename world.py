"""main module for controlling game state etc"""
import gen

class World:
	def __init__(self):
		self.game_state = "state_galaxy"

		self.galaxy = gen.Galaxy(stars = 1000)

		self.level_objs = []

	def update(self):
		state = getattr(self, self.game_state)
		state()

	def draw(self, surface):
		for _i in self.level_objs:
			_i.draw(surface)

	def state_galaxy(self):
		self.level_objs = self.galaxy.level_objs

	def state_sytem(self):
		print "im a solar system!"

	def state_planet(self):
		pass

	def state_terrain(self):
		pass