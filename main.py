import random

# Función para obtener el movimiento del jugador
def obtener_movimiento_jugador():
    return input("Elige tu movimiento (Piedra, Papel, Tijera, Lagarto o Spock): ").capitalize()

# Función para obtener el movimiento de la máquina
def obtener_movimiento_maquina():
    movimientos = ["Piedra", "Papel", "Tijera", "Lagarto", "Spock"]
    return random.choice(movimientos)

# Función para determinar el ganador
def determinar_ganador(jugador, maquina):
    if jugador == maquina:
        return "Empate"
    elif (jugador == "Piedra" and maquina == "Tijera") or (jugador == "Papel" and maquina == "Piedra") or \
            (jugador == "Tijera" and maquina == "Papel") or (jugador == "Spock" and maquina == "Tijera") or \
            (jugador == "Spock" and maquina == "Piedra") or (jugador == "Lagarto" and maquina == "Spock") or \
            (jugador == "Lagarto" and maquina == "Papel"):
        return "Jugador"
    else:
        return "Máquina"

# Función para preguntar al usuario si desea jugar otra partida
def jugar_otra_partida():
    respuesta = input("¿Deseas jugar otra partida? (sí/no): ").lower()
    return respuesta == "si"

# Función principal del juego
def ejecutar_juego():
    print("Bienvenido al Juego")
    print("Recuerda las siguientes reglas:  \nLas tijeras cortan el papel. \nEl papel cubre la piedra. \nLa piedra aplasta el lagarto. \nEl lagarto envenena a Spock. \nSpock aplasta las tijeras. \nLas tijeras decapitan el lagarto. \nEl lagarto se come el papel. \nEl papel refuta a Spock. \nSpock vaporiza la piedra. \nLa piedra aplasta a las tijeras.")
    print("El primero en llegar a 3 victorias gana la partida")
    victorias_jugador = 0
    victorias_maquina = 0

    while victorias_jugador < 3 and victorias_maquina < 3:
        print(f"Victorias jugador: {victorias_jugador} - Victorias máquina: {victorias_maquina}")
        jugador = obtener_movimiento_jugador()
        if jugador not in ["Piedra", "Papel", "Tijera", "Lagarto", "Spock"]:
            print("Movimiento inválido. Intenta de nuevo.")
            continue

        maquina = obtener_movimiento_maquina()
        print(f"La máquina eligió: {maquina}")

        ganador = determinar_ganador(jugador, maquina)
        if ganador == "Empate":
            print("Es un empate!")
        else:
            if ganador == "Jugador":
                print("¡Ganaste esta ronda!")
                victorias_jugador += 1
            else:
                print("Gana la máquina.")
                victorias_maquina += 1

    if victorias_jugador == 3:
        print("¡Felicidades! Ganaste la partida.")
    else:
        print("La máquina ha ganado la partida. ¡Inténtalo nuevamente!")

    # Preguntar al usuario si desea jugar otra partida
    if jugar_otra_partida():
        ejecutar_juego()
    else:
        print("Gracias por jugar. ¡Hasta luego!")

# Iniciar el juego
if __name__ == "__main__":
    ejecutar_juego()
