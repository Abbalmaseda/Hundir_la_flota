


#### 🚢 Hundir la Flota | Battleship Game

> **Selecciona tu idioma / Select your language:**
> 
> [🇪🇸 Leer en Español](#español) | [🇺🇸 Read in English](#english)

---

<a name="español"></a>

## 🇪🇸 Descripción en Español


### 🚢 Team Challenge: Hundir la Flota (Battleship)

Este proyecto implementa una versión digital del clásico juego **Hundir la Flota**, desarrollado en Python como parte del **Bootcamp de Data Science de The Bridge**.

El objetivo es simular un entorno de juego completo por turnos, aplicando principios de programación estructurada, diseño modular y metodología Agile.

---

### 🎮 Descripción del Sistema
El sistema reproduce una partida entre un usuario y una IA con comportamiento aleatoria. El flujo gestiona impactos, fallos y condiciones de victoria actualizando matrices en tiempo real.

### 🌍 Internacionalización (i18n)
El juego permite seleccionar el idioma al inicio:
* ES **Español**
* 🇺🇸 **English**

---

### 🧠 Lógica y Stack Tecnológico
El proyecto se apoya en herramientas fundamentales del ecosistema de Data Science:

* **Lenguaje:** Python 3.x
* **Librerías:** * `NumPy`: Gestión de tableros mediante matrices bidimensionales.
    * `Random`: Lógica de posicionamiento y disparos aleatorios.
* **Metodología:** Agile / Scrum con control de versiones en Git & GitHub.

---

### 📐 Arquitectura del Proyecto
El código sigue una estructura modular para facilitar el mantenimiento y la escalabilidad:

| Archivo | Responsabilidad |
| :--- | :--- |
| `main.py` | Orquestación del flujo y bucle principal del juego. |
| `clases.py` | Abstracción del tablero mediante POO (Clases `Board` y `Ships`). |
| `funciones.py` | Lógica de negocio (disparos, colocación y validaciones). |
| `variables.py` | Configuración global, diccionarios y coordenadas. |

---

### 👥 Equipo de Desarrollo
El éxito de este proyecto se basa en la colaboración distribuida y roles definidos:

* **Ana Belén Balmaseda** — *Scrum Master * 
(`variables.py`)
    * Coordinación de equipo, gestión de backlog y definicion de los parámetros, símbolos y textos para garantizar un código organizado, escalable y bilingüe
* **Dani García** — *Dev 1* (`clases.py`)
    * Diseño de la capa de objetos y estado del tablero.
* **Inés Goetsch** — *Dev 2* (`funciones.py`)
    * Mecánicas de juego y validación de lógica funcional.
* **Pablo Hernández** — *Dev 3* (`main.py`)
    * Ciclo de vida de la partida y flujo principal.
* **Maksym Chaika** — *Soporte Tecnico*
    * Optimización de código y resolución de incidencias.

---

### 🚀 Instalación y ejecución
Clona el repositorio:
git clone https://github.com/tu-usuario/Hundir_la_flota.git

Entra en el directorio:
cd Hundir_la_flota

Instala dependencias (si aplica):
pip install -r requirements.txt

Ejecuta el juego:
python main.py


**📅 Fecha:** Abril/ 2026  
**📍 Ubicación:** España 



<p align="center">
  <img src="image-2.png" width="300" alt="Battleship Team Challenge Logo">
</p>


 -----------------------------------------



<a name="english"></a>

## 🇺🇸 English Version

### 🚢 Team Challenge: Battleship (Hundir la Flota)

This project implements a digital version of the classic game Battleship, developed in Python as part of the Data Science Bootcamp at The Bridge.

The goal is to simulate a full turn-based game environment, applying structured programming principles, modular design, and Agile methodology.

### 🎮 System Description

The system simulates a match between a user and an AI with random behavior.
The flow handles hits, misses, and win conditions while updating boards in real time.

### 🌍 Internationalization (i18n)

The game allows language selection at the start:

ES Spanish
EN English

### 🧠 Logic and Tech Stack

The project is based on key tools from the Data Science ecosystem:

Language: Python 3.x
Libraries:
NumPy: management of boards using 2D matrices
Random: ship placement and random shooting logic
Methodology: Agile / Scrum with Git & GitHub version control

### 📐 Project Architecture

The code follows a modular structure to improve maintainability and scalability:

File	Responsibility
main.py	Game flow orchestration and main loop
clases.py	Board abstraction using OOP (classes Board and Ships)
funciones.py	Game logic (shooting, placement and validations)
variables.py	Global configuration, dictionaries and coordinates

### 👥 Development Team

This project is based on distributed collaboration with clearly defined roles:

Ana Belén Balmaseda — Scrum Master
(variables.py)
Team coordination, backlog management and global configuration.
Dani García — Dev 1 (clases.py)
Object layer design and board state management.
Inés Goetsch — Dev 2 (funciones.py)
Game mechanics and logic validation.
Pablo Hernández — Dev 3 (main.py)
Game lifecycle and main flow.
Maksym Chaika — Technical Support
Code optimization and issue resolution.

### 🚀 Installation and execution

Clone the repository:

git clone https://github.com/tu-usuario/Hundir_la_flota.git

Go to the project directory:
cd Hundir_la_flota

Install dependencies (if needed):
pip install -r requirements.txt

Run the game:
python main.py





**📅 Date:** April/ 2026  
**📍 Location:** Spain


<p align="center">
  <img src="image-2.png" width="300" alt="Battleship Team Challenge Logo">
</p>