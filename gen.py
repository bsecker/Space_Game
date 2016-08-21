"""main generator for shite"""
import random
import entities
import constants

class Galaxy:
	"""MOVE THIS TO OWN MODULE"""
	def __init__(self, seed = None, stars = 100):
		self.seed = seed
		self.stars = stars

		self.mux = constants.HALF_SCREEN_WIDTH #mean
		self.muy = constants.HALF_SCREEN_HEIGHT
		self.sigma = 120 #how clustered it is in the middle

		#generate galaxy
		self.level_objs = self.generate(self.seed, self.stars, self.mux, self.muy, self.sigma)

	def generate(self, seed, stars, mux, muy, sigma):
		"""generate level with gaussian distribution of planets. (clusters in middle)
			seed = random seed to use
			stars = number of stars to make
			mux = mean x, muy = mean y
			sigma = standard deviation

		"""
		random.seed(seed)
		star_list = []

		for _i in range(stars):
			x = random.gauss(mux, sigma)
			y = random.gauss(muy, sigma)
			star_list.append(entities.Star(x, y))

		return star_list



		
if __name__ == '__main__':
	gal = Galaxy()
	print gal.generate(100, 100, 320, 240, 30)