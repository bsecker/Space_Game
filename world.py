"""main module for controlling game state etc."""
import gen
import constants
import pygame

class World:
    """Things to remember

    game_state = pygame 'level'. ie main menu can be a state.
    level_objs = objects within the level (specified by game_state).

    """
    def __init__(self):
        self.game_state = "state_surface"
        self.system = gen.System(5)
        self.planet = self.system.planets[0]

        self.current = None
        self.level_objs = []
        self.level_entities = []
        self.player = None

        self.camera = Camera(simple_camera, 1500, 720)

        # Initialise Pygame
        pygame.init()
        screen_size = (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        self.screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption(constants.WIN_CAPTION)

        self.clock = pygame.time.Clock()
        self.game_running = True

    def go(self):
        """main loop"""
        while self.game_running:

            # Update
            self.event_loop()
            self.update()

            # Draw
            self.draw(self.screen)
            self.clock.tick(constants.FPS)
            pygame.display.update()

        pygame.quit()

    def update(self):
        state = getattr(self, self.game_state)
        state()

        # update everything in level_objs
        for _i in self.level_objs:
            _i.update()

        for _i in self.level_entities:
            _i.update()

        #update camera
        self.camera.update(self.player)

    def event_loop(self):
        """main event loop"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                self.game_running = False
 
            if event.type == pygame.KEYDOWN:
                # Quit Game
                if event.key == pygame.K_ESCAPE:
                    self.game_running = False
                if event.key == pygame.K_LEFT:
                    self.player.go_left()
                if event.key == pygame.K_RIGHT:
                    self.player.go_right()
                if event.key == pygame.K_UP:
                    self.player.jump() 

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and self.player.x_vel < 0:
                    self.player.stop()
                if event.key == pygame.K_RIGHT and self.player.x_vel > 0:
                    self.player.stop()

    def draw(self, surface):
        surface.fill(self.current.bg_colour)

        drawable_blocks = [_i for _i in self.level_objs if _i.rect.x < self.player.rect.x + 800 and _i.rect.x > self.player.rect.x - 800]

        # draw blocks
        for _i in drawable_blocks:
                _i.draw(surface, self.camera)

        # draw entities
        for _i in self.level_entities:
            _i.draw(surface, self.camera)

    def set_state(self, state):
        """change state to specified state"""
        pass

    def state_surface(self):
        self.current = self.planet.surface
        self.level_objs = self.current.level_objs
        self.level_entities = self.current.level_entities
        self.player = self.current.player

        

    def state_system(self):
        pass


class Camera(object): # ie, offset
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = pygame.Rect(0, 0, width, height)

    def apply(self, target):
        # recalculate position of entity on screen to apply scrolling
        return target.rect.move(self.state.topleft)

    def update(self, target):
        # update the position of the camera
        self.state = self.camera_func(self.state, target.rect) 

def simple_camera(camera, target_rect):
    l, t, _, _ = target_rect # l = left,  t = top
    _, _, w, h = camera      # w = width, h = height
    return pygame.Rect(-l+constants.HALF_SCREEN_WIDTH, -t+constants.HALF_SCREEN_HEIGHT, w, h)  


if __name__ == '__main__':
    game = World()
    game.go()