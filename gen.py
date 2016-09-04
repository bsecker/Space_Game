"""main generator module"""
import random
import entities_surface
import constants
import math
import pygame
import blocks

class System:
    def __init__(self, planet_count, ):
        self.planets = [Planet(1, 'rock'), Planet(2, 'ice')]
        self.planet = None


        
class Planet:
    def __init__(self, planet_id, planet_type):
        self.planet_id = planet_id
        self.planet_type = planet_type

        self.surface = SurfaceForest()

class Surface:
    def __init__(self, ):
        """Planet ground level."""
        # random.seed(seed)
        self.level_objs = self.generate()
        self.level_entities = []                    
        # add player
        self.player = self.generate_player( 50, 100)
        self.level_entities.append(self.player)

    def generate(self):
        pass

    def generate_player(self, x, y):
        player = entities_surface.Player(x,y)
        player.block_list = self.level_objs

        return player

    def update(self):
        pass

    def draw(self, surface):
        pass

class SurfaceIce(Surface):
    def __init__(self):
        Surface.__init__(self)

    def generate(self):
        pass

class SurfaceRock(Surface):
    def __init__(self):
        Surface.__init__(self)

    def generate(self):
        pass

class SurfaceForest(Surface):
    def __init__(self):
        Surface.__init__(self)
        self.bg_colour = constants.LIGHTBLUE

    def generate_walk(self):
        """generate forest based world"""
        block_list = []
        block_num = constants.SCREEN_WIDTH/constants.BLOCK_SIZE
        y = (constants.SCREEN_HEIGHT-constants.BLOCK_SIZE*25)
        
        for _i in range(block_num):
            x = _i * constants.BLOCK_SIZE

            # change y 
            y += random.choice([constants.BLOCK_SIZE, -constants.BLOCK_SIZE, 0])

            # add grass
            block = blocks.Grass(x, y)
            block_list.append(block)

            # add blocks below
            _y = y
            while _y <= constants.SCREEN_HEIGHT:
            	_y+=constants.BLOCK_SIZE
            	block = blocks.Dirt(x, _y)
            	block_list.append(block)
  
        return block_list

    def generate(self):
        """generate terrain based on recursive algorithm."""
        points = []
        block_list = []

        leftx = 0
        rightx = 5120
        lefty = constants.MAX_LEVEL_HEIGHT/2
        righty = constants.MAX_LEVEL_HEIGHT/2

        #1280/2^n = 40 => n = 5

        def roundTo(x, base=5):
            return int(base * round(float(x)/base))

        ##### make points    

        def _add(leftx, lefty, rightx, righty, recurs, displacement):
            recurs += 1

            midpointx = (leftx+rightx)/2
            midpointy = (lefty +righty)/2 + random.randint(-displacement, displacement)

            displacement = displacement/2 #half displacement
 
            if recurs < 10:
                _add(leftx, lefty, midpointx, midpointy, recurs, displacement)
                _add(midpointx, midpointy, rightx, righty, recurs, displacement)

            else:
                points.append((leftx, lefty))
                points.append((rightx, righty))

        recurs = 0
        _add(leftx, lefty, rightx, righty, recurs, 300)

        del points[1:-1:2]
        
        ##### add grass
        for _i in points:
            _y = roundTo(_i[1], constants.BLOCK_SIZE)
            block = blocks.Grass(_i[0], _y)
            block_list.append(block)

            # add dirt downwards from grass block
            block_down = blocks.Dirt_Long(_i[0], _y+constants.BLOCK_SIZE, 1)
            block_list.append(block_down)

            # while _y < constants.MAX_LEVEL_HEIGHT:
            #     _y += constants.BLOCK_SIZE
            #     block = blocks.Dirt(_i[0], _y)
            #     block_list.append(block)




        return block_list

## OLD CODE

# class Galaxy:
#     def __init__(self, seed = None):
#         """generator for the galaxy. Currently makes a sphere shape."""
#         self.seed = seed

#         self.mux = constants.HALF_SCREEN_WIDTH #mean
#         self.muy = constants.HALF_SCREEN_HEIGHT
#         self.sigma = 120 #how clustered it is in the middle

#         #generate galaxy
#         #self.stars = self.generate(self.seed, self.mux, self.muy, self.sigma)
#         #self.level_objs = self.make(self.stars)

#     def generate(self, seed, mux, muy, sigma):
#         """generate level with gaussian distribution of planets. (clusters in middle)
#             seed = random seed to use
#             mux = mean x, muy = mean y
#             sigma = standard deviation

#         """
#         random.seed(seed)
#         star_list = []
#         stars = random.randint( 250, 1500)

#         for _i_num, _i in enumerate(range(stars)):
#             system = {}
#             system['x'] = random.gauss(mux, sigma)
#             system['y'] = random.gauss(muy, sigma)
#             system['temperature'] = 1000
#             system['planet_count'] = random.randint(1, 10) #always one planet
#             system['name'] = None
#             system['id'] = _i_num
#             star_list.append(system)
#         print star_list
#         return star_list

#     def make(self, star_list):
#         """construct physical objects out of generated list"""
#         objs = []
#         for _i in star_list:
#             objs.append(entities.Star(_i['x'], _i['y']))
#         return objs

# class System:
#     def __init__(self, planet_count, name = None, seed = None):
#         self.planet_count = planet_count
#         self.name = name

#         self.level_objs = self.generate(self.planet_count, seed)

#     def generate(self, planet_count, seed):
#         """generate planets"""
#         planet_list = []

#         random.seed(seed)

#         # add sun
#         planet_list.append(entities.Sun())

#         # add planets
#         for _i in range(planet_count):
#             distance = random.randrange(10, 350)
#             angle = random.randrange(0, 360)
#             speed = random.random()/15 #slow as bro
#             name = "test planet"
#             colour = [random.randint(0, 255) for _i in range(3)]
#             planet_type = random.randint(0,10)
#             planet_list.append(Planet(distance, angle, speed, name, planet_type, colour))

#         return planet_list

# class Planet:
#     def __init__(self, distance, angle, speed, name = None, planet_type = None, colour = None):
#         """planet level"""
#         self.name = name
#         self.planet_type = planet_type
#         self.colour = colour

#         #in system entity
#         self.planet = entities.Planet(distance, angle, speed, colour)

#         self.level_objs = [Planet_Large(self.name, self.planet_type, self.colour)]

#     def update(self):
#         self.planet.update()

#     def draw(self, surface):
#         self.planet.draw(surface)

# class Planet_Large:
#     def __init__(self, name, planet_type, colour):
#         self.name = name
#         self.planet_type = planet_type
#         self.colour = colour

#         #physical entity:
#         self.level_objs = [entities.Planet_Large(self.colour)]
#         self.planet = self.level_objs[0]

#         self.texts = []
#         self.texts.append([(constants.SCREEN_WIDTH/4)*3, constants.SCREEN_HEIGHT/4, "Planet Name: {0}".format(self.name)])
#         self.texts.append([(constants.SCREEN_WIDTH/4)*3, constants.SCREEN_HEIGHT/4 + 50, "Planet Type: {0}".format(self.planet_type)])

#     def update(self):
#         self.planet.update()

#     def draw(self, surface):
#         self.planet.draw(surface)

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
    tree = Tree(50, 100)
    #print tree.blocks