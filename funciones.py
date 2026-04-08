#Funciones auxiliares Hundir la Flota

import variable
import random
from clases import board

def letra_a_numero(letra):
    # Función 1 (usa la variable COLUMNS): Convierte A en 1, B en 2, C en 3, etc.
    letra = letra.upper()
    return variable.COLUMNS[letra]

def disparo_jugador(tablero_enemigo):
    # Función 2 (para recieve_shot, usa la variable INSTRUCTIONS): Pide al jugador dónde disparar
    print(variable.INSTRUCTION_ROW)
    fila = int(input())
    
    print(variable.INSTRUCTION_COLUMN)
    columna = input()
    col_numero = letra_a_numero(columna)
    
    # Llama al método del tablero enemigo
    return tablero_enemigo.receive_shot(fila, col_numero)

def disparo_maquina(tablero_jugador):
    # Función 3 (para recieve_shot): Máquina dispara al azar
    fila = random.randint(1, 10)
    col = random.randint(1, 10)
    print(f"Máquina dispara a fila {fila}, columna {col}")
    return tablero_jugador.receive_shot(fila, col)