import pygame
from config import BLANCO, AZUL, ROJO
from utils import draw_text

def main_menu(screen):
    screen.fill((0, 0, 0))
    title_rect = draw_text(screen, "RACING DODGE", 80, BLANCO, 500, 150)

    play_rect = draw_text(screen, "Jugar", 50, AZUL, 500, 300)
    if play_rect.collidepoint(pygame.mouse.get_pos()):
        play_rect = draw_text(screen, "Jugar", 50, ROJO, 500, 300)
    quit_rect = draw_text(screen, "Salir", 50, AZUL, 500, 400)
    if quit_rect.collidepoint(pygame.mouse.get_pos()):
        quit_rect = draw_text(screen, "Salir", 50, ROJO, 500, 400)

    paragraph_rect = draw_text(screen, "Creado por YamidDev", 50, BLANCO, 500, 500)

    return {"title": title_rect, "play": play_rect, "quit": quit_rect, "paragraph": paragraph_rect}


def game_over_menu(screen, score, previous_high_score):
    screen.fill((0, 0, 0))
    draw_text(screen, "GAME OVER", 80, BLANCO, 500, 200)
    draw_text(screen, f"Puntos obtenidos: {score}", 40, BLANCO, 500, 300)
    if score > previous_high_score:
        draw_text(screen, "¡Rompiste el record!", 40, BLANCO, 500, 350)
    else:
        draw_text(screen, f"Puntaje maximo: {previous_high_score}", 40, BLANCO, 500, 350)

    retry_rect = draw_text(screen, "Reintentar", 50, AZUL, 500, 450)
    if retry_rect.collidepoint(pygame.mouse.get_pos()):
        retry_rect = draw_text(screen, "Reintentar", 50, ROJO, 500, 450)
    quit_rect = draw_text(screen, "Salir", 50, AZUL, 500, 500)
    if quit_rect.collidepoint(pygame.mouse.get_pos()):
        quit_rect = draw_text(screen, "Salir", 50, ROJO, 500, 500)

    return {"retry": retry_rect, "quit": quit_rect}


def win_menu(screen, score, previous_high_score):
    screen.fill((0, 0, 0))
    draw_text(screen, "GANASTE", 80, BLANCO, 500, 200)
    draw_text(screen, f"Puntos obtenidos: {score}", 40, BLANCO, 500, 300)
    if score > previous_high_score:
        draw_text(screen, "¡Rompiste el record!", 40, BLANCO, 500, 350)
    else:
        draw_text(screen, f"Puntaje maximo: {previous_high_score}", 40, BLANCO, 500, 350)

    retry_rect = draw_text(screen, "Reintentar", 50, AZUL, 500, 450)
    if retry_rect.collidepoint(pygame.mouse.get_pos()):
        retry_rect = draw_text(screen, "Reintentar", 50, ROJO, 500, 450)
    quit_rect = draw_text(screen, "Salir", 50, AZUL, 500, 500)
    if quit_rect.collidepoint(pygame.mouse.get_pos()):
        quit_rect = draw_text(screen, "Salir", 50, ROJO, 500, 500)

    return {"retry": retry_rect, "quit": quit_rect}


def pause_menu(screen):
    screen.fill((0, 0, 0))
    draw_text(screen, "PAUSA", 80, BLANCO, 500, 150)

    continue_rect = draw_text(screen, "Continuar", 50, AZUL, 500, 250)
    if continue_rect.collidepoint(pygame.mouse.get_pos()):
        continue_rect = draw_text(screen, "Continuar", 50, ROJO, 500, 250)
    restart_rect = draw_text(screen, "Reiniciar", 50, AZUL, 500, 350)
    if restart_rect.collidepoint(pygame.mouse.get_pos()):
        restart_rect = draw_text(screen, "Reiniciar", 50, ROJO, 500, 350)
    quit_rect = draw_text(screen, "Salir", 50, AZUL, 500, 450)
    if quit_rect.collidepoint(pygame.mouse.get_pos()):
        quit_rect = draw_text(screen, "Salir", 50, ROJO, 500, 450)

    return {"continue": continue_rect, "restart": restart_rect, "quit": quit_rect}
