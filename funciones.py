#Funciones auxiliares Hundir la Flota

import variable
import random
from clases import board


def letter_to_number(letter):
    
    # Función 1 (usa la variable COLUMNS): Convierte A en 1, B en 2, C en 3, etc.
    
    letter = letter.upper()
    return variable.COLUMNS[letter]


def player_shoot(enemy_board, tracking_board):
    
    # Función 2 (para recieve_shot, usa la variable INSTRUCTIONS): 
    #           
    #           Pide al jugador introducir un numero de row
    #           Comprueba si es un numero, luego si está dentro del tablero
    #           Asigna la row para el disparo
    #
    #           Pide al jugador introducir una columna en letra
    #           Comprobamos si la columna está dentro del tablero
    #           Asignamos la column para el disparo
    #
    #           Comprueba si se ha disparado anteriormente en esa coordenada
    #           Marca el disparo en los tableros

    while True:

        # FILA
        print(variable.INSTRUCTION_ROW)
        fila_input = input()

        print(variable.language["INSTRUCTION_COLUMNS"])
        column = input().upper()

        if column not in variable.COLUMNS:
            print(variable.language["COLUMN_ERROR"])
            continue

        col_num = variable.COLUMNS[column]

        
        print(variable.language["INSTRUCTION_ROWS"])
        row_input = input()

        if not row_input.isdigit():
            print(variable.language["ROW_ERROR"])
            continue

        row = int(row_input)

        if row < 1 or row > 10:
            print(variable.language["ROW_LENGTH_ERROR"])
            continue


        if tracking_board[row, col_num] != variable.WATER:
            print(variable.language["REPEAT_SHOT"])
            continue
        
        hit = enemy_board.receive_shot(row, col_num)
        
        if hit:
            print(variable.language["HIT_MSG"])
            tracking_board[row, col_num] = variable.HIT
            coord_hit = (row, col_num)

            for ship in enemy_board.ships_fleet.values():
                if coord_hit in ship.coords:
                    sunk = ship.is_sunk()
                    if sunk:
                        print(ship.ship_name)
                        print(variable.language["SUNK_MSG"])
                    break
        else:
            print(variable.language["MISS_MSG"])
            tracking_board[row, col_num] = variable.MISS

        break

def machine_shoot(player_board, tracking_board):

    # Función 3 (para recieve_shot): Máquina dispara al azar.
    #       Comprobamos que no repita disparo
    #       Indicamos donde dispara F y C
    #       Acto de recibir disparo en el tablero jugador y marcamos
    #       Comprobamos si hubo impacto en la flota
    
    while True:
        row = random.randint(1, 10)
        col = random.randint(1, 10)
        col_to_text = [key for key, values in variable.COLUMNS.items() if values == col]

        
        if tracking_board[row, col] != variable.WATER:
            continue
        
        print(f"{variable.language["CPU_SHOT"].format(col=col_to_text[0],row=row)}")

        hit = player_board.receive_shot(row, col)

        if hit:
            tracking_board[row, col] = variable.HIT
            print(variable.language["HIT_MSG"])
            coord_hit = (row, col)

            for ship in player_board.ships_fleet.values():
                if coord_hit in ship.coords:
                    sunk = ship.is_sunk()
                    if sunk:
                        print(ship.ship_name)
                        print(variable.language["SUNK_MSG"])
                    break

        else:
            tracking_board[row, col] = variable.MISS
            print(variable.language["MISS_MSG"])

        break

def all_ships_sunk(self):
        
        # Función 4. Determina si alguno de los jugadores tiene su 
        # flota hundida y por lo tanto pierde o continua en caso contrario.

        return all(ship.is_sunk() for ship in self.ships_fleet.values())

##########
