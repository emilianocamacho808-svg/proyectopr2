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

class Criatura(EntidadBasica, ElementoClimaticoMixin):
    def __init__(self, nombre, tipo, hp_max, ataques):
        super().__init__(nombre)
        self.tipo = tipo
        self._hp_max = hp_max
        self._hp_actual = hp_max
        self.ataques = ataques

    @property
    def hp_actual(self):
        return self._hp_actual
        
    @hp_actual.setter
    def hp_actual(self, valor):
        if valor < 0:
            self._hp_actual = 0
        elif valor > self._hp_max:
            self._hp_actual = self._hp_max
        else:
            self._hp_actual = valor

    def esta_vivo(self):
        return self._hp_actual > 0

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "tipo": self.tipo,
            "hp_max": self._hp_max,
            "hp_actual": self._hp_actual,
            "ataques": self.ataques
        }

    @classmethod
    def from_dict(cls, data):
        criatura = cls(data["nombre"], data["tipo"], data["hp_max"], data["ataques"])
        criatura.hp_actual = data["hp_actual"]
        return criatura

    def __str__(self):
        return f"{self.nombre} ({self.tipo}) - HP: {self._hp_actual}/{self._hp_max}"
    
    def __eq__(self, otra_criatura):
        return self.nombre == otra_criatura.nombre and self.tipo == otra_criatura.tipo

class SistemaCombate:
    def __init__(self, ruta_tipos='tipos.json'):
        with open(ruta_tipos, 'r', encoding='utf-8') as f:
            self.tabla_tipos = json.load(f)

    def calcular_multiplicador(self, tipo_at, tipo_def):
        ventajas = self.tabla_tipos.get(tipo_at, {}).get("fuertes_contra", {})
        debilidades = self.tabla_tipos.get(tipo_at, {}).get("debiles_contra", {})
        if tipo_def in ventajas: return 2.0
        if tipo_def in debilidades: return 0.5
        return 1.0

    def ejecutar_ataque(self, atacante, defensor, poder_base=20):
        if not atacante.esta_vivo() or not defensor.esta_vivo():
            raise CriaturaDebilitadaError(f"No se puede ejecutar el ataque.")
        
        mult = self.calcular_multiplicador(atacante.tipo, defensor.tipo)
        dano_final = int(poder_base * mult)
        defensor.hp_actual -= dano_final 
        return dano_final, mult
        