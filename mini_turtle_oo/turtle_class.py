import turtle

# 1. Definición de la Clase: Hacemos que Tortuga herede de turtle.Turtle
# Esto significa que Tortuga ya sabe dibujar y moverse.
class Tortuga(turtle.Turtle): 
    
    # Esta variable es solo para fines de depuración/prueba, la clase padre ya maneja la posición.
    # self.posicion_x se usa en main_poo.py para la prueba, así que la mantenemos.
    
    def __init__(self, x_inicial=0):
        # 1.1. Inicializar la clase padre (turtle.Turtle)
        super().__init__()
        
        # 1.2. Configuración estética de la tortuga
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto(x_inicial * 20, 0) # Posiciona la tortuga en el gráfico (multiplicamos por 20)
        self.pendown()

        # 1.3. Mantenemos la variable de prueba para que main_poo.py no falle
        self.posicion_x = x_inicial
        print(f"DEBUG - Nueva Tortuga creada en X={self.posicion_x}")

    # 2. Modificación del método Adelante
    def Adelante(self, pasos): # Nota: El main_poo usa 'Adelante' con mayúscula
        self.forward(pasos * 20) # Usamos el método real de la clase padre
        self.posicion_x += pasos # Actualizamos la variable de prueba
        print(f"DEBUG - Tortuga en: {self.posicion_x}")
        
    # 3. Modificación del método Reiniciar
    def reiniciar(self):
        self.clear() # Borra el dibujo
        self.penup()
        self.home()  # Mueve la tortuga a (0, 0)
        self.pendown()
        self.posicion_x = 0 # Reiniciamos la variable de prueba
        print("DEBUG - Posición X reseteada a 0.")

# 4. Función para inicializar y mantener la pantalla (se llama una sola vez)
def iniciar_pantalla():
    # Inicializa la pantalla
    screen = turtle.Screen()
    screen.setup(width=600, height=400) # Configuración de tamaño
    screen.title("Python Turtle Graphics - Proyecto POO")
    
def finalizar_dibujo():
    turtle.done()