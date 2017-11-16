import sys, pygame
from scenes.home import Home #scenes will contain everything from players to buttons, what ever you need. Just think of main.py as a navigator for the scenes


class Main:
    def __init__(self):
        pygame.init()

        self.size = self.width, self.height = 1280, 720 #ratio 1.777
        self.screen = pygame.display.set_mode(self.size)

        self.scenes = {'home' : Home}
        self.current_scene = self.scenes['home']()



        #EVERYTHING BEFORE THIS
        self.start()

    def start(self):
        self.current_scene.init(self.screen)
        while True:
            self.current_scene.render(self.screen, pygame.event.get())

            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    sys.exit()
                self.current_scene.update(event)
                    

            pygame.display.update()
            # pygame.draw.circle(self.screen, (255, 255, 0), (100, 100), 100)
            
    # def change_scene(self, scene):
        #clear scene
        #set current_scene = scene
            

game = Main()

