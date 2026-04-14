![image-2.png]




# 🚢 Team Challenge: Hundir la Flota (Battleship)

Este proyecto implementa una versión digital del clásico juego **Hundir la Flota**, desarrollado en Python como parte del **Bootcamp de Data Science de The Bridge**.

El objetivo es simular un entorno de juego completo por turnos, aplicando principios de programación estructurada, diseño modular y metodología Agile.

---

## 🎮 Descripción del Sistema
El sistema reproduce una partida entre un usuario y una IA con comportamiento heurístico. El flujo gestiona impactos, fallos y condiciones de victoria actualizando matrices en tiempo real.

### 🌍 Internacionalización (i18n)
El juego permite seleccionar el idioma al inicio:
* ES **Español**
* EN **English**

---

## 🧠 Lógica y Stack Tecnológico
El proyecto se apoya en herramientas fundamentales del ecosistema de Data Science:

* **Lenguaje:** Python 3.x
* **Librerías:** * `NumPy`: Gestión de tableros mediante matrices bidimensionales.
    * `Random`: Lógica de posicionamiento y disparos aleatorios.
* **Metodología:** Agile / Scrum con control de versiones en Git & GitHub.

---

## 📐 Arquitectura del Proyecto
El código sigue una estructura modular para facilitar el mantenimiento y la escalabilidad:

| Archivo | Responsabilidad |
| :--- | :--- |
| `main.py` | Orquestación del flujo y bucle principal del juego. |
| `clases.py` | Abstracción del tablero mediante POO (Clases `Board` y `Ships`). |
| `funciones.py` | Lógica de negocio (disparos, colocación y validaciones). |
| `variables.py` | Configuración global, diccionarios y coordenadas. |

---

## 👥 Equipo de Desarrollo
El éxito de este proyecto se basa en la colaboración distribuida y roles definidos:

* **Ana Belén Balmaseda** — *Scrum Master * 
(`variables.py`)
    * Coordinación de equipo, gestión de backlog y configuración global.
* **Dani García** — *Dev 1* (`clases.py`)
    * Diseño de la capa de objetos y estado del tablero.
* **Inés Goetsch** — *Dev 2* (`funciones.py`)
    * Mecánicas de juego y validación de lógica funcional.
* **Pablo Hernández** — *Dev 3* (`main.py`)
    * Ciclo de vida de la partida y flujo principal.
* **Maksym Chaika** — *Soporte Tecnico*
    * Optimización de código y resolución de incidencias.

---

## 🚀 Cómo ejecutarlo
1. Clona el repositorio:
   ```bash
   git clone [https://github.com/tu-usuario/Hundir_la_flota.git](https://github.com/tu-usuario/Hundir_la_flota.git)