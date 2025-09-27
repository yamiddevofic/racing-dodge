import pygame

def draw_text(screen, text, font_size, color, x, y, center=True):
    font = pygame.font.Font(None, font_size)
    surface = font.render(text, True, color)
    rect = surface.get_rect()
    if center:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)
    screen.blit(surface, rect)
    return rect
