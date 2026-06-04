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

    def test_efectividad_tipos(self):
        """Prueba el cálculo de daño con multiplicadores."""
        # Fuego contra Planta = x2.0
        mult = self.sistema.calcular_multiplicador("Fuego", "Planta")
        self.assertEqual(mult, 2.0)

    def test_excepcion_personalizada(self):
        """Prueba que el sistema levante la excepción si una criatura está debilitada."""
        self.criatura_fuego.hp_actual = 0
        with self.assertRaises(CriaturaDebilitadaError):
            self.sistema.ejecutar_ataque(self.criatura_fuego, self.criatura_planta)

    def test_metodo_especial_str(self):
        """Prueba el dunder method __str__."""
        representacion = str(self.criatura_fuego)
        self.assertEqual(representacion, "Ignis (Fuego) - HP: 100/100")

if __name__ == '__main__':
    unittest.main()