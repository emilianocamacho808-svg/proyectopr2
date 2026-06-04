import unittest
from logica import Criatura, SistemaCombate, CriaturaDebilitadaError

class TestSistemaBatalla(unittest.TestCase):
    def setUp(self):
        # Se ejecuta antes de cada prueba
        self.criatura_fuego = Criatura("Ignis", "Fuego", 100, ["Llamarada"])
        self.criatura_planta = Criatura("Planteo", "Planta", 100, ["Latigazo"])
        self.sistema = SistemaCombate('tipos.json')

    def test_encapsulamiento_hp(self):
        """Prueba que la propiedad setter de HP limite los valores correctamente."""
        self.criatura_fuego.hp_actual = -50
        self.assertEqual(self.criatura_fuego.hp_actual, 0)
        
        self.criatura_fuego.hp_actual = 500
        self.assertEqual(self.criatura_fuego.hp_actual, 100)

