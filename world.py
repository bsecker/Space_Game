"""main module for controlling game state etc."""
import gen
import constants

class World:
	"""Things to remember

	game_state = pygame 'level'. ie main menu can be a state.
	level_objs = objects within the level (specified by game_state).

	"""
	def __init__(self):
		self.game_state = "state_surface"
		self.system = gen.System(20)
		self.planet = self.system.planets[0]

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

	def set_state(self, state):
		"""change state to specified state"""
		pass

	def state_surface(self):
		self.level_objs = self.planet.surface.level_objs

	def state_system(self):
		pass