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
            "UNO",
            nuevoTablero(cantidadDeFilas, cantidadDeColumnas),
            nuevoTablero(cantidadDeFilas, cantidadDeColumnas))

## Ejercicio 3

# ACLARACION: ESTE EJERCICIO ESTA INCOMPLETO Y NO VA A EJECUTAR PORQUE EN LA FUNCION "coincidenBarcosEnGrilla" UTILIZA LA FUNCION 
# "BARCOSENGRILLA" QUE TIENE QUE SER IMPLEMENTADA EN EL EJERCICIO 5

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
        or len(barcosDisponibles(estadoDeJuego)) <= 0
        or not tableroValidoEnJuego(tableroDeJugador(estadoDeJuego, UNO), estadoDeJuego)
        or not tableroValidoEnJuego(tableroDeJugador(estadoDeJuego, DOS), estadoDeJuego)
        or not coincidenPosicionesAtacadas(tableroDeJugador(estadoDeJuego,UNO), tableroDeJugador(estadoDeJuego,DOS))):
        return False
    return True    

## Ejercicio 4


def dispararEnPosición(estado_juego: EstadoJuego, posición: Posición) -> ResultadoDisparo:
    """ Agregar docstring acá
        Cambia el turno del jugador y modifica las grillas de los tableros de ambos jugadores segun lo que se encuentre en la posicion
        Args: 
            estado_juego (EstadoJuego):
            posicion (Posicion):

        Returs:
            TOCADO Si en la posicion existe un barco y Nada en caso contrario.
         
    """

    valorCelda: Celda = celdaEnPosición(grillaLocal(tableroDeJugador(estado_juego, turnoContrario(turno(estado_juego)))),posición)

    if valorCelda == Celda.VACÍO :
        cambiarCeldaGrilla(grillaLocal(tableroDeJugador(estado_juego, turnoContrario(turno(estado_juego)))),posición, AGUA)
        cambiarCeldaGrilla(grillaOponente(tableroDeJugador(estado_juego, turno(estado_juego))),posición, AGUA)
    else:
        cambiarCeldaGrilla(grillaOponente(tableroDeJugador(estado_juego, turno(estado_juego))),posición, BARCO)

    cambiarTurno(estado_juego)

    return TOCADO if valorCelda == BARCO else NADA

def turnoContrario(jugador: Jugador):
    return DOS if jugador == UNO else UNO

## Ejercicio 5

def barcosEnGrilla(grilla: Grilla) -> list[BarcoEnGrilla]:
    """ Recorre la *grilla* completa para obtener las posiciones de ocupadas por barcos.
        PRE: esGrillaVálida(grilla)
        Args:
            grilla (Grilla): La grilla que contiene los barcos a ubicar.
        Returns:
            Lista de los barcos (list[BarcoEnGrilla]) encontrados en la * grilla*.
    """
    barcosEnGrilla:list[BarcoEnGrilla] = []

    for filaNro in range(cantidadDeFilasGrilla(grilla)):
        recorrerFilaYGuardarPosicionesDeBarcosEnGrilla(filaNro, grilla, barcosEnGrilla)

    return barcosEnGrilla

def recorrerFilaYGuardarPosicionesDeBarcosEnGrilla(filaNro:int, grilla:Grilla, barcosEnGrilla:list[BarcoEnGrilla]) -> None:
    """ Recorre la fila *filaNro* de una grilla y guardas las posiciones de los barcos, en esa fila, en una lista de BarcoEnGrilla.
        PRE: esGrillaVálida(grilla)
        PRE: 0 <= *filaNro* < cantidadDeFilasGrilla(grilla)
        Args:
            filaNro (int): El nro de fila a recorrer de la grilla.
            grilla (Grilla): La grilla que contiene los barcos a ubicar.
            barcosEnGrilla (list[BarcoEnGrilla]): Lista a llenar con las posiciones de los barcos.
        Returns:
            None
    """
    for celdaNro in range(cantidadDeColumnasGrilla(grilla)):
        if enEstaPosicionDeGrillaHayParteDeUnBarco(grilla, filaNro, celdaNro):
            posicionBarcoEnGrilla:Posición = (letraDeFilaNro(filaNro + 1), celdaNro + 1)
            encontroPosicionAdyacente:bool = ubicarPosicionEnBarcosEnGrillaAUnaPosicionAdyacenteSiExiste(barcosEnGrilla, posicionBarcoEnGrilla)
            
            if not encontroPosicionAdyacente:
                agregarPosicionEnBarcosEnGrillaComoNuevaLista(barcosEnGrilla, posicionBarcoEnGrilla)

def enEstaPosicionDeGrillaHayParteDeUnBarco(grilla:Grilla, filaNro:int, celdaNro:int) -> bool:
    """ Dado las cordenadas numericas *filaNro* y *celdaNro*, revisa si en la *grilla* hay un barco.
        PRE: esGrillaVálida(grilla)
        PRE: 0 <= *filaNro* < cantidadDeFilasGrilla(grilla)
        PRE: 0 <= *celdaNro* < cantidadDeColumnasGrilla(grilla)
        Args:
            grilla (Grilla): La grilla que contiene los barcos a ubicar.
            filaNro (int): Numero de fila de la grilla.
            celdaNro (int): Numero de columna de la grilla.
        Returns:
            True si en la posicion indicada por las coordenadas hay un barco. False, en caso contrario.
    """
    return grilla[filaNro][celdaNro] == BARCO

def ubicarPosicionEnBarcosEnGrillaAUnaPosicionAdyacenteSiExiste(barcosEnGrilla:list[BarcoEnGrilla], posicionBarcoEnGrilla:Posición) -> bool:
    """ Ubica la la posicion *posicionBarcoEnGrilla* en la lista correspondiente de *barcosEnGrilla* segun haya una posicion adyacente,
            si no, crea una nueva lista de posiciones para el barco.
        PRE: esPosiciónVálida(posicionBarcoEnGrilla)
        Args:
            barcosEnGrilla (list[BarcoEnGrilla]): Lista a llenar con las posiciones de los barcos.
            posicionBarcoEnGrilla (Posición): Posicion a ubicar en *barcosEnGrilla* donde haya una posicion adyacente.
        Returns:
            True si ecuentra una posicion adyacente para *posicionBarcoEnGrilla* dentro de *barcosEnGrilla*. False, en caso contrario.
    """
    encontroPosicionAdyacente:bool = False

    for indiceBarco in range(len(barcosEnGrilla)):
        encontroPosicionAdyacente = recorrerPoscionesDelBarcoYGuardarSiLaPosicionEsAdyacente(barcosEnGrilla, indiceBarco, posicionBarcoEnGrilla)

    return encontroPosicionAdyacente

def recorrerPoscionesDelBarcoYGuardarSiLaPosicionEsAdyacente(barcosEnGrilla:list[BarcoEnGrilla], indiceBarco:int, posicionBarcoEnGrilla:Posición) -> bool:
    """ Dada la lista *barcosEnGrilla* recorre las posiciones segun *indiceBarco* para hayar una posicion adyacente a *posicionBarcoEnGrilla* y sumarla a la lista.
        PRE: 0 <= indiceBarco < len(barcosEnGrilla)
        PRE: esPosiciónVálida(posicionBarcoEnGrilla)
        Args:
            barcosEnGrilla (list[BarcoEnGrilla]): Lista a llenar con las posiciones de los barcos.
            indiceBarco (int): Indica el BarcoEnGrilla a recorrer de *barcosEnGrilla*.
            posicionBarcoEnGrilla (Posición): Posicion a ubicar en *barcosEnGrilla* donde haya una posicion adyacente.
        Returns:
            True si ecuentra una posicion adyacente para *posicionBarcoEnGrilla* dentro de *barcosEnGrilla[indiceBarco]*. False, en caso contrario.
    """
    encontroPosicionAdyacente = False

    for posicion in barcosEnGrilla[indiceBarco]:
        if sonPosicionesAdyecentes(posicion, posicionBarcoEnGrilla):
            barcosEnGrilla[indiceBarco].append(posicionBarcoEnGrilla)
            encontroPosicionAdyacente = True

    return encontroPosicionAdyacente

def agregarPosicionEnBarcosEnGrillaComoNuevaLista(barcosEnGrilla:list[BarcoEnGrilla], posicionBarcoEnGrilla:Posición) -> None:
    """ Agrega una nueva lista a *barcosEnGrilla* con un primer elemento *posicionBarcoEnGrilla*.
        PRE: esPosiciónVálida(posicionBarcoEnGrilla)
        Args:
            barcosEnGrilla (list[BarcoEnGrilla]): Lista a llenar con una nueva lista con *posicionBarcoEnGrilla* como primer elemento.
            posicionBarcoEnGrilla (Posición): Primer elemento de la lista a nueva a agregar en *barcosEnGrilla*.
        Returns:
            None
    """
    barcosEnGrilla.append([posicionBarcoEnGrilla])

def letraDeFilaNro(numero: int) -> str:
    """ Describe la letra correspondiente al número de fila *numero*.
        PRE: 1 <= numero <= 26
        Args:
            numero (int): Numero de la fila a convertir a letra.
    """
    return chr(numero - 1 + ord('A'))

