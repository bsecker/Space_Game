# Import files
try:
    import sys
    import pygame
    import constants
    import random

except ImportError, _err:
    print("couldn't load module. {0}".format(_err))
    sys.exit() 

def main():
    # Initialise Pygame
    pygame.init()

    screen_size = (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption(constants.WIN_CAPTION)

    FPSCLOCK = pygame.time.Clock()

    # generate random world
    def _random(_min, _max, nodes):
        node_list = []
        # using dads thing that average of 12 tends towards standard dist.
        for _i in range(nodes):
            temp_node_list = [random.randrange(_min, _max) for i in range(12)]
            node_list.append(sum(temp_node_list) / len(temp_node_list))
        return node_list

    planets = _random(0,640,1000)

    game_running = True
    while game_running:
        screen.fill(constants.BG_COLOUR)
        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                break

            if event.type == pygame.KEYDOWN:
                
                # Quit Game
                if event.key == pygame.K_ESCAPE:
                    game_running = False
        # Draw
        for _i in planets:
            pygame.draw.circle(screen, constants.WHITE, (_i, 250), 5)

        FPSCLOCK.tick(constants.FPS)
        pygame.display.update()

if __name__ == '__main__':
    main()