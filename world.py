"""main module for controlling game state etc"""
import gen
import constants

class World:
	def __init__(self):
		self.game_state = "state_system"

		self.galaxy = gen.Galaxy()
		self.current_system = self.galaxy.level_objs[1]

		self.level_objs = []

	def update(self):
		state = getattr(self, self.game_state)
		state()

		# update everything - might need to change this!
		for _i in self.level_objs:
			_i.update()

	def draw(self, surface):
		surface.fill(constants.BG_COLOUR)
		for _i in self.level_objs:
			_i.draw(surface)

	def state_galaxy(self):
		self.level_objs = self.galaxy.level_objs

	def state_system(self):
		self.level_objs = self.current_system.level_objs

	def state_planet(self):
		pass

	def state_terrain(self):
		pass