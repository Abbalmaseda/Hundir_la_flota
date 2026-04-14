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
    # para que se ejecuten en el tablero de CPU y en el tracking del jugador
    #       Comprobamos si el jugador ha ganado, llamando la funcion que comprueba si
    # si toda la flota del enemigo está hundida
    #       Comienza el turno de la maquina
    #       Dispara al tablero del jugador y se marca en su tablero y en el tracking de CPU
    #       Comprobamos si ha ganado la máquina
    #       Cada vez que termine el bucle de recorrer todo lo definido, se suma 1 al turno,
    # haciendo saber al jugador que avanza en el juego.
    #       En el momento que alguno gane termina el bucle del juego

    print(variable.WELCOME_MSG)
    print(variable.PLAYER_NAME_MSG, end="")
    player_name = input().strip()

    
    player_board = board(player_id=player_name)
    cpu_board    = board(player_id="CPU")

    
    player_board.place_ships()
    cpu_board.place_ships()
    print(variable.SUCCES_MSG)

    turn = 1

    
    while True:
        print(f"\n{'='*40}")
        print(f"  TURN {turn}")
        print(f"{'='*40}")

        
        print(f"\nYour board ({player_name}):")
        player_board.display(player_board.my_board)

        print(f"\nYour tracking board:")
        player_board.display(player_board.tracking)

        
        print(f"\n--- {player_name}'s turn ---")
        player_shoot(cpu_board, player_board.tracking)

        
        if all_ships_sunk(cpu_board):
            print(variable.VICTORY_MSG)
            break

        
        print("\n--- CPU's turn ---")
        machine_shoot(player_board, cpu_board.tracking)

        
        if all_ships_sunk(player_board):
            print(variable.LOSE_MSG)
            break

        turn += 1

main()

##################