import pygame
from .button import button

class Home:
    def __init__(self):
        pass

    def init(self, screen):

        #init images
        self.background = pygame.image.load("./res/menu/Night Sky.png")
        self.background_rect = self.background.get_rect()

        self.earth = pygame.image.load('./res/menu/earth725.png')
        self.earty_rect = self.earth.get_rect()

    def render(self, screen, event):

        #render images
        screen.blit(self.background, self.background_rect)
        screen.blit(self.earth, self.earty_rect)

        button(screen, None, pygame.mouse.get_pos(), pygame.mouse.get_pressed(), text='test')
        
        # pygame.draw.circle(screen, (255, 0, 0), (0, 0), 100)


    def update(self, event):
        # print('update')
        #update things
        pass
