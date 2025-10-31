import unittest
from batallaNaval import *
from interfaz_batalla_naval import *

class cantidadDeBarcosDeTamaño_Test(unittest.TestCase):
    def test_cero_barcos_de_tamaño(self):
        barcos = [[('J',3), ('J',4), ('J',5)],
                  [('K',7), ('L',7)],
                  [('H',2), ('H',3), ('H',4)]]       
        self.assertEqual(cantidadDeBarcosDeTamaño(barcos,4),0)
        self.assertEqual(barcos, [[('J',3), ('J',4), ('J',5)],
                                  [('K',7), ('L',7)],
                                  [('H',2), ('H',3), ('H',4)]])
    
    def test_hay_dos_barcos_en_costados(self):
        barcos = [[('A',1), ('A',2), ('A',3)],
                  [('C',5), ('C',6)],
                  [('F',7), ('G',7)],
                  [('H',1), ('H',2), ('H',3)]]
        self.assertEqual(cantidadDeBarcosDeTamaño(barcos,3),2)
        self.assertEqual(barcos, [[('A',1), ('A',2), ('A',3)],
                                  [('C',5), ('C',6)],
                                  [('F',7), ('G',7)],
                                  [('H',1), ('H',2), ('H',3)]])

class nuevoJuego_Test(unittest.TestCase):
    def test_5x5_y_tres_barcos(self):
        grilla_uno_local = [[VACÍO,VACÍO,VACÍO,VACÍO,VACÍO],
                            [VACÍO,VACÍO,VACÍO,VACÍO,VACÍO], 
                            [VACÍO,VACÍO,VACÍO,VACÍO,VACÍO], 
                            [VACÍO,VACÍO,VACÍO,VACÍO,VACÍO], 
                            [VACÍO,VACÍO,VACÍO,VACÍO,VACÍO]]
        
        grilla_uno_oponente = [[VACÍO,VACÍO,VACÍO,VACÍO,VACÍO],
                               [VACÍO,VACÍO,VACÍO,VACÍO,VACÍO], 
                               [VACÍO,VACÍO,VACÍO,VACÍO,VACÍO], 
                               [VACÍO,VACÍO,VACÍO,VACÍO,VACÍO], 
                               [VACÍO,VACÍO,VACÍO,VACÍO,VACÍO]]
        
        grilla_dos_local = [[VACÍO,VACÍO,VACÍO,VACÍO,VACÍO],
                            [VACÍO,VACÍO,VACÍO,VACÍO,VACÍO], 
                            [VACÍO,VACÍO,VACÍO,VACÍO,VACÍO], 
                            [VACÍO,VACÍO,VACÍO,VACÍO,VACÍO], 
                            [VACÍO,VACÍO,VACÍO,VACÍO,VACÍO]]
        
        grilla_dos_oponente = [[VACÍO,VACÍO,VACÍO,VACÍO,VACÍO],
                               [VACÍO,VACÍO,VACÍO,VACÍO,VACÍO], 
                               [VACÍO,VACÍO,VACÍO,VACÍO,VACÍO], 
                               [VACÍO,VACÍO,VACÍO,VACÍO,VACÍO], 
                               [VACÍO,VACÍO,VACÍO,VACÍO,VACÍO]]
        
        juego = nuevoJuego(5,5,[2,3,4])
        self.assertEqual(juego[0], (5,5))
        self.assertEqual(juego[1], [2,3,4])
        self.assertEqual(juego[2], "UNO")
        self.assertEqual(juego[3], (grilla_uno_local, grilla_uno_oponente))
        self.assertEqual(juego[4], (grilla_dos_local, grilla_dos_oponente))

class esEstadoDeJuegoValido_Test(unittest.TestCase):
        
    def test_grillas_tienen_menos_de_1_fila(self):
        grillaUNO_local = []

        grillaUNO_oponente = []

        grillaDOS_local = []
        
        grillaDOS_oponente = []

        estado = ((0,0), [], [UNO], (grillaUNO_local, grillaUNO_oponente), (grillaDOS_local, grillaDOS_oponente))

        self.assertFalse(esEstadoDeJuegoVálido(estado))
        self.assertEqual(estado, ((0,0), [], [UNO], (grillaUNO_local, grillaUNO_oponente), (grillaDOS_local, grillaDOS_oponente)))
    
    def test_grillas_tienen_menos_de_1_columna(self):
        grillaUNO_local = [[]]

        grillaUNO_oponente = [[]]

        grillaDOS_local = [[]]
        
        grillaDOS_oponente = [[]]

        estado = ((0,0), [], [UNO], (grillaUNO_local, grillaUNO_oponente), (grillaDOS_local, grillaDOS_oponente))

        self.assertFalse(esEstadoDeJuegoVálido(estado))
        self.assertEqual(estado, ((0,0), [], [UNO], (grillaUNO_local, grillaUNO_oponente), (grillaDOS_local, grillaDOS_oponente)))
    
    def test_cero_barcos_disponibles(self):
        grillaUNO_local = [[VACÍO, VACÍO],
                           [VACÍO, VACÍO]]
        
        grillaUNO_oponente = [[VACÍO, VACÍO],
                              [VACÍO, VACÍO]]
        
        grillaDOS_local = [[VACÍO, VACÍO],
                           [VACÍO, VACÍO]]
        
        grillaDOS_oponente = [[VACÍO, VACÍO],
                              [VACÍO, VACÍO]]
        
        estado = ((2,2), [], [UNO], (grillaUNO_local, grillaUNO_oponente), (grillaDOS_local, grillaDOS_oponente))

        self.assertFalse(esEstadoDeJuegoVálido(estado))
        self.assertEqual(estado, ((2,2), [], [UNO], (grillaUNO_local, grillaUNO_oponente), (grillaDOS_local, grillaDOS_oponente)))

    def test_tablero_jugadorUNO_tiene_dim_dif_a_las_de_estado(self):
        grillaUNO_local = [[BARCO, BARCO],
                           [VACÍO, VACÍO],
                           [VACÍO, VACÍO]]
        
        grillaUNO_oponente = [[VACÍO, VACÍO],
                              [VACÍO, VACÍO],
                              [VACÍO, VACÍO]]
        
        grillaDOS_local = [[BARCO, VACÍO],
                           [BARCO, VACÍO]]
        
        grillaDOS_oponente = [[VACÍO, VACÍO],
                              [VACÍO, VACÍO]]
        
        estado = ((2,2), [2], [UNO], (grillaUNO_local, grillaUNO_oponente), (grillaDOS_local, grillaDOS_oponente))

        self.assertFalse(esEstadoDeJuegoVálido(estado))
        self.assertEqual(estado, ((2,2), [2], [UNO], (grillaUNO_local, grillaUNO_oponente), (grillaDOS_local, grillaDOS_oponente)))

    def test_tablero_jugadorDOS_tiene_dim_dif_a_las_de_estado(self):
        grillaUNO_local = [[BARCO, BARCO],
                           [VACÍO, VACÍO],
                           [VACÍO, VACÍO]]
        
        grillaUNO_oponente = [[VACÍO, VACÍO],
                              [VACÍO, VACÍO],
                              [VACÍO, VACÍO]]
        
        grillaDOS_local = [[BARCO, VACÍO],
                           [BARCO, VACÍO]]
        
        grillaDOS_oponente = [[VACÍO, VACÍO],
                              [VACÍO, VACÍO]]
        
        estado = ((3,3), [2], [DOS], (grillaUNO_local, grillaUNO_oponente), (grillaDOS_local, grillaDOS_oponente))

        self.assertFalse(esEstadoDeJuegoVálido(estado))
        self.assertEqual(estado, ((3,3), [2], [DOS], (grillaUNO_local, grillaUNO_oponente), (grillaDOS_local, grillaDOS_oponente)))
    
    def test_grillaUNOlocal_no_coinciden_con_los_disponibles(self):
        grillaUNO_local = [[VACÍO, BARCO],
                           [VACÍO, BARCO],
                           [VACÍO, BARCO]]
        
        grillaUNO_oponente = [[VACÍO, VACÍO],
                              [VACÍO, VACÍO],
                              [VACÍO, VACÍO]]
        
        grillaDOS_local = [[VACÍO, VACÍO],
                           [BARCO, VACÍO],
                           [BARCO, VACÍO]]
        
        grillaDOS_oponente = [[VACÍO, VACÍO],
                              [VACÍO, VACÍO],
                              [VACÍO, VACÍO]]
        
        estado = ((3,3), [2], [UNO], (grillaUNO_local, grillaUNO_oponente), (grillaDOS_local, grillaDOS_oponente))

        self.assertFalse(esEstadoDeJuegoVálido(estado))
        self.assertEqual(estado, ((3,3), [2], [UNO], (grillaUNO_local, grillaUNO_oponente), (grillaDOS_local, grillaDOS_oponente)))

    def test_barcos_grillaDOSlocal_no_coinciden_con_los_disponibles(self):
        grillaUNO_local = [[BARCO, BARCO],
                           [VACÍO, VACÍO],
                           [VACÍO, VACÍO]]
        
        grillaUNO_oponente = [[VACÍO, VACÍO],
                              [VACÍO, VACÍO],
                              [VACÍO, VACÍO]]
        
        grillaDOS_local = [[BARCO, VACÍO],
                           [BARCO, VACÍO],
                           [BARCO, VACÍO]]
        
        grillaDOS_oponente = [[VACÍO, VACÍO],
                              [VACÍO, VACÍO],
                              [VACÍO, VACÍO]]
        
        estado = ((3,3), [2], [DOS], (grillaUNO_local, grillaUNO_oponente), (grillaDOS_local, grillaDOS_oponente))

        self.assertFalse(esEstadoDeJuegoVálido(estado))
        self.assertEqual(estado, ((3,3), [2], [DOS], (grillaUNO_local, grillaUNO_oponente), (grillaDOS_local, grillaDOS_oponente)))

    def test_es_estado_de_juego_valido_UNO(self):
        grillaUNO_local = [[BARCO, VACÍO],
                           [BARCO, VACÍO]]
        
        grillaUNO_oponente = [[VACÍO, VACÍO],
                              [VACÍO, VACÍO]]
        
        grillaDOS_local = [[VACÍO, BARCO],
                           [VACÍO, BARCO]]
        
        grillaDOS_oponente = [[VACÍO, VACÍO],
                              [VACÍO, VACÍO]]
        
        estado = ((2,2), [2], [UNO], (grillaUNO_local, grillaUNO_oponente), (grillaDOS_local, grillaDOS_oponente))

        self.assertTrue(esEstadoDeJuegoVálido(estado))
        self.assertEqual(estado, ((2,2), [2], [UNO], (grillaUNO_local, grillaUNO_oponente), (grillaDOS_local, grillaDOS_oponente)))

    def test_es_estado_de_juego_valido_DOS(self):
        grillaUNO_local = [[BARCO, VACÍO],
                           [BARCO, VACÍO]]
        
        grillaUNO_oponente = [[VACÍO, VACÍO],
                              [VACÍO, VACÍO]]
        
        grillaDOS_local = [[VACÍO, BARCO],
                           [VACÍO, BARCO]]
        
        grillaDOS_oponente = [[VACÍO, VACÍO],
                              [VACÍO, VACÍO]]
        
        estado = ((2,2), [2], [DOS], (grillaUNO_local, grillaUNO_oponente), (grillaDOS_local, grillaDOS_oponente))

        self.assertTrue(esEstadoDeJuegoVálido(estado))
        self.assertEqual(estado, ((2,2), [2], [DOS], (grillaUNO_local, grillaUNO_oponente), (grillaDOS_local, grillaDOS_oponente)))

    def test_barcos_disponibles_tienen_mas_que_los_en_grillaUNOlocal(self):
        grillaUNO_local = [[BARCO, VACÍO],
                           [BARCO, VACÍO]]
    
        grillaUNO_oponente = [[VACÍO, VACÍO],
                              [VACÍO, VACÍO]]
    
        grillaDOS_local = [[VACÍO, BARCO],
                           [VACÍO, BARCO]]
    
        grillaDOS_oponente = [[VACÍO, VACÍO],
                              [VACÍO, VACÍO]]
        
        estado = ((2,2), [2,3], [UNO], 
              (grillaUNO_local, grillaUNO_oponente), 
              (grillaDOS_local, grillaDOS_oponente))

        self.assertFalse(esEstadoDeJuegoVálido(estado))
        self.assertEqual(estado, ((2,2), [2,3], [UNO], 
                              (grillaUNO_local, grillaUNO_oponente), 
                              (grillaDOS_local, grillaDOS_oponente)))
    
class coincidenPosAtacadas_Test(unittest.TestCase):
    def test_coinciden_las_pos_atacadas(self):
        tablero1 = ([[BARCO, BARCO],
                     [VACÍO, VACÍO],
                     [VACÍO, VACÍO]],

                     [[VACÍO, BARCO],
                      [VACÍO, BARCO],
                      [VACÍO, VACÍO]])
        
        tablero2 = ([[VACÍO, BARCO],
                     [VACÍO, BARCO],
                     [VACÍO, VACÍO]],

                     [[BARCO, BARCO],
                      [VACÍO, VACÍO],
                      [VACÍO, VACÍO]])
    
        self.assertTrue(coincidenPosicionesAtacadas(tablero1, tablero2))

    def test_no_coinciden_las_pos_atacadas(self):
        tablero1 = ([[BARCO, BARCO],
                     [VACÍO, VACÍO],
                     [VACÍO, VACÍO]],

                     [[VACÍO, BARCO],
                      [VACÍO, AGUA],
                      [VACÍO, VACÍO]])
        
        tablero2 = ([[VACÍO, BARCO],
                     [VACÍO, BARCO],
                     [VACÍO, VACÍO]],

                     [[BARCO, AGUA],
                      [VACÍO, VACÍO],
                      [VACÍO, VACÍO]])
    
        self.assertFalse(coincidenPosicionesAtacadas(tablero1,tablero2))

    def test_false_turnos_incoherentes(self):
        tablero1 = ([[BARCO, BARCO],
                     [VACÍO, VACÍO],
                     [VACÍO, VACÍO]],

                     [[VACÍO, AGUA],
                      [VACÍO, BARCO],
                      [VACÍO, BARCO]])

        tablero2 = ([[BARCO, BARCO],
                     [VACÍO, VACÍO],
                     [VACÍO, VACÍO]],

                     [[VACÍO, AGUA],
                      [VACÍO, VACÍO],
                      [VACÍO, VACÍO]])
        
        self.assertNotEqual(turnos(grillaOponente(tablero1)), turnos(grillaOponente(tablero2)))
    
    def test_true_turnos_coherentes(self):
        tablero1 = ([[BARCO, BARCO],
                     [VACÍO, VACÍO],
                     [VACÍO, VACÍO]],

                     [[BARCO, VACÍO],
                      [VACÍO, AGUA],
                      [VACÍO, AGUA]])

        tablero2 = ([[BARCO, BARCO],
                     [VACÍO, VACÍO],
                     [VACÍO, VACÍO]],

                     [[VACÍO, BARCO],
                      [VACÍO, AGUA],
                      [VACÍO, AGUA]])
        
        self.assertEqual(turnos(grillaOponente(tablero1)), turnos(grillaOponente(tablero2)))

    def test_true_turnos_coherentes_un_turno_de_diferencia_es_true(self):
        """Este es para el caso específico en el que se pasa por la parte de la función que cumple que seReflejanCorrectamente para los
        dos tableros, y aun falta que uno de los jugadores juegue, es decir, se debe tolerar un turno de diferencia"""
        tablero1 = ([[BARCO, BARCO],
                     [VACÍO, VACÍO],
                     [VACÍO, VACÍO]],
                    [[VACÍO, BARCO],
                     [VACÍO, VACÍO],
                     [VACÍO, VACÍO]])
        
        tablero2 = ([[BARCO, BARCO],
                     [VACÍO, VACÍO],
                     [VACÍO, VACÍO]],   
                    [[BARCO, VACÍO],
                     [VACÍO, VACÍO],
                     [VACÍO, VACÍO]])

        self.assertTrue(coincidenPosicionesAtacadas(tablero1, tablero2))


class mismosElementos_Test(unittest.TestCase):
    def test_mismosElementos_lista2_tiene_extra(self):

        lista1 = [2]
        lista2 = [2, 3]

        self.assertFalse(mismosElementos(lista1, lista2))
    
if __name__ == '__main__':
    unittest.main(verbosity=1)