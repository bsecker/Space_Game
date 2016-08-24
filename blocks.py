import constants
import pygame
import random

class Block:
    def __init__(self, colour):
        self.image = pygame.Surface((constants.BLOCK_SIZE, constants.BLOCK_SIZE))
        self.image.fill(colour)

        self.rect = self.image.get_rect()
        self.solid = True #if the player can walk through them or not

    def update(self):
        pass

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Grass(Block):
    def __init__(self):
        Block.__init__(self, constants.GREEN)
        self.block_id = 'grass'

class Rock(Block):
    def __init__(self):
        Block.__init__(self, constants.ORANGE)
        self.block_id = 'rock'
