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

    def reset_batalla(self):
        c1, c2 = random.sample(self.pool, 2)
        ataques_c1 = self.sistema_combate.tabla_tipos[c1[1]]["ataques"]
        ataques_c2 = self.sistema_combate.tabla_tipos[c2[1]]["ataques"]

        self.jugador = Criatura(c1[0], c1[1], 100, ataques_c1)
        self.enemigo = Criatura(c2[0], c2[1], 100, ataques_c2)
        self.mensaje = "¡Batalla iniciada!"
        self.ganador = None
        self.historial_ataques.clear()
        self.botones = [
            Boton(50, 450, 200, 50, self.jugador.ataques[0], (220, 220, 220)),
            Boton(300, 450, 200, 50, self.jugador.ataques[1], (220, 220, 220))
        ]

    def turno_grafico(self, atacante, defensor, nombre_ataque):
        try:
            dano, mult = self.sistema_combate.ejecutar_ataque(atacante, defensor)
            texto = "¡Súper efectivo!" if mult > 1 else "Poco efectivo..." if mult < 1 else ""
            self.historial_ataques.append(["Turno", atacante.nombre, defensor.nombre, dano, mult])
            return f"{atacante.nombre} usó {nombre_ataque}. {texto}"
        except CriaturaDebilitadaError as error:
            return str(error)

    def ejecutar(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if not self.ganador:
                        for btn in self.botones:
                            if btn.es_clickeado(event.pos):
                                self.mensaje = self.turno_grafico(self.jugador, self.enemigo, btn.texto)
                                if self.enemigo.esta_vivo():
                                    atk_e = random.choice(self.enemigo.ataques)
                                    self.mensaje += f" | {self.turno_grafico(self.enemigo, self.jugador, atk_e)}"
                                    if not self.jugador.esta_vivo(): self.ganador = "¡EL RIVAL GANA!"
                                else:
                                    self.ganador = "¡HAS GANADO!"
                    else:
                        if self.btn_reiniciar.es_clickeado(event.pos): self.reset_batalla()
                        elif self.btn_guardar.es_clickeado(event.pos):
                            GestorPersistencia.guardar_estado_json(self.jugador, self.enemigo)
                            GestorPersistencia.exportar_historial_csv(self.historial_ataques)
                        elif self.btn_salir.es_clickeado(event.pos): run = False

            self.pantalla.fill((245, 245, 250))
            
            pygame.display.flip()
        pygame.quit()