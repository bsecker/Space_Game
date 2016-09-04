import pygame
import constants
import math

"""classes for actual physical entites that the player can see on the surface

TO DO:
replace sprites with dirty sprites!

"""

class BaseEntity:
    def __init__(self, x, y, width, height, colour):
        """for blocky style entities"""
        self.image = pygame.Surface(( width, height))
        self.image.fill(colour)

        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

class Entity(BaseEntity):
    def __init__(self, x, y, width, height, colour):
        BaseEntity.__init__(self, x, y, width, height, colour)
        self.max_gravity = 20
        self.jump_speed = 8
        self.gravity_accel = .30
        self.move_speed = 10
        self.alive = True

        self.x_vel = 0
        self.y_vel = 0
        self.direction = 'L'

        self.block_list = None

    def update(self):
        self.calc_gravity()

        # Move left/right
        self.rect.x += self.x_vel

        #collide with objects
        block_hit_list = pygame.sprite.spritecollide(self, self.block_list, False)
        for block in block_hit_list:
            if block.solid:
                if self.x_vel > 0:
                    self.rect.right = block.rect.left
                elif self.x_vel < 0:
                    self.rect.left = block.rect.right

        #move up/down
        self.rect.y += self.y_vel
        # collide with objects
        block_hit_list = pygame.sprite.spritecollide(self, self.block_list, False)
        for block in block_hit_list:
            if block.solid:# Reset our position based on the top/bottom of the object.
                if self.y_vel > 0:
                    self.rect.bottom = block.rect.top
                elif self.y_vel < 0:
                    self.rect.top = block.rect.bottom

                # Stop our vertical movement
                self.y_vel = 0


    def calc_gravity(self):
        """ Calculate effect of gravity. """
        if self.y_vel <= self.max_gravity:
            self.y_vel += self.gravity_accel
 

    def jump(self):
        """ Called when user hits 'jump' button. """
 
        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down
        # 1 when working with a platform moving down.
        self.rect.y += 2
        # only if the block is solid
        block_hit_list = [i for i in pygame.sprite.spritecollide(self, self.block_list, False) if i.solid == True]
        self.rect.y -= 2
 
        # If it is ok to jump, set our speed upwards
        if len(block_hit_list) > 0:
            self.y_vel = -self.jump_speed

    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.x_vel = -self.move_speed
        self.direction = 'L'
 
    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.x_vel = self.move_speed
        self.direction = 'R'
 
    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.x_vel = 0

    def draw(self, surface, camera):
        surface.blit(self.image, camera.apply(self))


class Player(Entity):
    def __init__(self, x, y):
        """main class for player on surface"""
        Entity.__init__(self, x, y, constants.BLOCK_SIZE*2, constants.BLOCK_SIZE*4, constants.RED)
        self.jetpack_capacity = 100
        self.jetpack_fuel = 0

    def jump(self):
        Entity.jump(self)

        self.rect.y += 2
        # only if the block is solid
        block_hit_list = [i for i in pygame.sprite.spritecollide(self, self.block_list, False) if i.solid == True]
        self.rect.y -= 2

        if len(block_hit_list) == 0:
            self.y_vel =- 5