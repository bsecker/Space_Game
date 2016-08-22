"""main generator module"""
import random
import entities
import constants
import math

class Galaxy:
    def __init__(self, seed = None):
        """generator for the galaxy. Curerntly makes a sphere shape."""
        self.seed = seed

        self.mux = constants.HALF_SCREEN_WIDTH #mean
        self.muy = constants.HALF_SCREEN_HEIGHT
        self.sigma = 120 #how clustered it is in the middle

        #generate galaxy
        self.level_objs = self.generate(self.seed, self.mux, self.muy, self.sigma)

    def generate(self, seed, mux, muy, sigma):
        """generate level with gaussian distribution of planets. (clusters in middle)
            seed = random seed to use
            mux = mean x, muy = mean y
            sigma = standard deviation

        """
        random.seed(seed)
        star_list = []
        stars = random.randint( 250, 1500)

        for _i in range(stars):
            x = random.gauss(mux, sigma)
            y = random.gauss(muy, sigma)
            temperature = 1000
            planet_count = random.randint(1, 10) #always one planet
            name = None
            star_list.append(System(x, y, temperature, planet_count, name))
        return star_list

class System:
    def __init__(self, x, y, temperature, planet_count, name = None):
        self.planet_count = planet_count
        self.temperature = temperature
        self.name = name

        #actual star on galaxy level
        self.star = entities.Star(x, y)

        self.level_objs = self.generate(self.planet_count)

        # print "Planet Count: {0} \n Star: {1}".format(self.planet_count, self.star)

    def update(self):
        self.star.update()

    def draw(self, surface):
        self.star.draw(surface)

    def generate(self, planet_count):
        """generate planets"""
        planet_list = []

        # add sun
        planet_list.append(entities.Sun())

        # add planets
        for _i in range(planet_count):
            distance = random.randrange(10, 350)
            angle = random.randrange(0, 360)
            speed = random.random()/4 #slow as bro
            planet_list.append(entities.Planet(distance, angle, speed))

        return planet_list


# test this functionality works
if __name__ == '__main__':
    gal = Galaxy()
    print gal.generate(100, 320, 240, 30)