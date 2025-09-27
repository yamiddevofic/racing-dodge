import pygame
from config import ALTO, ANCHO
import random
# Cache de imágenes para optimizar rendimiento
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
    contador_tiempo = contador_tiempo_actual + 1  # Incrementar contador de tiempo

    # Precomputar enemigos esperando solo si es necesario
    if enemigo_activo is None and contador_tiempo >= 60:
        enemigos_esperando = [i for i, enemigo in enumerate(enemigos) if enemigo[2] == 0]
        if enemigos_esperando:
            enemigo_activo = random.choice(enemigos_esperando)
            contador_tiempo = 0  # Resetear contador

    # Modificar enemigos in-place para evitar crear nueva lista
    for i, enemigo in enumerate(enemigos):
        if enemigo[2] == 0 and i == enemigo_activo:  # Este enemigo debe empezar a caer
            enemigo[2] = 1  # Cambiar a cayendo
            enemigo_activo = None  # Resetear el enemigo activo
        elif enemigo[2] == 1:  # Cayendo
            enemigo[1] += velocidad  # Mover enemigo
            # Si el enemigo sale de la pantalla por abajo, lo ocultamos
            if enemigo[1] > ALTO + 50:
                enemigo[2] = 2  # Ocultar enemigo

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
        # Clamp x to keep enemies within horizontal bounds
        if x < 0:
            x = 0
        if x + ancho > ANCHO:
            x = ANCHO - ancho
        # Do not clamp y at bottom, allow enemies to fall off screen
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
        # Respaldo: dibujar fondo azul y verde como antes
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
        # Respaldo: dibujar rectángulo
        color = (0, 255, 0) if tipo == 1 else (255, 0, 0)
        pygame.draw.rect(pantalla, color, (x, y, ancho, alto))
    

def colision_circulo_rectangulo(cx, cy, radio, rx, ry, rw, rh):
    """Detecta colisión entre un círculo y un rectángulo."""
    # Rechazo rápido basado en bounding box extendido
    if cx < rx - radio or cx > rx + rw + radio or cy < ry - radio or cy > ry + rh + radio:
        return False
    
    # Punto más cercano en el rectángulo al centro del círculo
    closest_x = max(rx, min(cx, rx + rw))
    closest_y = max(ry, min(cy, ry + rh))
    # Distancia
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
        # Si no se puede cargar la imagen, dibujar un círculo como respaldo
        pygame.draw.circle(pantalla, color, (x, y), radio)
