import pygame

class Boton:
    def __init__(self, x, y, ancho, alto, texto, color):
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.texto = texto
        self.color = color

    def dibujar(self, pantalla, fuente):
        pygame.draw.rect(pantalla, self.color, self.rect)
        pygame.draw.rect(pantalla, (0, 0, 0), self.rect, 2)
        txt = fuente.render(self.texto, True, (0, 0, 0))
        pantalla.blit(txt, (self.rect.x + 10, self.rect.y + 10))

    def es_clickeado(self, pos):
        return self.rect.collidepoint(pos)