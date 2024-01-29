
marcadorA=0
marcadorB=0

while True:

    JugadorA= input("ingrese piedra, papel o tijera: ")
    JugadorB= input("ingrese piedra, papel o tijera: ")

    if JugadorA == JugadorB :
        print(f"empate {JugadorA} and {JugadorB}")
    elif (JugadorA == "tijera" and JugadorB == "papel") or \
             (JugadorA == "papel" and JugadorB == "piedra") or \
             (JugadorA == "piedra" and JugadorB == "tijera"):
            marcadorA += 1
            print(f"A es el ganador de esta ronda: {marcadorA} and {marcadorB}")
    elif (JugadorA == "tijera" and JugadorB == "piedra") or \
         (JugadorA == "papel" and JugadorB == "tijera") or \
         (JugadorA == "piedra" and JugadorB == "papel"):
            marcadorB += 1
            print(f"B es el ganador de esta ronda: {marcadorB} and {marcadorA}")
    if marcadorA == 3 :
        print(f"el jugador A ha ganado")
        
    elif marcadorB == 3 :
        print(f"el jugador B ha ganado")
        