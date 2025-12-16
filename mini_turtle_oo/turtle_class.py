# turtle_class.py - Clase Tortuga
class Tortuga:
    def __init__(self, x_inicial=0):
        self.posicion_x = x_inicial
        print(f"DEBUG - Nueva Tortuga creada en X={self.posicion_x}")

    def adelante(self, pasos):
        self.posicion_x += pasos
        print(f"DEBUG - Tortuga en: {self.posicion_x}")

    def reiniciar(self):
        self.posicion_x = 0
        print("DEBUG - Posición X reseteada a 0.")