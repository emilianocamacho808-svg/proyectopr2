import json
import csv
from logica import Criatura

class GestorPersistencia:
    @staticmethod
    def guardar_estado_json(jugador, enemigo, archivo="partida.json"):
        estado = {
            "jugador": jugador.to_dict(),
            "enemigo": enemigo.to_dict()
        }
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(estado, f, indent=4, ensure_ascii=False)

    @staticmethod
    def cargar_estado_json(archivo="partida.json"):
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                estado = json.load(f)
            jugador = Criatura.from_dict(estado["jugador"])
            enemigo = Criatura.from_dict(estado["enemigo"])
            return jugador, enemigo
        except FileNotFoundError:
            return None, None
