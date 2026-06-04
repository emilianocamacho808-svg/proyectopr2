import json

class CriaturaDebilitadaError(Exception):
    def __init__(self, mensaje="La criatura está debilitada y no puede continuar."):
        super().__init__(mensaje)

