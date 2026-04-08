#-------------------------------------------
#Tamaño del tablero
BOARD_SIZE = 10

#-------------------------------------------
#Barcos y sus medidas
SHIPS = {
    "Pertol_Boat_1": 1,
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
WELCOME_MSG = "Welcome to battleship!"
INSTRUCTION_ROW = "Enter the row number to fire (1-10):"
INSTRUCTION_COLUMN = "Enter the column letter to fire (A-J):"
HIT_MSG = "Hit!"
MISS_MSG =  "Miss"
SUNK_MSG = "Ship sunk!"
VICTORY_MSG = "Congratulations, you won!"
LOSE_MSG = " You lost!"

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
#------------------------------------------------
#Nombre del jugador
player = input("Introduce your NICK")


success_message = "Ships placed"



