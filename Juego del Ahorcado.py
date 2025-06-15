# -*- coding: utf-8 -*-
"""
Created on Fri Jun 13 23:40:22 2025

@author: Eli
"""

import random

# Lista de palabras posibles para jugar. Se puede ir agregando más palabras si se desea.
palabras = ["zanahoria", "conejo", "gato", "alice", "perrito", "cookie", "perlita", "bts", "army"]

# Función que elige una palabra aleatoria de la lista
def elegir_palabra():
    return random.choice(palabras).lower()  # Devuelve una palabra en minúsculas

# Función principal del juego del ahorcado
def jugar_ahorcado():
    palabra = elegir_palabra()  # Selecciona la palabra secreta
    letras_adivinadas = []      # Lista para almacenar las letras que el usuario ya intentó
    intentos = 6                # Número máximo de intentos que tiene el jugador
    mostrar = ["_" for _ in palabra]  # Lista que muestra el progreso con guiones bajos
    
    # Ciclo principal del juego
    while intentos > 0 and "_" in mostrar:
        print("\nPalabra:", " ".join(mostrar))  # Muestra la palabra oculta con los guiones
        print("Letras adivinadas:", ", ".join(letras_adivinadas))  # Muestra las letras usadas
        print(f"Intentos restantes: {intentos}")  # Muestra los intentos disponibles
        
        # Pedimos al usuario que ingrese una letra o intente adivinar toda la palabra
        intento = input("Ingresa una letra o la palabra completa: ").lower()
        
        # Si el usuario ingresa una sola letra
        if len(intento) == 1:
           if intento in letras_adivinadas:
               print("Ya intentaste esa letra.")  # Si ya la usó, lo avisamos
           elif intento in palabra:
               print("¡Bien! La letra está en la palabra.")
               letras_adivinadas.append(intento)  # Guardamos la letra correcta
                
               # Recorremos la palabra para mostrar la letra en todas sus posiciones
               for i, letra in enumerate(palabra):
                    if letra == intento:
                        mostrar[i] = intento
           else:
               print("La letra no está en la palabra.")
               letras_adivinadas.append(intento)  # Guardamos la letra incorrecta
               intentos -= 1                      # Perdemos un intento
        # Si el usuario intenta adivinar toda la palabra
        elif intento == palabra:
            mostrar = list(palabra)  # Si acierta, mostramos toda la palabra
            break
        else:
            print("Palabra incorrecta.")
            intentos -= 1  # Si falla la palabra completa, pierde un intento
    # Evaluamos si el jugador ganó o perdió
    if "_" not in mostrar:
        print(f"\n ¡Felicidades ganaste! Adivinaste la palabra: {palabra}")
    else:
        print(f"\n Te quedaste sin intentos¡Perdiste¡. La palabra era: {palabra}")
        
# Función que muestra el menú principal del juego
def menu():
    while True:
        print("\n--- MENÚ DEL AHORCADO ---")
        print("1. Jugar")
        print("2. Salir")
        opcion = input("Selecciona una opción (1 o 2): ")

        # Si se elige jugar, iniciamos el juego
        if opcion == "1":
            jugar_ahorcado()
        # Si elige salir, mostramos un mensaje de despedida
        elif opcion == "2":
            print("¡Gracias por jugar, Eli! 🐰🎀")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

# Llamamos al menú si el archivo se ejecuta directamente
if __name__ == "__main__":
    menu()