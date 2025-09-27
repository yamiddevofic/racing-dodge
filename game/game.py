import pygame
import random
from config import ANCHO, ALTO, JUGADOR_RADIO, JUGADOR_VELOCIDAD, ROJO, AMARILLO, VERDE, ENEMIGO_RADIO, ENEMIGO_VELOCIDAD, ENEMIGO_ANCHO, ENEMIGO_ALTO, BLANCO
from functions import mover_jugador, aplicar_limites, dibujar_escena_paisaje, dibujar_jugador, dibujar_enemigo, mover_enemigos, aplicar_limites_enemigos, colision_circulo_rectangulo
from utils import draw_text

class Jugador:
    def __init__(self):
        self.x = ANCHO // 2
        self.y = ALTO * 0.8
        self.radio = JUGADOR_RADIO
        self.velocidad = JUGADOR_VELOCIDAD
        self.color = AMARILLO

    def mover(self):
        self.x, self.y = mover_jugador(self.x, self.y, self.velocidad)
        self.x, self.y = aplicar_limites(self.x, self.y, self.radio)

    def dibujar(self, pantalla):
        dibujar_jugador(pantalla, self.x, self.y, self.color, self.radio)

class Enemigo:
    def __init__(self, x, y, tipo):
        self.x = x
        self.y = y
        self.estado = 0  # 0 = esperando, 1 = cayendo, 2 = eliminado
        self.temporizador = 0
        self.tipo = tipo  # 0 = coche rojo (peligro), 1 = moneda (puntos)
        self.ancho = ENEMIGO_ANCHO
        self.alto = ENEMIGO_ALTO

    def mover(self, velocidad):
        if self.estado == 1:  # Cayendo
            self.y += velocidad
            if self.y > ALTO + 50:
                self.estado = 2  # Ocultar enemigo

    def activar(self):
        if self.estado == 0:
            self.estado = 1

    def dibujar(self, pantalla):
        if self.estado == 1:  # Solo dibujar enemigos que están cayendo
            dibujar_enemigo(pantalla, self.x, self.y, self.tipo, self.ancho, self.alto)

    def aplicar_limites(self):
        if self.x < 0:
            self.x = 0
        if self.x + self.ancho > ANCHO:
            self.x = ANCHO - self.ancho
        if self.y < 0:
            self.y = 0

    def colisiona_con(self, jugador_x, jugador_y, jugador_radio):
        if self.estado != 1:
            return False
            
        # Verificación rápida de bounding box
        if (jugador_x + jugador_radio >= self.x and 
            jugador_x - jugador_radio <= self.x + self.ancho and
            jugador_y + jugador_radio >= self.y and 
            jugador_y - jugador_radio <= self.y + self.alto):
            
            return colision_circulo_rectangulo(jugador_x, jugador_y, jugador_radio, 
                                             self.x, self.y, self.ancho, self.alto)
        return False

class Juego:
    def __init__(self):
        self.jugador = Jugador()
        self.puntos = 0
        self.enemigos = []
        self.enemigo_activo = None
        self.contador_tiempo = 0
        self.tiempo_entre_enemigos = 111
        
        for i in range(100):
            tipo = 0 if i < 50 else 1
            x = random.randint(0, ANCHO - ENEMIGO_ANCHO)
            self.enemigos.append(Enemigo(x, ALTO * 0.1, tipo))

    def reset(self):
        self.jugador = Jugador()
        self.puntos = 0
        self.enemigos = []
        self.enemigo_activo = None
        self.contador_tiempo = 0
        
        for i in range(100):
            tipo = 0 if i < 50 else 1  
            x = random.randint(0, ANCHO - ENEMIGO_ANCHO)
            self.enemigos.append(Enemigo(x, ALTO * 0.1, tipo))

    def mover_enemigos(self):
        self.contador_tiempo += 1

        if self.enemigo_activo is None and self.contador_tiempo >= 60:
            enemigos_esperando = [i for i, enemigo in enumerate(self.enemigos) if enemigo.estado == 0]
            if enemigos_esperando:
                self.enemigo_activo = random.choice(enemigos_esperando)
                self.contador_tiempo = 0

        for i, enemigo in enumerate(self.enemigos):
            if enemigo.estado == 0 and i == self.enemigo_activo:
                enemigo.activar()
                self.enemigo_activo = None
            elif enemigo.estado == 1:
                enemigo.mover(ENEMIGO_VELOCIDAD)
                enemigo.aplicar_limites()

    def verificar_colisiones(self):
        for enemigo in self.enemigos:
            if enemigo.colisiona_con(self.jugador.x, self.jugador.y, self.jugador.radio):
                if enemigo.tipo == 1:
                    self.puntos += 1
                    if not hasattr(self, 'coin_sound'):
                        self.coin_sound = pygame.mixer.Sound('game/assets/sounds/cash.mp3')
                    self.coin_sound.play()
                    enemigo.estado = 2
                else:
                    if not hasattr(self, 'crash_sound'):
                        self.crash_sound = pygame.mixer.Sound('game/assets/sounds/not-a-big-crash.mp3')
                    self.crash_sound.play()
                    return False
        return True

    def todos_enemigos_eliminados(self):
        return all(enemigo.estado == 2 for enemigo in self.enemigos)

    def dibujar(self, pantalla):
        dibujar_escena_paisaje(pantalla)
        
        for enemigo in self.enemigos:
            enemigo.dibujar(pantalla)
            
        self.jugador.dibujar(pantalla)
        draw_text(pantalla, f"Puntos: {self.puntos}", 30, BLANCO, ANCHO//2, 30, center=True)

    def ejecutar(self, pantalla):
        self.jugador.mover()
        self.mover_enemigos()

        if not self.verificar_colisiones():
            return "game_over"

        if self.todos_enemigos_eliminados():
            return "win"

        self.dibujar(pantalla)
        return "continue"


juego = Juego()

def reset_game():
    juego.reset()

def run_game(screen):
    return juego.ejecutar(screen)
