from typing import Any
from biblioteca import *

## Ejercicio 1
def cantidadDeBarcosDeTamaño(barcos: list[BarcoEnGrilla], tamaño: int) -> int:
   cantidad : int = 0
   for barco in barcos:
        if len(barco) == tamaño:
            cantidad += 1
   return cantidad

## Ejercicio 2

def grillaVacia(cantidadDeFilas: int, cantidadDeColumnas: int) -> Grilla:
    """Función que arma cada una de las grillas a partir de la cantidad de filas y columnas"""
    grilla_res : Grilla = []
    fila_vacia : list[str] = ["VACÍO"] * cantidadDeColumnas
    i : int = 0
    while i < cantidadDeFilas:
        grilla_res.append(fila_vacia.copy())
        i += 1
    return grilla_res

def nuevoTablero(cantidadDeFilas: int, cantidadDeColumnas: int) -> Tablero:
    """Funcion que arma cada tablero para cada jugador a partir de las dos grillas vacias; cada uno tiene ahora
    un tablero con una grilla local, y una grilla oponente"""
    return(grillaVacia(cantidadDeFilas, cantidadDeColumnas), grillaVacia(cantidadDeFilas, cantidadDeColumnas))

def nuevoJuego(cantidadDeFilas: int, cantidadDeColumnas: int, barcosDisponibles: list[Barco]) -> EstadoJuego:
    """ Funcion que devuelve el estado de Juego inicial, indicando, en una tupla, las dimensiones de cada una de las grillas,
     la longitud de cada uno de los barcos que se disponen en forma de lista, y los dos tableros vacíos """
    return((cantidadDeFilas, cantidadDeColumnas),
            barcosDisponibles,
            [UNO],
            nuevoTablero(cantidadDeFilas, cantidadDeColumnas),
            nuevoTablero(cantidadDeFilas, cantidadDeColumnas))

# en el return de ejemplo en la parte de "barcosDisponibles" devuelve [3,3,2]; creo que haciendo referencia a que cuando inicia
# el juego la hay 3 barcos que se disponen para colocar en la grilla local (dos de longitud 3 y uno de longitud 2), la funcion
# que hice no devuelve una lista así, devuelve barcosDisponibles tal cual se metió a la funcion, no se si lo correcto sería
# hacer una funcion que tambien a partir del numero metido(q es la cantidad de barcos que voy a disponer para colocar) cree
# una lista con barcos de longitudes al azar, o si esta bien q devuelva el barcosDisponibles asi como está (porque en 
# el enunciado en el ejemplo lo devuelven asi como está)

"""    #TODO: Implementame
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
"""


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



