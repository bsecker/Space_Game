import constants
import pygame
import random

class Block:
    def __init__(self, colour, x, y):
        self.image = pygame.Surface((constants.BLOCK_SIZE, constants.BLOCK_SIZE))
        self.image.fill(colour)

        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.solid = True #if the player can walk through them or not

    def update(self):
        pass

    def draw(self, surface, camera):
        surface.blit(self.image, camera.apply(self))

class Grass(Block):
    def __init__(self, x, y):
        Block.__init__(self, constants.GREEN, x, y)
        self.block_id = 'grass'

class Rock(Block):
    def __init__(self, x, y):
        Block.__init__(self, constants.ORANGE, x, y)
        self.block_id = 'rock'

class Dirt(Block):
    def __init__(self, x, y):
        Block.__init__(self, constants.BROWN, x, y)
        self.block_id = 'dirt'

class Dirt_Long(Block):
    def __init__(self, x, y, height):
        """makes a dirt block of a arbitrary length."""
        self.block_id = 'dirt_long'
        self.image = pygame.Surface((10, height))
        self.image.fill(constants.BROWN)

        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.solid = True

class Trunk(Block):
    def __init__(self, x, y):
        Block.__init__(self, constants.BROWN, x, y)
        self.block_id = 'trunk'
        self.solid = False

class Leaves(Block):
    def __init__(self, x, y):
        Block.__init__(self, constants.DARKGREEN, x, y)
        self.block_id = 'leaves'
        self.solid = False