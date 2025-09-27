import pygame
import sys
import json
import os
from config import ANCHO, ALTO, FPS, TITLE
from menus import main_menu, game_over_menu, pause_menu, win_menu
from game import *

SCORES_FILE = "scores.json"

def load_scores():
    if os.path.exists(SCORES_FILE):
        with open(SCORES_FILE, 'r') as f:
            return json.load(f)
    return []

def save_scores(scores):
    with open(SCORES_FILE, 'w') as f:
        json.dump(scores, f)

scores = load_scores()
high_score = max(scores) if scores else 0

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('game/assets/sounds/music.mp3')
pygame.mixer.music.set_volume(0.8)
screen = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

estado = "menu"

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if estado == "jugando":
                    estado = "paused"
                elif estado == "paused":
                    estado = "jugando"
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if estado == "menu":
                botones = main_menu(screen)
                if botones["play"].collidepoint(event.pos):
                    reset_game()
                    estado = "jugando"
                elif botones["quit"].collidepoint(event.pos):
                    running = False
            elif estado == "paused":
                botones = pause_menu(screen)
                if botones["continue"].collidepoint(event.pos):
                    estado = "jugando"
                elif botones["restart"].collidepoint(event.pos):
                    reset_game()
                    estado = "jugando"
                elif botones["quit"].collidepoint(event.pos):
                    running = False
            elif estado == "game_over":
                botones = game_over_menu(screen, juego.puntos, previous_high)
                if botones["retry"].collidepoint(event.pos):
                    reset_game()
                    estado = "jugando"
                elif botones["quit"].collidepoint(event.pos):
                    running = False
            elif estado == "win":
                botones = win_menu(screen, juego.puntos, previous_high)
                if botones["retry"].collidepoint(event.pos):
                    reset_game()
                    estado = "jugando"
                elif botones["quit"].collidepoint(event.pos):
                    running = False

    if estado == "jugando":
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.play(-1)
    elif estado == "paused":
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.stop()

    if estado == "menu":
        botones = main_menu(screen)
    elif estado == "jugando":
        result = run_game(screen)
        if result == "game_over":
            previous_high = high_score
            scores.append(juego.puntos)
            save_scores(scores)
            high_score = max(high_score, juego.puntos)
            estado = "game_over"
        elif result == "win":
            previous_high = high_score
            scores.append(juego.puntos)
            save_scores(scores)
            high_score = max(high_score, juego.puntos)
            estado = "win"
    elif estado == "game_over":
        botones = game_over_menu(screen, juego.puntos, previous_high)
    elif estado == "win":
        botones = win_menu(screen, juego.puntos, previous_high)

    pygame.display.flip()
    clock.tick(FPS)

if os.path.exists(SCORES_FILE):
    os.remove(SCORES_FILE)

pygame.quit()
sys.exit()
