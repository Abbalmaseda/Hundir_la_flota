#-------------------------------------------
#Tamaño del tablero
BOARD_SIZE = 10

#-------------------------------------------
#Barcos y sus medidas
SHIPS = {
    "Petrol_Boat_1": 1,
    "Petrol_Boat_2":1,
    "Petrol_Boat_3":1,
    "Petrol_Boat_4":1,
    "Destroyer_1":2,
    "Destroyer_2":2,
    "Destroyer_3":2,
    "Submarine_1":3,
    "Submarine_2":3,
    "Battleship":4
}

SHIPS_S = dict(sorted(SHIPS.items(), key=lambda x: x[1], reverse=True))

#-------------------------------------------
#Simbolos tablero
WATER = "~"
SHIP = "S"
HIT = "X"
MISS = "O"

#-------------------------------------------
#Mensajes 
WELCOME_MSG = "Bienvenido a Hundir la Flota"
INSTRUCTIONS_GAME = "¡Coloca tus barcos en el tablero y dispara coordenadas para intentar hundir los barcos del rival! Gana quien consiga destruir toda la flota enemiga antes"
INSTRUCTION_ROW = "Introduce un número de row para disparar (1-10):"
INSTRUCTION_COLUMN = "Introduce una letra de columna para disparar (A-J):"
HIT_MSG = "Tocado"
MISS_MSG =  "Agua"
SUNK_MSG = "¡Hundido!"
VICTORY_MSG = "¡Victoria! Enhorabuena has hundido la flota rival"
LOSE_MSG = "Has perdido. Vuelve a intentarlo"
PLAYER_NAME_MSG = "Introduce tu nombre: "
SUCCES_MSG = "Los barcos han sido colocados"

#-------------------------------------------
# rows enumeradas desde el 1 hasta el 101
ROWS = {i: i for i in range(1, BOARD_SIZE+1)}

#-------------------------------------------
# Columnas desde la A a la J
COLUMNS = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10
}

#-------------------------------------------
# Variables para Multidioma

language = {}
LANGUAGE_OPTIONS = ["ES","EN"]
OUTPUT_MSG = f"Selecciona el idioma del juego: {LANGUAGE_OPTIONS}:"


#-------------------------------------------
# Diccionarios de idiomas
dict_ES = {
    "WELCOME_MSG": "Bienvenido a Hundir la Flota.",  
    "INSTRUCTIONS_GAME": "¡Dispara coordenadas para intentar hundir los barcos del rival!\nGana quien consiga destruir toda la flota enemiga antes.\nLos barcos se colocan de manera aleatoria.\nEmpiezas jugando tú",   
    "INSTRUCTION_ROWS": "Introduce un número de fila para disparar (1-10):",
    "INSTRUCTION_COLUMNS": "Introduce una letra de columna para disparar (A-J):",
    "HIT_MSG": "Tocado.",
    "MISS_MSG": "Agua.",
    "SUNK_MSG": "¡Hundido!",
    "VICTORY_MSG": "¡Victoria! Enhorabuena has hundido la flota rival.",
    "LOSE_MSG": "Has perdido. Vuelve a intentarlo.",
    "PLAYER_NAME_MSG": "Introduce tu nombre: ",
    "SUCCES_MSG": "Los barcos han sido colocados.",
    "XY_ERROR": "Coordenadas no válidas.",
    "XY_LENGTH_ERORR": "Coordenadas fuera del tablero.",
    "ROW_ERROR": "Debes introducir un número.",
    "ROW_LENGTH_ERROR": "Fila fuera de rango.",
    "COLUMN_ERROR": "Columna inválida.",
    "REPEAT_SHOT": "Ya has disparado ahí.",
    "CPU_SHOT": "La CPU dispara a {col}{row}.",
    "PLAYER_BOARD_NAME": "\nTu tablero ({player_name}):\n",
    "PLAYER_TURN": "\n--- Turno de {player_name}  ---\n",
    "CPU_BOARD_NAME": "\nTablero de seguimiento:\n",
    "CPU_TURN": "\n--- Turno de la CPU ---\n",
    "TURN": "  TURNO {turn}"

}

dict_EN = {
    "WELCOME_MSG": "Welcome to Battleship!",  
    "INSTRUCTIONS_GAME": "Fire at coordinates to try to sink your opponent’s fleet!\nWin by destroying all enemy ships before yours are sunk.\nShips are placed randomly.\nYou start playing.",   
    "INSTRUCTION_ROWS": "Enter the row number to fire (1-10):",
    "INSTRUCTION_COLUMNS": "Enter the column letter to fire (A-J):",
    "HIT_MSG": "Hit.",
    "MISS_MSG": "Miss.",
    "SUNK_MSG": "Ship sunk!",
    "VICTORY_MSG": "Victory! Congratulations you have sunk the enemy fleet.",
    "LOSE_MSG": "You lost. Try again.",
    "PLAYER_NAME_MSG": "Enter your name: ",
    "SUCCES_MSG": "Ships have been placed.",
    "XY_ERROR": "Invalid coordinates.",
    "XY_LENGTH_ERORR": "Coordinates ouf of bounds.",
    "ROW_ERROR": "You must enter a number.",
    "ROW_LENGTH_ERROR": "Row out of range.",
    "COLUMN_ERROR": "Invalid column.",
    "REPEAT_SHOT": "You've already fired there.",
    "CPU_SHOT": "CPU fires at {col}{row}.",
    "PLAYER_BOARD_NAME": "\n--- Your board ({player_name}): ---\n",
    "PLAYER_TURN": "\n--- {player_name}'s turn ---\n",
    "CPU_BOARD_NAME": "\n--- Your tracking board: ---\n",
    "CPU_TURN": "\n--- CPU's turn ---\n",
    "TURN": "  TURN {turn}"
}


HEADER = r"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      _   _ _   _ _   _ ____ ___ ____  
     | | | | | | | \ | |  _ \_ _|  _ \ 
     | |_| | | | |  \| | | | | || |_) |
     |  _  | |_| | |\  | |_| | ||  _ < 
     |_| |_|\___/|_| \_|____/___|_| \_\
                                      
         L A   F L O T A
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
