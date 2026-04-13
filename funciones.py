#Funciones auxiliares Hundir la Flota

import variable
import random
from clases import board


def letter_to_number(letter):
    # Función 1 (usa la variable COLUMNS): Convierte A en 1, B en 2, C en 3, etc.
def letter_to_number(letter):
    letter = letter.upper()
    if letter in variable.COLUMNS: 
        return variable.COLUMNS[letter]
    else:
        raise ValueError("¡Invalid column! Use A-J.") 

def player_shot(enemy_board):
    # Función 2 (para receive_shot, usa las variables INSTRUCTIONS): Pide al jugador dónde disparar
    while True:
        try:
            row = int(input(variable.INSTRUCTION_ROW))
            column = input(variable.INSTRUCTION_COLUMN)
            col_number = letter_to_number(column)
            # Llama al método del tablero enemigo
            return enemy_board.receive_shot(row, col_number)
        except (ValueError, KeyError):
            print("¡Fail! Row (1-10), column (A-J). Try again.")


def computer_shot(player_board):
    # Función 3 (para receive_shot): Máquina dispara al azar
    row = random.randint(1, variable.BOARD_SIZE)
    col = random.randint(1, variable.BOARD_SIZE)
    print(f"Computer shoots at row {row}, column {col}")
    return player_board.receive_shot(row, col)