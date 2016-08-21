import pygame
import constants

class Base_Entity(pygame.sprite.Sprite):
    """Entity Superclass."""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

class Star(Base_Entity):
	""" star system """
	def __init__(self, x, y, temperature, planets_num, name = None):
		Base_Entity.__init__(self)
		self.entity_id = "star"
		self.temperature = temperature
		self.name = name
		self.planets_num = planets_num 

		# physical 'galaxy level' attributes
		self.size = 1
		self.rect = pygame.Rect(x, y, self.size, self.size)

	
	def draw(self, surface):
		pygame.draw.circle(surface, constants.WHITE, (self.rect.x, self.rect.y), 2)
