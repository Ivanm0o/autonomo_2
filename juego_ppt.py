import random

print("========================================")
print("     JUEGO: PIEDRA, PAPEL O TIJERA      ")
print("========================================")

nombre = input("Ingresa tu nombre: ")

victorias = 0
derrotas = 0
seguir_jugando = "si"

# Bucle
while seguir_jugando == "si":
    
    print("----------------------------------------")
    print("Marcador -> Ganadas: " + str(victorias) + " | Perdidas: " + str(derrotas))
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    
    opcion = input("Elige una opción (1, 2 o 3): ")
    
    # Valicación
    if opcion == "1" or opcion == "2" or opcion == "3":
        
        #Elección por parte del PC
        pc_numero = random.randint(1, 3)
        
        if pc_numero == 1:
            pc_eleccion = "Piedra"
        elif pc_numero == 2:
            pc_eleccion = "Papel"
        else:
            pc_eleccion = "Tijera"
            
        print("La PC eligió: " + pc_eleccion)
        
        # Lógica de ganador, perdedor o empate
        usuario_numero = int(opcion)
        
        if usuario_numero == pc_numero:
            print("¡Es un EMPATE!")
        elif (usuario_numero == 1 and pc_numero == 3) or (usuario_numero == 2 and pc_numero == 1) or (usuario_numero == 3 and pc_numero == 2):
            print("¡GANASTE " + nombre + "!")
            victorias = victorias + 1
        else:
            print("¡PERDISTE!")
            derrotas = derrotas + 1
            
    else:
        print("Opción no válida. Escribe 1, 2 o 3.")

    #Pregunta para controlar el bucle
    print("----------------------------------------")
    input_seguir = input("¿Jugar otra vez? (si/no): ")
    
    if input_seguir == "si" or input_seguir == "SI":
        seguir_jugando = "si"
    else:
        seguir_jugando = "no"

print("Fin del juego.")