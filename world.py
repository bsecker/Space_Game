"""main module for controlling game state etc."""
import gen
import constants

class World:
	"""Things to remember

	game_state = pygame 'level'. ie main menu can be a state.
	level_objs = objects within the level (specified by game_state).

	"""
	def __init__(self):
		self.game_state = "state_galaxy"

		self.galaxy = gen.Galaxy()
		self.system = None
		self.planet = None
		self.planet_large = None
		self.terrain = None
		self.menu = None

		self.level_objs = []

	def update(self):
		state = getattr(self, self.game_state)
		state()

		# update everything in level_objs
		for _i in self.level_objs:
			_i.update()

	def draw(self, surface):
		surface.fill(constants.BG_COLOUR)

		for _i in self.level_objs:
			_i.draw(surface)

	def state_galaxy(self):
		self.level_objs = self.galaxy.level_objs

	def state_system(self):
		self.level_objs = self.system.level_objs

	def state_planet(self):
		self.level_objs = self.planet.level_objs

	def state_terrain(self):
		pass

	def state_menu(self):
		self.level_objs = self.menu.level_objs

	def set_state(self, state):
		"""change state to specified state"""
