# main_poo.py - Script de prueba para Versión POO
from mini_turtle_oo import Tortuga

print("--- Inicio de Prueba Orientada a Objetos ---")

# Creación de dos objetos independientes
t1 = Tortuga() 
t2 = Tortuga() 

t1.adelante(5)
t2.adelante(10)

print(f"Posición final de T1: {t1.posicion_x}") # Debe ser 5
print(f"Posición final de T2: {t2.posicion_x}") # Debe ser 10