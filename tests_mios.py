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
        
        estado = ((3,3), [2], [UNO], (grillaUNO_local, grillaUNO_oponente), (grillaDOS_local, grillaDOS_oponente))

        self.assertFalse(esEstadoDeJuegoVálido(estado))
        self.assertEqual(estado, ((3,3), [2], [UNO], (grillaUNO_local, grillaUNO_oponente), (grillaDOS_local, grillaDOS_oponente)))
    
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

    def test_cero_barcos_disponibles(self):
        grillaUNO_local = [[VACÍO, VACÍO],
                           [VACÍO, VACÍO]]
        
        grillaUNO_oponente = [[VACÍO, VACÍO],
                              [VACÍO, VACÍO]]
        
        grillaDOS_local = [[VACÍO, VACÍO],
                           [VACÍO, VACÍO]]
        
        grillaDOS_oponente = [[VACÍO, VACÍO],
                              [VACÍO, VACÍO]]
        
        estado = ((3,3), [], [UNO], (grillaUNO_local, grillaUNO_oponente), (grillaDOS_local, grillaDOS_oponente))

        self.assertFalse(esEstadoDeJuegoVálido(estado))
        self.assertEqual(estado, ((3,3), [], [UNO], (grillaUNO_local, grillaUNO_oponente), (grillaDOS_local, grillaDOS_oponente)))

    def test_grillas_tienen_menos_de_1_fila(self):
        grillaUNO_local = [[]]

        grillaUNO_oponente = [[]]

        grillaDOS_local = [[]]
        
        grillaDOS_oponente = [[]]

        estado = ((0,0), [], [UNO], (grillaUNO_local, grillaUNO_oponente), (grillaDOS_local, grillaDOS_oponente))

        self.assertFalse(esEstadoDeJuegoVálido(estado))
        self.assertEqual(estado, ((0,0), [], [UNO], (grillaUNO_local, grillaUNO_oponente), (grillaDOS_local, grillaDOS_oponente)))

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

class mismosElementos_Test(unittest.TestCase):
    def test_mismosElementos_lista2_tiene_extra(self):

        lista1 = [2]
        lista2 = [2, 3]

        self.assertFalse(mismosElementos(lista1, lista2))

class seReflejanLosAtaquesCorrectamente_Test(unittest.TestCase):

    def test_se_reflejan_correctamente_devuelve_false(self):
        grilla1 = [[VACÍO, AGUA],
            [VACÍO, VACÍO]]
        
        grilla2 = [[VACÍO, BARCO],
                   [VACÍO, VACÍO]]
        
        self.assertFalse(seReflejanLosAtaquesCorrectamente(grilla1, grilla2))

    def test_se_reflejan_correctamente_devuelve_true(self):
        grilla1 = [[VACÍO, AGUA],
            [VACÍO, BARCO]]
        
        grilla2 = [[VACÍO, AGUA],
            [VACÍO, BARCO]]
        
        self.assertTrue(seReflejanLosAtaquesCorrectamente(grilla1, grilla2))

if __name__ == '__main__':
    unittest.main(verbosity=1)