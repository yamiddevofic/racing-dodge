# Racing Dodge - Proyecto PyGame 🏎️

**Prueba Técnica - 2025**
**Tutor: Python - Trabajo Práctico**

## Descripción del Proyecto

Racing Dodge es un juego desarrollado en Python utilizando la librería **PyGame** que implementa un sistema de carreras donde el jugador debe esquivar coches enemigos mientras recolecta monedas para aumentar su puntuación.

### Criterios de Evaluación Cumplidos

✅ **Uso de PyGame**: El proyecto utiliza exclusivamente PyGame para gráficos, sonido y gestión de eventos  
✅ **Funciones personalizadas**: Implementación extensiva de funciones personalizadas en módulos separados  
✅ **Múltiples funciones, menús y enemigos**: Sistema completo con diferentes tipos de enemigos y menús interactivos  
✅ **Archivo README descriptivo**: Este documento detalla la funcionalidad y arquitectura del proyecto  

## Características Técnicas

### Arquitectura del Código

El proyecto sigue una arquitectura modular con separación de responsabilidades:

- **Módulo [`game/main.py`](game/main.py:1)**: Bucle principal del juego y gestión de estados
- **Módulo [`game/game.py`](game/game.py:1)**: Lógica del juego con clases Jugador y Enemigo
- **Módulo [`game/functions.py`](game/functions.py:1)**: Funciones utilitarias personalizadas
- **Módulo [`game/menus.py`](game/menus.py:1)**: Sistema de menús interactivos
- **Módulo [`game/config.py`](game/config.py:1)**: Configuración centralizada
- **Módulo [`game/utils.py`](game/utils.py:1)**: Utilidades de renderizado

### Funciones Personalizadas Implementadas

El proyecto incluye **más de 15 funciones personalizadas** distribuidas en diferentes módulos:

#### En [`game/functions.py`](game/functions.py:1):
- [`manejar_eventos()`](game/functions.py:8): Gestión de eventos del sistema
- [`mover_jugador()`](game/functions.py:16): Movimiento del jugador con teclado
- [`mover_enemigos()`](game/functions.py:25): Sistema de movimiento de enemigos optimizado
- [`aplicar_limites()`](game/functions.py:50): Restricciones de movimiento en pantalla
- [`dibujar_escena_paisaje()`](game/functions.py:77): Renderizado del fondo con caché
- [`dibujar_enemigo()`](game/functions.py:97): Renderizado de enemigos con sprites
- [`colision_circulo_rectangulo()`](game/functions.py:117): Detección avanzada de colisiones
- [`dibujar_jugador()`](game/functions.py:130): Renderizado del jugador con sprites

#### En [`game/utils.py`](game/utils.py:1):
- [`draw_text()`](game/utils.py:3): Sistema de renderizado de texto centrado

#### En [`game/menus.py`](game/menus.py:1):
- [`main_menu()`](game/menus.py:5): Menú principal con efectos hover
- [`game_over_menu()`](game/menus.py:26): Menú de fin de juego
- [`win_menu()`](game/menus.py:50): Menú de victoria
- [`pause_menu()`](game/menus.py:74): Menú de pausa

### Sistema de Enemigos

El juego implementa **dos tipos de enemigos** con comportamientos distintos:

1. **Coches rojos** (tipo 0): Causan game over al colisionar
2. **Monedas** (tipo 1): Otorgan puntos al ser recolectadas

Cada enemigo tiene un sistema de estados (esperando, cayendo, eliminado) y se gestionan mediante la clase [`Enemigo`](game/game.py:22) en [`game/game.py`](game/game.py:1).

## Guía de Instalación y Uso - Paso a Paso

### Paso 1: Verificar Requisitos del Sistema
- **Python 3.12 o superior** instalado en el sistema
- Acceso a línea de comandos (Terminal/CMD/PowerShell)

### Paso 2: Descargar el Proyecto
```bash
# Si tienes Git instalado:
git clone git@github.com:yamiddevofic/racing-dodge.git
cd dodge_the_blocks

# Si descargas el proyecto como ZIP:
# 1. Extrae el archivo ZIP en una carpeta
# 2. Abre la terminal en la carpeta extraída
```

### Paso 3: Instalar Dependencias
```bash
# Instalar PyGame y dependencias
pip install -r requirements.txt

# Si encuentras problemas, instalar PyGame directamente:
pip install pygame
```

### Paso 4: Verificar la Instalación
```bash
# Verificar que Python esté instalado
python3 --version

# Verificar que PyGame se instaló correctamente
python3 -c "import pygame; print('PyGame instalado correctamente')"
```

### Paso 5: Ejecutar el Juego
```bash
# Desde la carpeta principal del proyecto
python3 game/main.py
```

### Paso 6: Controles del Juego
Una vez ejecutado el juego:
- **Menú Principal**: Usa el mouse para hacer clic en "Jugar" o "Salir"
- **Durante el Juego**:
  - **Tecla A**: Mover coche a la izquierda
  - **Tecla D**: Mover coche a la derecha
  - **ESC**: Pausar/Reanudar juego
- **Menús**: Siempre usa el mouse para interactuar con botones

### Solución de Problemas Comunes

**Error: "ModuleNotFoundError: No module named 'pygame'"**
```bash
pip install pygame
```

**Error: Las imágenes no se cargan**
- Verifica que los archivos existan en `game/assets/images/`
- Asegúrate de ejecutar desde la carpeta correcta

**El juego no inicia**
- Verifica que Python 3.12+ esté instalado
- Ejecuta `python3 --version` para confirmar

## Estructura del Proyecto

```
racing-dodge/
├── game/
│   ├── main.py              # Punto de entrada principal
│   ├── game.py              # Lógica del juego con clases
│   ├── config.py            # Configuración global
│   ├── menus.py             # Sistema de menús
│   ├── functions.py         # Funciones utilitarias personalizadas
│   ├── utils.py             # Utilidades de renderizado
│   └── assets/
│       ├── images/          # Sprites del juego
│       │   ├── player.png   # Jugador
│       │   ├── enemy.png    # Enemigos
│       │   ├── money.png    # Monedas
│       │   └── run.png      # Fondo
│       └── sounds/          # Efectos de sonido
│           ├── music.mp3    # Música
│           └── cash.mp3     # Sonido monedas
├── requirements.txt         # Dependencias
└── README.md               # Este archivo
```

## Funcionalidades Implementadas

### Sistema de Juego
- ✅ Movimiento del jugador con teclado (teclas A/D)
- ✅ Generación procedural de enemigos
- ✅ Sistema de colisiones avanzado
- ✅ Mecánica de recolección de monedas
- ✅ Condiciones de victoria/derrota
- ✅ Sistema de puntuación persistente

### Sistema de Menús
- ✅ Menú principal interactivo
- ✅ Menú de pausa funcional
- ✅ Menús de game over y victoria
- ✅ Efectos hover en botones
- ✅ Navegación entre estados del juego

### Optimizaciones Técnicas
- ✅ Cache de imágenes para mejor rendimiento
- ✅ Gestión eficiente de memoria
- ✅ Sistema de estados del juego
- ✅ Separación clara de responsabilidades

## Controles

- **Tecla A**: Mover a la izquierda
- **Tecla D**: Mover a la derecha
- **ESC**: Pausar/Reanudar juego
- **Click**: Interactuar con menús

## Evaluación de Criterios

### ✅ Uso de PyGame
El proyecto utiliza PyGame para:
- Renderizado de gráficos 2D
- Gestión de eventos de teclado y mouse
- Reproducción de música y efectos de sonido
- Control de tiempo y FPS

### ✅ Funciones Personalizadas
Se han implementado funciones personalizadas que incluyen:
- Movimiento y física de entidades
- Detección de colisiones avanzada
- Sistemas de renderizado optimizados
- Gestión de estados del juego
- Interfaz de usuario interactiva

### ✅ Múltiples Funciones, Menús y Enemigos
- **Funciones**: Más de 15 funciones personalizadas
- **Menús**: 4 menús diferentes (principal, pausa, game over, victoria)
- **Enemigos**: 2 tipos con comportamientos distintos (coches rojos y monedas)

### ✅ Documentación Completa
Este README describe detalladamente:
- Arquitectura del código
- Funcionalidades implementadas
- Criterios de evaluación cumplidos
- Instrucciones de instalación y uso

## Conclusión

Este proyecto demuestra competencia en el desarrollo de juegos con PyGame, implementando una arquitectura modular con funciones personalizadas, sistema de menús completo y diferentes tipos de enemigos. Cumple con todos los criterios de evaluación establecidos para la prueba técnica.

**Desarrollado por:** Yamid Dev  
**Tecnologías:** Python 3, PyGame  
**Fecha de entrega:** 2025
