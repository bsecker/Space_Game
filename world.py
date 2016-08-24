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

    def event_loop(self):
        """main event loop"""
        for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    self.game_running = False
     
                if event.type == pygame.KEYDOWN:
                    # Quit Game
                    if event.key == pygame.K_ESCAPE:
                        self.game_running = False

    def draw(self, surface):
        surface.fill(self.current.bg_colour)

        for _i in self.level_objs:
            _i.draw(surface)

    def set_state(self, state):
        """change state to specified state"""
        pass

    def state_surface(self):
        self.current = self.planet.surface
        self.level_objs = self.current.level_objs

    def state_system(self):
        pass