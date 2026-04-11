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

# -CAMBIO SUGERIDO------
# PROBLEMA: No se actualiza el tablero ni las vidas de los barcos.
# SOLUCION: 

def player_shoot(enemy_board, tracking_board):
    
    # Función 2 (para recieve_shot, usa la variable INSTRUCTIONS): Pide al jugador 

    while True:
        
        print(variable.INSTRUCTION_ROW)
        row = int(input())
        print(variable.INSTRUCTION_COLUMN)
        column_letter = input()

        #comprobamos que esté dentro del rango
        if col_number not in variable.COLUMNS:
            print("Column invalid. Use A-J")
            continue
        
        col_number = letter_to_number(column_letter)
        result = enemy_board.receive_shot(row,column_letter)

        if result:
            tracking_board[row,col_number] = variable.MISS
            print(variable.MISS_MSG)
        
        return result


# -CAMBIO SUGERIDO------
# PROBLEMA: Evitar que se repitan disparos
# SOLUCION: 

def machine_shoot(player_board, tracking_cpu):
    
    # Función 3 (para recieve_shot): Máquina dispara al azar

    while True:
        row = random.randint(1, 10)
        col = random.randint(1, 10)
        # Comprobamos que no repita disparo
        if tracking_cpu[row,col] not in (variable.HIT, variable.MISS):
            break
    
    # Comprobamos si hay impacto o agua y reflejamos en la matriz de la maquina
    print(f"The machine fires at row {row} and column {col}")
    result = player_board.receive_shot(row, col)
    if result:
        tracking_cpu[row, col] = variable.HIT 
    else:
        tracking_cpu[row, col] = variable.MISS
    
    # Si hubo impacto, comprobamos si se ha hundido algún barco.
    if result:
        print(f"The machine has impacted your fleet!")
        for ship_obj in player_board.ships_fleet.values():
            if ship_obj.length == 0 and not ship_obj.sunk:
                ship_obj.sunk = True
                print(f"The machine has sunk your {ship_obj.variable.ship_name}")

    return result

# -NUEVA FUNCIÓN-----

def all_ships_sunk(game_board):
    # Función 4. Determina si alguno de los jugadores tiene su 
    # flota hundida y por lo tanto pierde o continua en caso contrario.

    for ship_obj in game_board.ships_fleet.values():
        
        if not ship_obj.is_sunk():
            return False
        
    return True