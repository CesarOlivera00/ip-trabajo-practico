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
    fila_vacia : list[str] = [VACÍO] * cantidadDeColumnas
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

## Ejercicio 3

def tamaños(barcos: list[BarcoEnGrilla]) -> list[int]:
    """ Funcion que toma una lista de tipo BarcoEnGrilla y a partir de ella hace una lista con los tamaños de cada barco; es decir
     una lista[Barco]"""
    lista_tamaños_de_barcos : list[int] = []
    for barco in barcos:
        lista_tamaños_de_barcos.append(len(barco))
    return lista_tamaños_de_barcos

def mismosElementos(lista1: list[Any], lista2: list[Any]) -> bool:
    """ Funcion que toma dos listas y se fija si, para un elemento determinado, coincide la cantidad de apariciones del elemento en
    cada una"""
    for elemento in lista1:
        if cantidadDeApariciones(elemento, lista1) != cantidadDeApariciones(elemento, lista2):
            return False
    for elemento in lista2:
        if cantidadDeApariciones(elemento, lista1) != cantidadDeApariciones(elemento, lista2):
            return False
    return True

def coincidenBarcosEnGrilla(barcos: list[Barco], grilla: Grilla) -> bool:
    """ Funcion que verifica si la lista de barcos representados a partir de su tamaño que está en
    estadoDeJuego tiene los mismos elementos que la lista que armó la función "tamaños" a partir
    de los barcos tipo BarcoEnGrilla que aparecen en la grilla dada """
    return mismosElementos(barcos, tamaños(barcosEnGrilla(grilla)))

def tableroValidoEnJuego(tablero: Tablero, estadoDeJuego: EstadoJuego) -> bool:
    """ Utiliza las funciones grillaLocal y grillaOponente, que toman la grilla local y la grilla oponente de un tablero, respectivamente,
    y se las da como parámetro a grillaValida, que se fija para cada una si cumplen las condiciones para ser válidas. También utiliza
    la función coincidenBarcosEnGrilla para verificar si los tamaños de barcos que están disponibles en estadoDeJuego son los mismos que
    fueron colocados en la grilla local del tablero. Cada tablero será valido si sus dos grillas cumplen las condiciones y si los barcos
    colocados son los disponibles """
    return (grillaVálidaEnJuego(grillaLocal(tablero), estadoDeJuego)
             and grillaVálidaEnJuego(grillaOponente(tablero), estadoDeJuego)
             and coincidenBarcosEnGrilla(barcosDisponibles(estadoDeJuego), grillaLocal(tablero)))

def seReflejanLosAtaquesCorrectamente(grilla1: Grilla, grilla2: Grilla) -> bool:
    """ Función que compara la grilla oponente del jugador 1 con la grilla local del jugador 2; devuelve True si los resultados de los 
    ataques realizados a la grilla local fueron correctamente reflejados en la grilla oponente """
    celda : int = len(grilla1[0])
    for i in range(len(grilla1)):
        for j in range(celda):
            if grilla1[i][j] != VACÍO:
                if grilla1[i][j] != grilla2[i][j]:
                    return False
    return True

def coincidenPosicionesAtacadas(tablero: Tablero, tableroOponente: Tablero) -> bool:
    """ Funcion que utiliza seReflejanLosAtaques para que la comparación de posiciones atacadas con las posiciones marcadas sea simetrica
    y funcione para el tablero local y oponente de ambos jugadores """
    return(seReflejanLosAtaquesCorrectamente(grillaOponente(tablero), grillaLocal(tableroOponente))
           and seReflejanLosAtaquesCorrectamente(grillaOponente(tableroOponente), grillaLocal(tablero)))

def esEstadoDeJuegoVálido(estadoDeJuego: EstadoJuego) -> bool:
    """ Funcion que engloba todo lo que se tiene que cumplir para que el estado de juego sea válido """
    if (cantidadDeFilasEstadoJuego(estadoDeJuego) < 1 or cantidadDeFilasEstadoJuego(estadoDeJuego) > 26
        or cantidadDeColumnasEstadoJuego(estadoDeJuego) <= 0 
        or len(barcosDisponibles(estadoDeJuego)) < 0
        or not tableroValidoEnJuego(tableroDeJugador(estadoDeJuego, UNO), estadoDeJuego)
        or not tableroValidoEnJuego(tableroDeJugador(estadoDeJuego, DOS), estadoDeJuego)
        or not coincidenPosicionesAtacadas(tableroDeJugador(estadoDeJuego,UNO), tableroDeJugador(estadoDeJuego,DOS))):
        return False
    return True    

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



