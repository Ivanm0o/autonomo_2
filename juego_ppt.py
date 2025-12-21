import tkinter as tk
import random

# Colores del programa
COLOR_FONDO = "#121212"
COLOR_TEXTO = "#FFFFFF"
COLOR_BOTONES = "#03DAC6" 
COLOR_TITULOS = "#BB86FC"
COLOR_ROJO = "#E63455"

# Opciones fijas del juego (Tupla)
OPCIONES = ("Piedra", "Papel", "Tijera")

# Variables para guardar datos
victorias = 0
derrotas = 0
empates = 0
nombre_jugador = "Jugador"

# --- Funciones del Juego ---

def turno_pc():
    # La PC elige un numero al azar entre 1 y 3
    numero = random.randint(1, 3)
    # Sacamos el nombre de la tupla (restamos 1 porque empieza en 0)
    nombre_eleccion = OPCIONES[numero - 1]
    return nombre_eleccion, numero

def calcular_ganador(mi_num, pc_num):
    # 0: Empate, 1: Gane, -1: Perdi
    if mi_num == pc_num:
        return 0
    elif (mi_num == 1 and pc_num == 3) or (mi_num == 2 and pc_num == 1) or (mi_num == 3 and pc_num == 2):
        return 1
    else:
        return -1

# Funciones de la Ventana 

def iniciar():
    global nombre_jugador
    # Guardamos el nombre si escribieron algo
    texto = entrada_nombre.get()
    if texto != "":
        nombre_jugador = texto
    
    # Cambiamos de pantalla
    frame_inicio.pack_forget()
    frame_juego.pack(expand=True, fill="both", padx=20, pady=20)
    
    # Actualizamos el nombre en la pantalla de juego
    lbl_jugador.config(text="Jugador: " + nombre_jugador)

def boton_jugar(opcion_usuario):
    global victorias, derrotas, empates

    # Logica de la PC y resultado
    texto_pc, numero_pc = turno_pc()
    resultado = calcular_ganador(opcion_usuario, numero_pc)

    # Decidimos que mensaje mostrar
    mensaje = ""
    color = ""
    
    # AQUI CORREGIMOS: Agregamos el nombre_jugador al mensaje
    if resultado == 0:
        mensaje = "¡Empataste " + nombre_jugador + "!"
        color = "yellow"
        empates += 1
    elif resultado == 1:
        mensaje = "¡Ganaste " + nombre_jugador + "!"
        color = COLOR_BOTONES
        victorias += 1
    else:
        mensaje = "¡Perdiste " + nombre_jugador + "!"
        color = COLOR_ROJO
        derrotas += 1

    # Actualizamos los textos en pantalla
    lbl_pc.config(text="PC eligió: " + texto_pc, fg=COLOR_TITULOS)
    lbl_resultado.config(text=mensaje, fg=color)
    
    texto_marcador = "Ganadas: " + str(victorias) + " | Perdidas: " + str(derrotas) + " | Empates: " + str(empates)
    lbl_stats.config(text=texto_marcador)

def salir():
    ventana.destroy()

# --- Diseño de la Interfaz ---

ventana = tk.Tk()
ventana.title("Piedra, Papel o Tijera")
ventana.geometry("500x500")
ventana.config(bg=COLOR_FONDO)
ventana.resizable(False, False)

# Pantalla de Inicio
frame_inicio = tk.Frame(ventana, bg=COLOR_FONDO)
frame_inicio.pack(expand=True, fill="both")

tk.Label(frame_inicio, text="BIENVENIDO", font=("Arial", 20, "bold"), bg=COLOR_FONDO, fg=COLOR_TITULOS).pack(pady=40)
tk.Label(frame_inicio, text="Ingresa tu nombre:", font=("Arial", 12), bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(pady=10)

entrada_nombre = tk.Entry(frame_inicio, font=("Arial", 14), justify="center")
entrada_nombre.pack(pady=10, ipady=5)

tk.Button(frame_inicio, text="COMENZAR", font=("Arial", 12, "bold"), bg=COLOR_BOTONES, command=iniciar).pack(pady=30)

# Pantalla de Juego (oculta al principio)
frame_juego = tk.Frame(ventana, bg=COLOR_FONDO)

# Encabezado
lbl_jugador = tk.Label(frame_juego, text="Jugador: ", font=("Arial", 12), bg=COLOR_FONDO, fg=COLOR_TEXTO, anchor="w")
lbl_jugador.pack(fill="x")

# Zona de resultados
lbl_pc = tk.Label(frame_juego, text="VS  ?", font=("Arial", 24, "bold"), bg=COLOR_FONDO, fg="#555555")
lbl_pc.pack(pady=30)

lbl_resultado = tk.Label(frame_juego, text="Elige una opción", font=("Arial", 16, "bold"), bg=COLOR_FONDO, fg=COLOR_TEXTO)
lbl_resultado.pack(pady=10)

# Botones para jugar
panel_botones = tk.Frame(frame_juego, bg=COLOR_FONDO)
panel_botones.pack(pady=20)

tk.Button(panel_botones, text="PIEDRA", font=("Arial", 10, "bold"), bg="#333333", fg="white", width=10, height=2, command=lambda: boton_jugar(1)).grid(row=0, column=0, padx=10)
tk.Button(panel_botones, text="PAPEL", font=("Arial", 10, "bold"), bg="#333333", fg="white", width=10, height=2, command=lambda: boton_jugar(2)).grid(row=0, column=1, padx=10)
tk.Button(panel_botones, text="TIJERA", font=("Arial", 10, "bold"), bg="#333333", fg="white", width=10, height=2, command=lambda: boton_jugar(3)).grid(row=0, column=2, padx=10)

# Marcador y Salir
lbl_stats = tk.Label(frame_juego, text="Ganadas: 0 | Perdidas: 0 | Empates: 0", font=("Arial", 10), bg=COLOR_FONDO, fg="#888888")
lbl_stats.pack(side="bottom", pady=10)

tk.Button(frame_juego, text="Salir", bg=COLOR_FONDO, fg=COLOR_ROJO, bd=0, command=salir).place(x=420, y=0)

ventana.mainloop()
