# PROYECTO FINAL: PIEDRA, PAPEL O TIJERA (V2.0 CON INTERFAZ)
DESCRIPCIÓN: Evolución del proyecto clásico de consola a una aplicación de escritorio completa. El programa ahora cuenta con una interfaz gráfica (GUI) moderna, navegación entre pantallas (Login -> Juego) y marcadores en tiempo real.

# HERRAMIENTAS Y TECNOLOGÍAS:

Lenguaje: Python 3.

Interfaz: Librería tkinter (Investigación propia para la Unidad 4).

Lógica: Librería random.

Diseño Lógico: Bizagi / Raptor.

# INTEGRACIÓN DE LAS 4 UNIDADES (CAMBIOS TÉCNICOS): Para cumplir con la rúbrica final, reestructuré todo el código antiguo:

De input a Entry (Unidad 2): Ya no uso la consola para pedir el nombre. Creé una pantalla de inicio con una caja de texto (Entry) y validación de usuario.

De print a Label (Unidad 2): Los resultados ya no se imprimen línea por línea; ahora actualizo etiquetas visuales en la ventana.

Tuplas (Unidad 3): Implementé la tupla OPCIONES = ("Piedra", "Papel", "Tijera") para manejar datos fijos e inmutables.

Modularización (Unidad 4): El código antiguo era un bloque único. El nuevo usa funciones separadas (turno_pc, calcular_ganador) para organizar la lógica, separando el "backend" (cálculos) del "frontend" (visual).

# CÓMO EJECUTAR:

Abrir juego_gui.py en Visual Studio Code.

Dar clic en "Run".

Ingresar nombre en la ventana negra y jugar.
