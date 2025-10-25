from typing import Any
from biblioteca import *

# Tipos (los que están comentados se definen en un módulo auxiliar)
# Celda = VACÍO | AGUA | BARCO  # contenido de una celda
Grilla = list[list[Celda]]      # una grilla, dada por una matriz de celdas
Tablero = tuple[Grilla,Grilla]       # un tablero, dado por la grilla local y la grilla del oponente
Dimensiones = tuple[int,int]         # cantidad de filas (alto) y cantidad de columnas (ancho) de las grillas
Posición = tuple[str,int]            # una ubicación de una grilla, dada por una letra y un número
# Jugador = UNO | DOS           # identificador de jugador
Barco = int                     # definición de barco (sólo su tamaño)
BarcoEnGrilla = list[Posición]      # un barco ubicado en la grilla (lista de posiciones que ocupa en la grilla)
# Dirección = ARRIBA | ABAJO | IZQUIERDA | DERECHA
EstadoJuego = tuple[
    Dimensiones,                # dimensiones de las grillas
    list[Barco],                # barcos disponibles
    list[Jugador],              # turno
    Tablero,                    # tablero jugador 1
    Tablero                     # tablero jugador 2
]
## Ejercicio 1
def cantidadDeBarcosDeTamaño(barcos: list[BarcoEnGrilla], tamaño: int) -> int:
    """ Agregar docstring acá
    """
    return False # TODO: Implementame

## Ejercicio 2

def nuevoJuego(
        cantidadDeFilas: int,
        cantidadDeColumnas: int,
        barcosDisponibles: list[Barco]
    ) -> EstadoJuego:
    """ Agregar docstring acá
    """
    # TODO: Implementame
    return((5,5), [3, 3, 2], [UNO],
            ([[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]],
            [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]),
            ([[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]],
            [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]])
    )

## Ejercicio 3

def esEstadoDeJuegoVálido(estadoDeJuego: EstadoJuego) -> bool:
    """ Agregar docstring acá
    """
    return False # TODO: Implementame


## Ejercicio 4

def dispararEnPosición(estado_juego: EstadoJuego, posición: Posición) -> ResultadoDisparo:
    """ Agregar docstring acá
    """
    return NADA # TODO: Implementame


## Ejercicio 5

def barcosEnGrilla(grilla: Grilla) -> list[BarcoEnGrilla]:
    """ Agregar docstring acá
    """
    return [] # TODO: Implementame



