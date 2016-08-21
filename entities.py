import pygame
import constants

class Base_Entity(pygame.sprite.Sprite):
    """Entity Superclass."""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


class Star(Base_Entity):
	""" star system """
	def __init__(self, x, y, size = 1):
		Base_Entity.__init__(self)
		self.entity_id = "star"
		self.rect = pygame.Rect(x, y, size, size)

	def draw(self, surface):
		pygame.draw.circle(surface, constants.WHITE, (self.rect.x, self.rect.y), 2)
