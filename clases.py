import random
import variable
import numpy as np


class board:

        #Esta clase representa el tablero de juego de un jugador.
        #Attributes:
        #player_id (str): Identificador del jugador. Si no se le pasa nombre
        #                 por defecto será la CPU.

        #size (int): Dimensión del tablero (size x size), le sumamos
        #            uno porque en la fila y columna 0 vamos a incluir
        #            los nombres de estas.

        #my_board (np.ndarray): Matriz con barcos e impactos.
        #                       Este es el tablero donde se colocan los
        #                       barcos del usuario.

        #tracking (np.ndarray): Matriz de seguimiento de disparos al rival.
        #                       Este es el tablero donde ver los impactos que
        #                       hemos causado en la CPU.

        #ships_fleet (dict): Diccionario que almacena las instancias de la clase ship() 
        #                    que hay en este tablero.


    def __init__(self, my_board = "", tracking = "", player_id = "CPU", size = BOARD_SIZE+1,ships_fleet = {}):
        columns_values = []
        rows_values = []
        for c in COLUMNS.keys(): # Recupero los valores por defecto para los títulos de las columnas
            columns_values.append(c) # y los alimento en la lista creada para ello
        for x in ROWS.keys(): # Hago lo mismo para las filas
            rows_values.append(x)

        my_board = np.full([size, size], ' ', dtype=object) #Genero la matriz del tablero del usuario
        my_board[0, 1:] = columns_values # asigno los valores obtenidos anteriormente a la fila y columna 0
        my_board[1:, 0] = rows_values

        tracking = np.full([size, size], ' ', dtype=object) # Lo mismo para el tablero de seguimiento
        tracking[0, 1:] = columns_values
        tracking[1:, 0] = rows_values

        self.player = player_id
        self.board_size = size
        self.my_board = my_board
        self.tracking = tracking
        self.ships_fleet = ships_fleet




    def place_ships(self):

        # Coloca los barcos de manera aleatoria a partir del diccionario SHIPS definido en variable.py
        # El for recorre el diccionario SHIPS para obtener el nombre del barco y su longitud
        # Despues crea la instancia de la clase ship() con el valor de index y lo almacena en el atributo ships_fleet
            
        
        for key, value in SHIPS.items():
            self.ships_fleet[key] = ship(key,value)
            while True:
                self.ships_fleet[key].ship_name = key
                self.ships_fleet[key].length = value
                self.ships_fleet[key].orientation = np.random.randint(1,5) # 1 = north, 2 = east; 3 = south, 4 = west
                x_init = np.random.randint(1,self.board_size) # Genero la posición en las filas
                y_init = np.random.randint(1,self.board_size) # Genero la posición en las columnas
                
                if self.ships_fleet[key].orientation == 1: # Chequeo validez según orientación y defino barco como lista de coordenadas
                    if x_init - (self.ships_fleet[key].length - 1) < 1:
                        continue
                    self.ships_fleet[key].coords = [(x_init - i, y_init) for i in range(self.ships_fleet[key].length)]
                elif self.ships_fleet[key].orientation == 2:
                    if y_init + (self.ships_fleet[key].length - 1) >= self.board_size:
                        continue
                    self.ships_fleet[key].coords = [(x_init, y_init + i) for i in range(self.ships_fleet[key].length)]
                elif self.ships_fleet[key].orientation == 3:
                    if x_init + (self.ships_fleet[key].length - 1) >= self.board_size:
                        continue
                    self.ships_fleet[key].coords = [(x_init + i, y_init) for i in range(self.ships_fleet[key].length)]
                else:
                    if y_init - (self.ships_fleet[key].length - 1) < 1:
                        continue
                    self.ships_fleet[key].coords = [(x_init, y_init - i) for i in range(self.ships_fleet[key].length)]
                

                if any(self.my_board[i,j] == SHIP for i,j in self.ships_fleet[key].coords): # Compruebo que en esas coordenadas no hay un barco
                    continue

                for i, j in self.ships_fleet[key].coords: # Coloco el barco en el tablero del jugador
                    self.my_board[i, j] = SHIP

                break

        return True # Si se colocan todos los barcos, devuelve True
        #return lo_que_sea ¡¡¡Cambiar por mensaje de variables.py!!!
        




    #def receive_shot(self, x: int, y: int):
        # Raise ValueError: Si las coordenadas están fuera del tablero.

        # Procesa un disparo en la coordenada (x, y).
        #   Args:
        #   x (int): Fila del disparo (1-10).
        #   y (int): Columna del disparo (A-J).


        #return bool # True si impacta en barco, False si es agua.
        
        
        
        
    #def display():


class ship():

    # Defino la clase barco. El barco sabe su longitud, dónde está, y si está hundido.

    def __init__(self, ship_name, length, sunk = False, coords = []):
        self.ship_name = ship_name # Posiblemente no haga falta
        self.length = length
        self.sunk = sunk
        self.coords = coords

    # El método is_sunk() devuelve False si el barco flota, y True si ya ha sido impactado en todas sus posiciones.
    # Para que funcione, con cada disparo hay que:
    #   1. Comprobar el valor de la posición que recibe el disparo.
    #   2. Si ha sido impacto, buscar en el atributo ships_fleet qué indice (que instancia de la clase ship()) tiene esa posición.
    #   3. Invocar el método para saber si está hundido: nombre_tablero.ships_fleet["indice"].is_sunk()
    def is_sunk(self):
        if self.length == 0:
            self.sunk = True
        return self.sunk
