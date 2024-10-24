nombre1 = input("¿Cómo se llamará el jugador 1?: ")
nombre2 = input("¿Cómo se llamará el jugador 2?: ")

seguir_jugando = "si"

while seguir_jugando.lower() == "si":
    # Solicitar jugadas y convertir a minúsculas
    jugador_1 = input(f"¡Hola {nombre1}! ¿Qué eliges? ¿Piedra, papel o tijera?: ").lower()
    jugador_2 = input(f"¡Hola {nombre2}! ¿Qué eliges? ¿Piedra, papel o tijera?: ").lower()

    condicion1 = jugador_1 == "piedra" and jugador_2 == "tijera"
    condicion2 = jugador_1 == "papel" and jugador_2 == "piedra"
    condicion3 = jugador_1 == "tijera" and jugador_2 == "papel"

    if jugador_1 == jugador_2:
        print("¡Ha sido un empate!")
    elif condicion1 or condicion2 or condicion3:
        print('Ha ganado:', nombre1)
    else:
        print('Ha ganado:', nombre2)  # Corregido: antes decía nombre1
    
    seguir_jugando = input("¿Desean jugar otra vez? (si/no): ")

print("¡Gracias por jugar!")