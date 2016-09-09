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

        self.chunks = {}

    def update(self):
        pass

    def get_current_chunk(self, player):
        pass
        
    def add_chunk(self, objs):
        """take level_objs and add to dictionary"""
        for _i in objs:
            pass


    def __set_chunk(self, chunk):
        """take level_objs and pickle"""
        objs = {}
        for _i in chunk:
            objs['rect'] = _i.rect

    def __get_chunk(self, chunk):
        pass


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
    def __init__(self, seed = None):
        """Planet ground level."""
        random.seed(seed)
        self.level_objs, self.spawnpoint = self.generate()
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
        rightx = constants.CHUNK_SIZE
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

            if midpointy > constants.MAX_LEVEL_HEIGHT:
                midpointy = constants.MAX_LEVEL_HEIGHT-constants.BLOCK_SIZE

            displacement = displacement/2 #half displacement
 
            if recurs < constants.RECURS_DEPTH:
                _add(leftx, lefty, midpointx, midpointy, recurs, displacement)
                _add(midpointx, midpointy, rightx, righty, recurs, displacement)

            else:
                points.append((leftx, lefty))
                points.append((rightx, righty))

        recurs = 0
        _add(leftx, lefty, rightx, righty, recurs, 600)

        # add less rugged biome
        # leftx = constants.CHUNK_SIZE
        # rightx = leftx+constants.CHUNK_SIZE
        # _add(leftx, lefty, rightx, righty, recurs, 750)

        # # add completely flat biome (testing)
        # leftx += constants.CHUNK_SIZE
        # rightx = leftx+constants.CHUNK_SIZE
        # _add(leftx, lefty, rightx, righty, recurs, 250)

        # strip every second point and end points to prevent doubleups
        del points[1:-1:2]
        
        ##### add grass
        for _i in points:
            _y = roundTo(_i[1], constants.BLOCK_SIZE)
            block = blocks.Grass(_i[0], _y)
            block_list.append(block)

            # add dirt downwards from grass block
            block_down = blocks.Dirt_Long(_i[0], _y+constants.BLOCK_SIZE, constants.MAX_LEVEL_HEIGHT - _y)
            block_list.append(block_down)

            # add single blocks downwards
            # while _y < constants.MAX_LEVEL_HEIGHT:
            #     _y += constants.BLOCK_SIZE
            #     block_down = blocks.Dirt(_i[0], _y)
            #     block_list.append(block_down)


        # set spawnpoint to exact middle (TO DO: fix y pos)
        spawnpoint = (
            points[-1][0]/2,
            0
            )

        return block_list, spawnpoint


# test function to see if this functionality works
if __name__ == '__main__':
    level = SurfaceForest()
    objs = [[_i.rect] for _i in level.level_objs]

    #pickle.dump( objs, open("save.p", "wb"))

    #new_objs = pickle.load(open("save.p","rb"))
    #print new_objs