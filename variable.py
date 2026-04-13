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
INSTRUCTION_ROW = "Introduce un número de fila para disparar (1-10):"
INSTRUCTION_COLUMN = "Introduce una letra de columna para disparar (A-J):"
HIT_MSG = "Tocado"
MISS_MSG =  "Agua"
SUNK_MSG = "¡Hundido!"
VICTORY_MSG = "¡Victoria! Enhorabuena has hundido la flota rival"
LOSE_MSG = "Has perdido. Vuelve a intentarlo"
PLAYER_NAME_MSG = "Introduce tu nombre: "
SUCCES_MSG = "Los barcos han sido colocados"

#-------------------------------------------
# Filas enumeradas desde el 1 hasta el 101
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
# Diccionarios de idiomas
dict_ES = {
    "WELCOME_MSG": "Bienvenido a Hundir la Flota",  
    "INSTRUCTIONS_GAME": "¡Coloca tus barcos en el tablero y dispara coordenadas para intentar hundir los barcos del rival! Gana quien consiga destruir toda la flota enemiga antes",   
    "INSTRUCTION_ROW": "Introduce un número de fila para disparar (1-10):",
    "INSTRUCTION_COLUMNS": "Introduce una letra de columna para disparar (A-J):",
    "HIT_MSG": "Tocado",
    "MISS_MSG": "Agua",
    "SUNK_MSG": "¡Hundido!",
    "VICTORY_MSG": "¡Victoria! Enhorabuena has hundido la flota rival",
    "LOSE_MSG": "Has perdido. Vuelve a intentarlo",
    "PLAYER_NAME_MSG": "Introduce tu nombre: ",
    "SUCCES_MSG": "Los barcos han sido colocados",
    "XY_ERROR": "Coordenadas no válidas",
    "XY_LENGTH_ERORR": "Coordenadas fuera del tablero",
    "ROW_ERROR": "Debes introducir un número",
    "ROW_LENGTH_ERROR": "Fila fuera de rango",
    "COLUMN_ERROR": "Columna inválida",
    "REPEAT_SHOT": "Ya has disparado ahí",
    "CPU_SHOT": "La CPU dispara a fila {fila}, columna {col}",
    "PLAYER_BOARD_NAME": "\nTu tablero ({player_name}):",
    "PLAYER_TURN": "\n--- Turno de {player_name}  ---",
    "CPU_BOARD_NAME": "\nTablero de seguimiento:",
    "CPU_TURN": "\n--- Turno de la CPU ---"

}

dict_EN = {
    "WELCOME_MSG": "Welcome to Battleship!",  
    "INSTRUCTIONS_GAME": "Place your ships on the board and fire at coordinates to try to sink your opponent’s fleet! Win by destroying all enemy ships before yours are sunk",   
    "INSTRUCTION_ROW": "Enter the row number to fire (1-10):",
    "INSTRUCTION_COLUMNS": "Enter the column letter to fire (A-J):",
    "HIT_MSG": "Hit",
    "MISS_MSG": "Miss",
    "SUNK_MSG": "Ship sunk!",
    "VICTORY_MSG": "Victory! Congratulations you have sunk the enemy fleet",
    "LOSE_MSG": "You lost. Try again",
    "PLAYER_NAME_MSG": "Enter your name: ",
    "SUCCES_MSG": "Ships have been placed",
    "XY_ERROR": "Invalid coordinates",
    "XY_LENGTH_ERORR": "Coordinates ouf of bounds",
    "ROW_ERROR": "You must enter a number",
    "ROW_LENGTH_ERROR": "Row out of range",
    "COLUMN_ERROR": "Invalid column",
    "REPEAT_SHOT": "You've already fired there",
    "CPU_SHOT": "CPU fires at row {fila}, column {col}",
    "PLAYER_BOARD_NAME": "\n--- Your board ({player_name}): ---",
    "PLAYER_TURN": "\n--- {player_name}'s turn ---",
    "CPU_BOARD_NAME": "\n--- Your tracking board: ---",
    "CPU_TURN": "\n--- CPU's turn ---"
}


