# 🪢 Juego del Ahorcado en Python

**Desarrollado por:** Elizabeth Lopez  
**Asignatura:** Lógica de Programación

Este proyecto es una implementación en Python del clásico **juego del Ahorcado**, desarrollado como parte de una actividad académica. El juego permite a la usuaria jugar de forma individual, mostrando una interfaz en consola con un menú interactivo y registro de estadísticas.

---

## 🎮 Características principales

- **Menú interactivo** con tres opciones:
  1. Jugar sola  
  2. Ver estadísticas de la última partida  
  3. Salir del juego
- **Selección aleatoria** de una palabra secreta desde una lista predefinida.
- **Representación visual** de la palabra oculta con guiones bajos.
- **Control de letras adivinadas:** no se descuentan intentos al repetir una letra ya ingresada.
- **Posibilidad de adivinar toda la palabra** en cualquier momento.
- **Mensajes personalizados** según el resultado (victoria o derrota).
- **Registro de estadísticas** al finalizar cada partida:
  - Modo de juego  
  - Palabra utilizada  
  - Resultado (Ganó / Perdió)  
  - Intentos restantes

---

## 🧪 Tecnologías utilizadas

- **Lenguaje:** Python 3  
- **Editor de desarrollo:** [Spyder](https://www.spyder-ide.org/)

---

## 📊 Visualización de estadísticas

Tras cada partida, se guarda un resumen automático con los datos mencionados.  
Estas estadísticas pueden consultarse desde el menú principal seleccionando la opción **"Ver estadísticas de la última partida"**.

---

## 🧩 Estructura del programa

1. **Menú principal**  
   El usuario elige una de las tres opciones disponibles.

2. **Preparación del juego**  
   Se inicializa la palabra secreta, el número de intentos, la lista de letras usadas y la visualización parcial.

3. **Bucle del juego**  
   El programa recibe entradas del usuario, actualiza la visualización y evalúa si se gana o se pierde.

4. **Cierre de partida**  
   Se muestra un mensaje final de resultado y se almacenan las estadísticas.

---

## ✅ Requisitos para ejecución

- Tener instalado Python 3
- Ejecutar el archivo `Juego del Ahorcado.py` desde un IDE o consola

---

## Conclusiones

1. **Fortalecimiento de la lógica de programación**  
   Desarrollar el juego del ahorcado permitió reforzar conceptos clave como estructuras de decisión, bucles, listas y diccionarios en Python, consolidando la capacidad de resolver problemas paso a paso.

2. **Importancia de la validación de entradas**  
   La implementación de verificaciones para letras repetidas, intentos y palabras completas demuestra la relevancia de validar correctamente la información que ingresa el usuario, evitando errores y mejorando la experiencia de juego.

3. **Visualización clara de resultados**  
   Integrar un sistema de estadísticas al finalizar la partida brinda al jugador retroalimentación inmediata y fomenta la comprensión de los resultados, lo cual enriquece tanto el aprendizaje como la diversión.
