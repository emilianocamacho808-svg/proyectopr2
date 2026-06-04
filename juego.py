import pygame
import random
import sys
from boton import Boton
from logica import Criatura, SistemaCombate, CriaturaDebilitadaError
from persistencia import GestorPersistencia

class Juego:
    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Proyecto PR2: Batalla Elemental")
        self.fuente = pygame.font.SysFont("Arial", 18, bold=True) 
        self.sistema_combate = SistemaCombate('tipos.json')
        self.pool = [("maracaibo", "Fuego"), ("rio chama", "Agua"), ("sabila", "Planta"), 
                     ("corpolec", "Electrico"), ("chambeador", "Tierra"), ("conviasa", "Volador")]
        
        self.btn_reiniciar = Boton(150, 250, 150, 50, "Otra Batalla", (150, 255, 150))
        self.btn_guardar = Boton(350, 250, 150, 50, "Guardar Datos", (150, 150, 255))
        self.btn_salir = Boton(550, 250, 150, 50, "Cerrar", (255, 150, 150))
        
        self.historial_ataques = []
        self.reset_batalla()

