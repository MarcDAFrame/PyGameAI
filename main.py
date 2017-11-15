import sys, pygame
import game_map
from scenes.home import Home

class Main:
    def __init__(self):
        pygame.init()

        self.size = self.width, self.height = 960, 540 #ratio 1.777
        self.screen = pygame.display.set_mode(self.size)

        self.scenes = {'home' : Home}
        self.current_scene = self.scenes['home']


        self.ball = pygame.image.load("./res/imgs/ball.png")
        print(self.ball)
        self.ballrect = self.ball.get_rect()

        #EVERYTHING BEFORE THIS
        self.start()

    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    sys.exit()
                    
            self.current_scene.render(self.screen)
            self.screen.blit(self.ball, self.ballrect)
            pygame.display.update()
            # pygame.draw.circle(self.screen, (255, 255, 0), (100, 100), 100)
            
    # def change_scene(self, scene):
        #clear scene
        #set current_scene = scene
            

game = Main()

