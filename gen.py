"""main generator module"""
import random
import entities
import constants
import math
import pygame

## TO DO: fix texts and stuff. make sure each level can have text

class Galaxy:
    def __init__(self, seed = None):
        """generator for the galaxy. Currently makes a sphere shape."""
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
            speed = random.random()/15 #slow as bro
            name = "test planet"
            colour = [random.randint(0, 255) for _i in range(3)]
            planet_type = random.randint(0,10)
            planet_list.append(Planet(distance, angle, speed, name, planet_type, colour))

        return planet_list

class Planet:
    def __init__(self, distance, angle, speed, name = None, planet_type = 1, colour = None):
        """planet level"""
        self.name = name
        self.planet_type = planet_type
        self.colour = colour

        #in system entity
        self.planet = entities.Planet(distance, angle, speed, colour)

        self.level_objs = [Planet_Large(self.name, self.planet_type, self.colour)]

    def update(self):
        self.planet.update()

    def draw(self, surface):
        self.planet.draw(surface)

class Planet_Large:
    def __init__(self, name, planet_type, colour):
        self.name = name
        self.planet_type = planet_type
        self.colour = colour

        #physical entity:
        self.level_objs = [entities.Planet_Large(self.colour)]
        self.planet = self.level_objs[0]

        self.texts = []
        self.texts.append([(constants.SCREEN_WIDTH/4)*3, constants.SCREEN_HEIGHT/4, "Planet Name: {0}".format(self.name)])
        self.texts.append([(constants.SCREEN_WIDTH/4)*3, constants.SCREEN_HEIGHT/4 + 50, "Planet Type: {0}".format(self.planet_type)])

    def update(self):
        self.planet.update()

    def draw(self, surface):
        self.planet.draw(surface)
        # self.name_text.draw(surface)
        # self.type_text.draw(surface)


class Planet_Ground:
    def __init__(self):
        """Planet ground level."""
        pass

    def generate(self):
        pass

    def update(self):
        pass

    def draw(self, surface):
        pass


# class Text:
#     """text control. Currently does nothing special."""
#     def __init__(self, x, y, message,):
#         self.font = font
#         self.x = x
#         self.y = y
#         self.message = str(message)

#     def draw(self, surface):
#         text = self.font.render(self.message, 1, constants.SPACE_TEXT_COLOUR)
#         rect = text.get_rect()
#         rect = (self.x, self.y)
#         surface.blit(text, rect)

# test function to see if this functionality works
if __name__ == '__main__':
    gal = Galaxy()
    print gal.generate(100, 320, 240, 30)