import variable
from clases import board
from funciones import player_shoot, machine_shoot, all_ships_sunk

def main():
    
    # Función principal del juego:
    #       Comenzamos con la bienvenida y recogida del nombre del jugador
    #       Creación de tableros
    #       Colocación flota
    #       Establecemos un turno por jugador
    #       Bucle principal del juego
    #       Número de turno
    #       Se muestran ambos tableros; flota del jugador y tracking
    #       Comienza el jugador, llamamos las funciones de disparo
    #       para que se ejecuten en el tablero de CPU y en el tracking del jugador
    #       Comprobamos si el jugador ha ganado, llamando la funcion que comprueba si
    #       si toda la flota del enemigo está hundida
    #       Comienza el turno de la maquina
    #       Dispara al tablero del jugador y se marca en su tablero y en el tracking de CPU
    #       Comprobamos si ha ganado la máquina
    #       Cada vez que termine el bucle de recorrer todo lo definido, se suma 1 al turno,
    #          haciendo saber al jugador que avanza en el juego.
    #       En el momento que alguno gane termina el bucle del juego

    print(variable.HEADER)
    set_language = input(variable.OUTPUT_MSG)
    if set_language.upper() == "EN":
        variable.language = variable.dict_EN
        print("You have selected to play in English.")
    elif set_language.upper() == "ES":
        variable.language = variable.dict_ES
        print("Has seleccionado jugar en español.")
    
    
    print(variable.language["WELCOME_MSG"])
    print(variable.language["INSTRUCTIONS_GAME"])
    print(variable.language["PLAYER_NAME_MSG"], end="")
    player_name = input().strip()

    
    player_board = board(player_id=player_name)
    cpu_board    = board(player_id="CPU")

    
    player_board.place_ships()
    cpu_board.place_ships()
    print(variable.language["SUCCES_MSG"])

    turn = 1

    
    while True:
        print(f"\n{'='*40}")
        print(f"{variable.language["TURN"].format(turn=turn)}")
        print(f"{'='*40}\n")

        
        print(f"{variable.language["PLAYER_BOARD_NAME"].format(player_name=player_name)}")

        player_board.display(player_board.my_board)

        print(f"{variable.language["CPU_BOARD_NAME"]}")
        player_board.display(player_board.tracking)

        # --- Turno del jugador ---
        print(f"{variable.language["PLAYER_TURN"].format(player_name=player_name)}")
        player_shoot(cpu_board, player_board.tracking)

        
        if all_ships_sunk(cpu_board):
            print(variable.language["VICTORY_MSG"])
            break

        
        print(variable.language["CPU_TURN"])
        machine_shoot(player_board, cpu_board.tracking)

        
        if all_ships_sunk(player_board):
            print(variable.language["LOSE_MSG"])
            break

        turn += 1

main()

##################