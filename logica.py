import json

class CriaturaDebilitadaError(Exception):
    def __init__(self, mensaje="La criatura está debilitada y no puede continuar."):
        super().__init__(mensaje)

class ElementoClimaticoMixin:
    def aplicar_clima(self):
        return "El clima afecta el campo de batalla."

class EntidadBasica:
    def __init__(self, nombre):
        self._nombre = nombre
        
    @property
    def nombre(self):
        return self._nombre

