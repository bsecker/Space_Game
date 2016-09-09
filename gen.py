"""main generator module"""
import random
import entities_surface
import constants
import math
import pygame
import blocks
import cPickle as pickle 


class LevelManager:
    """main class for handling loading and saving levels dynamically"""
    def __init__(self, level = None):
        self.level = level
        self.path = "/levels/{0}/".format(level)

        self.chunks = []
        self.chunk_num = constants.CHUNKS

        leftx = 0
        rightx = constants.CHUNK_SIZE
        lefty = constants.MAX_LEVEL_HEIGHT/2
        righty = constants.MAX_LEVEL_HEIGHT/2

        self.level = self.generate_chunk(leftx, lefty, rightx, righty, 200)

    def update(self,):
        pass

    def generate_chunk(self, leftx, rightx, lefty, righty, displacement):
        """generate terrain based on recursive algorithm."""
        points = []
        block_list = []

        def roundTo(x, base=5):
            return int(base * round(float(x)/base))

        ##### make points    
        def _generate_chunk_points(leftx, lefty, rightx, righty, recurs, displacement):
            recurs += 1

            midpointx = (leftx+rightx)/2
            midpointy = (lefty +righty)/2 + random.randint(-displacement, displacement)

            if midpointy > constants.MAX_LEVEL_HEIGHT:
                midpointy = constants.MAX_LEVEL_HEIGHT-constants.BLOCK_SIZE

            displacement = displacement/2 #half displacement
 
            if recurs < constants.RECURS_DEPTH:
                _generate_chunk_points(leftx, lefty, midpointx, midpointy, recurs, displacement)
                _generate_chunk_points(midpointx, midpointy, rightx, righty, recurs, displacement)

            else:
                points.append((leftx, lefty))
                points.append((rightx, righty))

        recurs = 0
        _generate_chunk_points(leftx, lefty, rightx, righty, recurs, displacement)

        # strip every second point and end points to prevent doubleups
        del points[1:-1:2]
        
        ##### add grass
        for _i in points:
            _y = roundTo(_i[1], constants.BLOCK_SIZE)
            block = blocks.Grass(_i[0], _y)
            block_list.append(block)

            # add dirt downwards from grass block
            print constants.MAX_LEVEL_HEIGHT - _y
            block_down = blocks.Dirt_Long(_i[0], _y+constants.BLOCK_SIZE, 10)#constants.MAX_LEVEL_HEIGHT - _y)
            block_list.append(block_down)

        return block_list


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
    def __init__(self, levelmanager):
        """Planet ground level."""
        self.levelmanager = levelmanager
        self.level_objs = self.levelmanager.level
        self.spawnpoint = (0,0)
        self.level_entities = []                    
        # add player
        self.player = self.generate_player( self.spawnpoint)
        self.level_entities.append(self.player)

    def generate(self):
        pass

    def generate_player(self, spawnpoint):
        player = entities_surface.Player(spawnpoint[0],spawnpoint[1])
        player.block_list = self.level_objs

        return player

    def update(self):
        pass

    def draw(self, surface):
        pass

class SurfaceIce(Surface):
    def __init__(self, levelmanager):
        Surface.__init__(self, levelmanager)

    def generate(self):
        pass

class SurfaceForest(Surface):
    def __init__(self, levelmanager):
        Surface.__init__(self, levelmanager)
        self.bg_colour = constants.LIGHTBLUE


# test function to see if this functionality works
if __name__ == '__main__':
    level = SurfaceForest()
    objs = [[_i.rect] for _i in level.level_objs]

    #pickle.dump( objs, open("save.p", "wb"))

    #new_objs = pickle.load(open("save.p","rb"))
    #print new_objs