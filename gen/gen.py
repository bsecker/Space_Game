"""main generator for shite"""

class Galaxy:
	def __init__(self, seed = None):
		self.seed = seed

		#generate galaxy
		self.level_objs = self.generate()

	def generate(self, seed):
		random.seed(seed)

		



