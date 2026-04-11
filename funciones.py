#Funciones auxiliares Hundir la Flota

import variable
import random
from clases import board


# -CAMBIO SUGERIDO------
# PROBLEMA: Resto de codigo en ingles
# SOLUCION: Cambio al ingles
def letter_to_number(letter):
    # Función 1 (usa la variable COLUMNS): Convierte A en 1, B en 2, C en 3, etc.
    letter = letter.upper()
    return variable.COLUMNS[letter]

def player_shoot(enemy_board):
    # Función 2 (para recieve_shot, usa la variable INSTRUCTIONS): Pide al jugador dónde disparar
    print(variable.INSTRUCTION_ROW)
    row = int(input())
    
    print(variable.INSTRUCTION_COLUMN)
    column = input()
    col_number = letter_to_number(column)
    
    # Llama al método del tablero enemigo
    return enemy_board.receive_shot(row, col_number)

def machine_shoot(player_board):
    # Función 3 (para recieve_shot): Máquina dispara al azar
    row = random.randint(1, 10)
    col = random.randint(1, 10)
    print(f"The machine fires at row {row} and column {col}")
    return player_board.receive_shot(row, col)