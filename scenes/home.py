import pygame

class Home:
    def render(screen):
        ball = pygame.image.load("./res/imgs/ball.png")
        ballrect = ball.get_rect()
        screen.blit(ball, ballrect)
        pygame.draw.circle(screen, (255, 0, 0), (0, 0), 100)