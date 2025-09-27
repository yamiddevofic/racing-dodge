import pygame
from config import ALTO, ANCHO
import random
_image_cache = {}


def manejar_eventos():
    """Procesa eventos como cerrar la ventana."""
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            return False
    return True


def mover_jugador(x, y, velocidad):
    """Mueve al jugador horizontalmente según las teclas presionadas."""
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_a]:
        x -= velocidad
    if teclas[pygame.K_d]:
        x += velocidad
    return x, y

def mover_enemigos(enemigos, velocidad, enemigo_activo_actual, contador_tiempo_actual):
    """Mueve los enemigos según su estado (esperando, cayendo, terminado)."""
    enemigo_activo = enemigo_activo_actual

    if enemigo_activo is None and contador_tiempo >= 60:
        enemigos_esperando = [i for i, enemigo in enumerate(enemigos) if enemigo[2] == 0]
        if enemigos_esperando:
            enemigo_activo = random.choice(enemigos_esperando)
            contador_tiempo = 0

    for i, enemigo in enumerate(enemigos):
        if enemigo[2] == 0 and i == enemigo_activo:
            enemigo[2] = 1
            enemigo_activo = None
        elif enemigo[2] == 1:
            enemigo[1] += velocidad
            if enemigo[1] > ALTO + 50:
                enemigo[2] = 2

    return enemigos, enemigo_activo, contador_tiempo

def aplicar_limites(x, y, radio):
    """Evita que el jugador salga de la pantalla."""
    if x - radio < 0:
        x = radio
    if x + radio > ANCHO:
        x = ANCHO - radio
    if y - radio < 0:
        y = radio
    if y + radio > ALTO:
        y = ALTO - radio
    return x, y

def aplicar_limites_enemigos(enemigos, ancho, alto):
    nuevos_enemigos = []
    for enemigo in enemigos:
        x, y, estado, temporizador, tipo = enemigo
        if x < 0:
            x = 0
        if x + ancho > ANCHO:
            x = ANCHO - ancho
        if y < 0:
            y = 0
        nuevos_enemigos.append([x, y, estado, temporizador, tipo])
    return nuevos_enemigos

def dibujar_escena_paisaje(pantalla):
    """Dibuja el fondo del juego usando la imagen run.png."""
    imagen_path = 'game/assets/images/run.png'
    cache_key = (imagen_path, ANCHO, ALTO)
    
    if cache_key not in _image_cache:
        try:
            imagen_fondo = pygame.image.load(imagen_path).convert()
            imagen_fondo = pygame.transform.scale(imagen_fondo, (ANCHO, ALTO))
            _image_cache[cache_key] = imagen_fondo
        except pygame.error:
            _image_cache[cache_key] = None
    
    if _image_cache[cache_key] is not None:
        pantalla.blit(_image_cache[cache_key], (0, 0))
    else:
        pantalla.fill((0, 0, 255))
        pygame.draw.rect(pantalla, (0, 255, 0), (0, ALTO * 0.85, ANCHO, ALTO * 0.15))

def dibujar_enemigo(pantalla, x, y, tipo, ancho, alto):
    imagen_path = 'game/assets/images/money.png' if tipo == 1 else 'game/assets/images/enemy.png'
    cache_key = (imagen_path, ancho, alto)
    
    if cache_key not in _image_cache:
        try:
            imagen_enemigo = pygame.image.load(imagen_path).convert_alpha()
            imagen_enemigo = pygame.transform.scale(imagen_enemigo, (ancho, alto))
            _image_cache[cache_key] = imagen_enemigo
        except pygame.error:
            _image_cache[cache_key] = None
    
    if _image_cache[cache_key] is not None:
        pantalla.blit(_image_cache[cache_key], (x, y))
    else:
        color = (0, 255, 0) if tipo == 1 else (255, 0, 0)
        pygame.draw.rect(pantalla, color, (x, y, ancho, alto))
    

def colision_circulo_rectangulo(cx, cy, radio, rx, ry, rw, rh):
    """Detecta colisión entre un círculo y un rectángulo."""
    if cx < rx - radio or cx > rx + rw + radio or cy < ry - radio or cy > ry + rh + radio:
        return False
    
    closest_x = max(rx, min(cx, rx + rw))
    closest_y = max(ry, min(cy, ry + rh))
    
    distance = ((cx - closest_x) ** 2 + (cy - closest_y) ** 2) ** 0.5
    return distance < radio

def dibujar_jugador(pantalla, x, y, color, radio):
    """Dibuja al jugador en pantalla."""
    imagen_path = 'game/assets/images/player.png'
    ancho_imagen = radio * 3
    alto_imagen = radio * 3
    cache_key = (imagen_path, ancho_imagen, alto_imagen)
    
    if cache_key not in _image_cache:
        try:
            imagen_carro = pygame.image.load(imagen_path).convert_alpha()
            imagen_carro = pygame.transform.scale(imagen_carro, (ancho_imagen, alto_imagen))
            _image_cache[cache_key] = imagen_carro
        except pygame.error:
            _image_cache[cache_key] = None
    
    if _image_cache[cache_key] is not None:
        rect = _image_cache[cache_key].get_rect(center=(x, y))
        pantalla.blit(_image_cache[cache_key], rect)
    else:
        pygame.draw.circle(pantalla, color, (x, y), radio)
