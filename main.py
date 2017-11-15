import sys, pygame
import game_map

class Main:
    def __init__(self):
        pygame.init()

        size = width, height = 960, 540 #ratio 1.777
        screen = pygame.display.set_mode(size)
        self.start()
        print('test')

    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
                    break

game = Main()

