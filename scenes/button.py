import pygame
def button(screen, target, mouse, click, shape=(150,450,100,50), color=(0, 255, 0), text=None):
    if shape[0]+shape[2] > mouse[0] > shape[0] and shape[1]+shape[3] > mouse[1] > shape[1]:
        if click[0] == 1:
            pygame.draw.rect(screen, (255, 0,0), shape)
        else:
            pygame.draw.rect(screen, color, shape)
    else:
        pygame.draw.rect(screen, color, shape)

    if text:
        font_text = pygame.font.Font('freesansbold.ttf',shape[3])
        TextSurf, TextRect = text_objects(text, font_text)
        TextRect.center = ((shape[0]),(shape[1]))
        screen.blit(TextSurf, TextRect)


def text_objects(text, font, color=(255,255,255)):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()