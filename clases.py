import random
import variable
import numpy as np


class board:

        #Esta clase representa el tablero de juego de un jugador.
        #Atributos:
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


    def __init__(self, my_board = "", tracking = "", player_id = "CPU", size = variable.BOARD_SIZE+1):
        columns_values = []
        rows_values = []
        for c in variable.COLUMNS.keys(): # Recupero los valores por defecto para los títulos de las columnas
            columns_values.append(c) # y los alimento en la lista creada para ello
        for x in variable.ROWS.keys(): # Hago lo mismo para las filas
            rows_values.append(str(x))

        my_board = np.full([size, size], variable.WATER, dtype=object) #Genero la matriz del tablero del usuario
        my_board[0, 0] = " "
        my_board[0, 1:] = columns_values # asigno los valores obtenidos anteriormente a la fila y columna 0
        my_board[1:, 0] = rows_values

        tracking = np.full([size, size], variable.WATER, dtype=object) # Lo mismo para el tablero de seguimiento
        tracking[0, 0] = " "
        tracking[0, 1:] = columns_values
        tracking[1:, 0] = rows_values

        self.player = player_id
        self.board_size = size
        self.my_board = my_board
        self.tracking = tracking
        self.ships_fleet = {}
        # -CAMBIO SUGERIDO------
        # PROBLEMA: Solo se crea un tablero.
        # SOLUCIÓN: linea 29 y 51. No compartir diccionario con CPU.




    def place_ships(self):

        # Coloca los barcos de manera aleatoria a partir del diccionario SHIPS definido en variable.py
        # El for recorre el diccionario SHIPS para obtener el nombre del barco y su longitud.
        # Despues crea la instancia de la clase ship() con el valor de index y lo almacena en el atributo ships_fleet.
        # El bucle while True se ejecuta hasta que el objeto barco está ubicado correctamente de manera aleatoria.
            
        
        for key, value in variable.SHIPS.items():
            self.ships_fleet[key] = ship(key,value)
            while True:
                self.ships_fleet[key].ship_name = key
                self.ships_fleet[key].length = value
                self.ships_fleet[key].orientation = np.random.randint(1,5) # 1 = north, 2 = east; 3 = south, 4 = west
                x_init = np.random.randint(1,self.board_size) # Genero la posición en las filas
                y_init = np.random.randint(1,self.board_size) # Genero la posición en las columnas
                

                if self.ships_fleet[key].orientation == 1:
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
                
                # Comprueba que en esas coordenadas no hay un barco
                if any(self.my_board[i,j] == variable.SHIP for i,j in self.ships_fleet[key].coords): 
                    continue
                
                # Coloca el barco en el tablero del jugador
                for i, j in self.ships_fleet[key].coords: 
                    self.my_board[i, j] = variable.SHIP

                break

        return True # Si se colocan todos los barcos, devuelve True (debería ser una salida por pantalla)
        




    def receive_shot(self, x: int, y: int):
        
        # Recive un valor int como coordenadas x e y, sería bueno una función que recoja el valor introducido por el usuario,
        # lo mapee en el caso de las columnas, lo convierta a int y llame al método
        # pasando esos int como argumentos.
        
        # MODO DE USO:
        #   1. Llamar al método pasando los argumentos como int. Devuelve ValueError en caso de que no llegue como int.
        #   2. Comprueba que las coordenadas están en la zona de disparo, sin valor 0 en fila o columna y no excede las dimensiones del tablero. Devuelve ValueError si eso ocurre.
        #   3. Comprueba el valor de la posición impacatada. Si ha impactado, devuelve True, si es agua devuelve False.

        
        if not isinstance(x, int) or not isinstance(y, int):
            raise ValueError("Las coordenadas recibidas no son válidas.") #Esto debería ser un mensaje de error en variable.py
        elif x > self.my_board.size or y > self.my_board.shape[1]:
            raise ValueError("Las coordenadas recibidas no son válidas.") #Esto debería ser un mensaje de error en variable.py
        elif x == 0 or y == 0:
            raise ValueError("Las coordenadas recibidas no son válidas.") #Esto debería ser un mensaje de error en variable.py
        
        # -CAMBIO SUGERIDO M------------------
        # PROBLEMA: No se refleja en el tablero los disparos, tampoco se resta vida a los barcos
        # SOLUCION: 
        if self.my_board[x,y] == variable.SHIP:
            self.my_board[x,y] = variable.HIT #Marca en el tablero "X"
            # Buscamos el barco al que pertenece esa celda y restamos una vida
            for ship_obj in self.ships_fleet.values():
                if (x,y) in ship_obj.coords:
                    ship_obj.lenght -= 1 
                    break
            return True
        else:
            self.my_board[x,y] = variable.MISS #Marca en el tablero "O"
            return False
        
        
        
        
    def display(self,attr):

        # Recibe un atributo como argumento, el argumento debe ser el nombre del tablero a mostrar (my_board o tracking).
        # Lo que hace es recorrer la matriz con el primer for y convertir cada array en una lista usando como separador espacios
        # para mostrar una impresión en pantalla ordenada y limpia.
        # El primer for se usa para alinear números de 1 cifra y el segundo de 2 cifras.

        # MODO DE USO:
        #   Para mostrar el tablero del jugador: nombre_del_objeto_tablero.display(nombre_del_objeto_tablero.my_board)
        #   Para mostrar el tablero de la CPU: nombre_del_objeto_tablero.display(nombre_del_objeto_tablero.tracking)

        for i in attr[:10]:
                print("  ".join([str(x) for x in i]))
        for i in attr[10:]:
            print(" ".join([str(x) for x in i[0:1]]), end=" ")
            print("  ".join([str(x) for x in i[1:]]))


class ship():

    # Define la clase barco. Cada barco será una instancia de este objeto.
    # 
    # Atributos:
    #   ship_name (str): Nombre del barco obtenido del diccionario SHIPS. No es crítico, lo dejamos
    #                    por si en el flujo se quiere preguntar al barco cómo se llama.
    #
    #   length (int): Es la longitud actual del barco, comienza siendo la longitud total y se le restan los impactos.
    #
    #   sunk (bool): Sirve para saber si el barco flota o se ha hundido. Cominza siendo False porque el barco flota por defecto.
    #
    #   coords (list): Son las coordenadas de hubicación del barco.
    

    def __init__(self, ship_name, length, sunk = False, coords = []):
        self.ship_name = ship_name
        self.length = length
        self.sunk = sunk
        self.coords = coords

    def is_sunk(self):

        # El método is_sunk() devuelve False si el barco flota, y True si ya ha sido impactado en todas sus posiciones.
        # MODO DE USO:
        # con cada disparo hay que:
        #   1. Comprobar el valor de la posición que recibe el disparo.
        #   2. Si ha sido impacto, buscar en el atributo ships_fleet qué indice (que instancia de la clase ship()) tiene esa posición.
        #   3. Restar una posición al atributo lenght del barco.
        #   3. Invocar el método para saber si está hundido: nombre_tablero.ships_fleet["indice"].is_sunk()

        if self.length == 0:
            self.sunk = True
        return self.sunk