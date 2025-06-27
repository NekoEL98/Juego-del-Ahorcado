# Juego del Ahorcado
Realización del Juego del Ahorcado en Python

Desarrollado por:
Elizabeth Lopez

Este proyecto consiste en el desarrollo del clásico juego del ahorcado, implementado en Python como parte de la asignatura de Lógica de Programación.
El juego permite al usuario jugar de forma individual adivinando una palabra secreta, con opciones adicionales como visualizar estadísticas de la última partida.

Características principales
Menú interactivo con tres opciones:
  Jugar sola
  Ver estadísticas de la última partida
  Salir del juego

Selección aleatoria de una palabra de una lista predefinida
Representación visual de la palabra oculta con guiones bajos
Control de letras ya adivinadas (sin restar intentos si se repiten)
Oportunidad de adivinar toda la palabra
Mensajes personalizados de victoria o derrota
Registro de estadísticas: modo, palabra, resultado e intentos restantes

Tecnologías utilizadas
  Python 3
  Editor: Spyder

Estadísticas
Al finalizar cada partida, se guarda un resumen con:
  Modo de juego
  Palabra utilizada
  Resultado (Ganó / Perdió)
  Intentos restantes
Estas estadísticas pueden visualizarse desde el menú principal en la opción 2.

Estructura del programa
  Menú principal
  El usuario elige entre jugar, ver estadísticas o salir.
  Preparación del juego
  Se inicializa todo lo necesario para empezar (palabra, intentos, letras, pantalla).
  Bucle del juego
  Se evalúan las entradas del usuario hasta ganar o perder.
  Cierre
  Se muestran mensajes de resultado y se registran estadísticas.
