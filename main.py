# main_poo.py - Script de Prueba Orientada a Objetos
from mini_turtle_oo import Tortuga, iniciar_pantalla, finalizar_dibujo # <--- IMPORTACIÓN MODIFICADA

# 1. Prepara la pantalla antes de crear las tortugas
iniciar_pantalla() 

print("--- Inicio de Prueba Orientada a Objetos ---")

# Creación de dos objetos independientes
t1 = Tortuga()  # Empieza en (0, 0)
t2 = Tortuga(x_inicial=-5) # Empieza en (-100, 0) y será de otro color

# Nota: Puedes configurar t2 con otro color después de crearlo si quieres:
t2.color("blue")

t1.Adelante(5)  # t1 se mueve a (100, 0)
t2.Adelante(10) # t2 se mueve a (100, 0)

print(f"Posición final de T1: {t1.posicion_x}") 
print(f"Posición final de T2: {t2.posicion_x}") 

# 2. Mantiene la ventana abierta
finalizar_dibujo()