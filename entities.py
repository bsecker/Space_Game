import pygame
import constants
import math

"""classes for actual physical entites that the player can see

TO DO:
replace sprites with dirty sprites!

"""



class Base_Entity(pygame.sprite.Sprite):
    """Entity Superclass."""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

### GALAXY LEVEL ###

class Star(Base_Entity):
    """ star system """
    def __init__(self, x, y):
        Base_Entity.__init__(self)
        self.entity_id = "star"

        # physical 'galaxy level' attributes
        self.size = 2
        self.rect = pygame.Rect(x, y, self.size, self.size)
        self.color = constants.WHITE

    def update(self):
        pass

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.rect.centerx, self.rect.centery), self.size)


### SYSTEM LEVEL ###

class Planet(Base_Entity):
    def __init__(self, distance, angle, speed, colour):
        Base_Entity.__init__(self)
        self.entity_id = "planet"
        self.x = 0
        self.y = 0
        self.size = 2

        self.distance = distance
        self.angle = angle
        self.speed = speed
        self.colour = colour

        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def update(self):
        self.dirty = 1

        # calculate using trig the position of the planet
        angle = math.radians(self.angle)
        self.rect.centerx = constants.HALF_SCREEN_WIDTH + math.cos(angle)*self.distance
        self.rect.centery = constants.HALF_SCREEN_HEIGHT + math.sin(angle)*self.distance

        #rotate
        if self.angle < 360:
            self.angle += self.speed
        else:
            self.angle = 0

    def draw(self, surface):
        pygame.draw.circle(surface, self.colour, (self.rect.centerx, self.rect.centery), self.size)

class Sun(Base_Entity):
    def __init__(self):
        self.entity_id = "sun"
        self.size = 5
        self.x = constants.HALF_SCREEN_WIDTH-(self.size/2)
        self.y = constants.HALF_SCREEN_HEIGHT-(self.size/2)
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def update(self):
        pass

    def draw(self, surface):
        pygame.draw.circle(surface, constants.YELLOW, (self.rect.centerx, self.rect.centery), self.size)

### PLANET LEVEL ###
class Planet_Large(Base_Entity):
    def __init__(self, colour):
        Base_Entity.__init__(self)
        self.entity_id = "planet_large"
        self.size = 230
        self.colour = colour
        print self.colour

    def update(self):
        pass

    def draw(self, surface):
        pygame.draw.circle(surface, self.colour, (constants.HALF_SCREEN_WIDTH/2,constants.HALF_SCREEN_HEIGHT), self.size)
