# 🚢 Team Challenge: Hundir la Flota (Battleship)
Este proyecto es una versión del clásico juego **Hundir la Flota** desarrollada en Python para el Bootcamp de Data Science de **The Bridge**.

## 🛠️ Tecnologías y Metodología
* **Lenguaje:** Python 3.x (NumPy, Random)
* **Gestión:** Metodología Agile / Scrum
* **Control de Versiones:** Git & GitHub

## 📂 Estructura del Proyecto
* `main.py`: Punto de entrada y bucle de juego.
* `clases.py`: Lógica del tablero (Clase `board`).
* `funciones.py`: Lógica de disparos y colocación.
* `variable.py`: Configuración, diccionarios de barcos y mapeo de coordenadas.

## 📐 Lógica de Coordenadas
Para facilitar la visualización, el tablero es de **11x11**:
* **Índice 0:** Reservado para etiquetas (A-J y 1-10).
* **Índices 1-10:** Espacio real de juego donde se sitúan los barcos.
* *Nota:* El mapeo en `variable.py` está configurado en **base 1** para coincidir con esta estructura.

## 👥 Equipo de Desarrollo
Este proyecto ha sido desarrollado de manera colaborativa por:
* Ana Belén Balmaseda Afqir
* Dani García Ordiales
* Inés Goetsch
* Pablo Hernández
