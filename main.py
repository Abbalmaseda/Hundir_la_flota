import variable
from clases import board
from funciones import disparo_jugador, disparo_maquina, all_ships_sunk

def main():
    
    # Bienvenida y nombre del jugador
    print(variable.WELCOME_MSG)
    print(variable.PLAYER_NAME_MSG, end="")
    player_name = input().strip()

    # Crear tableros
    player_board = board(player_id=player_name)
    cpu_board    = board(player_id="CPU")

    # Colocar barcos
    player_board.place_ships()
    cpu_board.place_ships()
    print(variable.success_message)

    turn = 1

    # Bucle principal del juego
    while True:
        print(f"\n{'='*40}")
        print(f"  TURN {turn}")
        print(f"{'='*40}")

        # Mostrar tableros
        print(f"\nYour board ({player_name}):")
        player_board.display(player_board.my_board)

        print(f"\nYour tracking board:")
        player_board.display(player_board.tracking)

        # --- Turno del jugador ---
        print(f"\n--- {player_name}'s turn ---")
        disparo_jugador(cpu_board, player_board.tracking)

        # Comprobamos si el jugador ha ganado
        if all_ships_sunk(cpu_board):
            print(variable.VICTORY_MSG)
            break

        # --- Turno de la máquina ---
        print("\n--- CPU's turn ---")
        disparo_maquina(player_board, cpu_board.tracking)

        # Comprobamos si la máquina ha ganado
        if all_ships_sunk(player_board):
            print(variable.LOSE_MSG)
            break

        turn += 1

main()