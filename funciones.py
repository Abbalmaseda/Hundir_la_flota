#Funciones auxiliares Hundir la Flota

import variable
import random
from clases import board

def letra_a_numero(letra):
    # Función 1 (usa la variable COLUMNS): Convierte A en 1, B en 2, C en 3, etc.
    letra = letra.upper()
    return variable.COLUMNS[letra]

def disparo_jugador(tablero_enemigo, tracking_board):
    
    while True:

        # FILA
        print(variable.INSTRUCTION_ROW)
        fila_input = input()

        if not fila_input.isdigit():
            print("Debes introducir un número.")
            continue

        fila = int(fila_input)

        if fila < 1 or fila > 10:
            print("Fila fuera de rango.")
            continue

        # COLUMNA
        print(variable.INSTRUCTION_COLUMN)
        columna = input().upper()

        if columna not in variable.COLUMNS:
            print("Columna inválida.")
            continue

        col_num = variable.COLUMNS[columna]

        # COMPROBAR REPETIDO
        if tracking_board[fila, col_num] != variable.WATER:
            print("Ya has disparado ahí.")
            continue

        # DISPARO
        hit = tablero_enemigo.receive_shot(fila, col_num)

        if hit:
            print(variable.HIT_MSG)
            tracking_board[fila, col_num] = variable.HIT
        else:
            print(variable.MISS_MSG)
            tracking_board[fila, col_num] = variable.MISS

        break

def disparo_maquina(tablero_jugador, tracking_board):
    while True:
        fila = random.randint(1, 10)
        col = random.randint(1, 10)

        # Evitar repetir disparos
        if tracking_board[fila, col] != variable.WATER:
            continue

        print(f"Máquina dispara a fila {fila}, columna {col}")

        hit = tablero_jugador.receive_shot(fila, col)

        if hit:
            tracking_board[fila, col] = variable.HIT
        else:
            tracking_board[fila, col] = variable.MISS

        break

def all_ships_sunk(self):
        return all(ship.is_sunk() for ship in self.ships_fleet.values())  #Comprobamos si estan todos los barcos hundidos

#############