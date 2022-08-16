import random


def jugar():
    print("BIENVENIDO AL SUPER JUEGO CACHIPOOM, HABER QUE ONDA")

    usuario = input("Escoge una opcion: 'pi' para piedra, 'pa' para papel, 'ti' para tijera.\n").lower()
    computadora = random.choice(['pi', 'pa' , 'ti' ])

    if usuario == computadora:
        return (f"! Empate, yo habi elegido {computadora} ")

    if gano_el_jugador(usuario, computadora):
        return (f"!Ganaste tontito, yo habia elegido {computadora} ")

    return (f"Perdiste tontito, yo habia elegido {computadora}!!")


def gano_el_jugador(jugador, oponente):

    if ((jugador == 'pi' and oponente == 'ti')
        or (jugador == 'ti' and oponente == 'pa')
        or (jugador == 'pa' and oponente == 'pi')):
        return True
    else:
        return False


print(jugar())

