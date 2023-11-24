import tkinter as tk
from PIL import Image, ImageTk
import random
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Quiz de Fútbol")

clubes = []
opciones = []
club_elegido = None
puntaje_total = 0
puntaje_acumulado = 0
vidas = 3
vidas_generales = 3
ligas_jugadas = set()


ruta_imagenes = "/home/alcal/Descargas/progFinal/Escudos/"

ligas_y_clubes = {
    "Premier League": ["Arsenal", "Aston Villa", "Bournemouth", "Brentford", "Brighton And Hove Albion", "Burnley", "Chelsea", "Crystal Palace", "Everton", "Fulham", "Liverpool", "Luton", "Manchester City", "Manchester United", "Newcastle United", "Nottingham Forest", "Sheffield United", "Tottenham Hotspur", "West Ham United", "Wolverhampton Wanderers",],
    "Bundes Liga": ["FC Augsburg", "Bayer Leverkusen", "FC Bayern Munchen", "VFL Bochum 1848", "Borussia Dortmund", "Borussia Monchegladbach", "FC Koln", "SV Darmstadt 98", "Eintracht", "Sport-Club Freiburg", "1. FC Heidenheim 1846", "TSG 1899 Hoffenheim","RB Leipzig", "1. FSV Mainz 05", "VFB Stuttgart", "FC Union Berlin", "SV Werder Bremen", "VFL Wolfsburg"],
    "La liga" : ["Athletic Club", "Atletico Madrid", "CA Osazuna", "Cadiz CF", "Deportivo Alaves", "FC Barcelona", "Getafe CF", "Girona FC", "Granada CF", "Rayo Vallecano", "RC Celta", "Real Betis", "Real Madrid", "Real Sociedad", "Sevilla FC", "UD Almeria", "Valencia CF", "Villareal CF"],
    "Serie A" : ["Atalanta", "Bologna", "Cagliari", "Empoli F.C", "Fiorentina", "Frosinone", "Genoa", "Internazionale", "Juventus", "Lazio", "Lecce", "Milan","Monza","Napoli","Roma","U.S Salernitana 1919","Sassuolo","Torino","Udinese","Verona"],
    "Liga Brasilera" : ["Botafogo","Palmeiras","Gremio","Flamengo","Bragantino","Fluminense","Atletico PR", "Fortaleza EC", "Atletico MG", "Cuiaba", "Cruzeiro", "Internacional", "Sao Paulo", "Corinthians", "Bahia", "Goias", "Santos", "Vasco Da Gamma", "America MG", "Coritiba"],
    "Liga Argentina" : ["River Plate", "Talleres (Cordoba)", "San Lorenzo", "Lanus", "Estudiantes De La Plata", "Defensa Y Justicia", "Boca Juniors", "Rosario Central", "Godoy Cruz", "Argentinos Juniors", "Atletico Tucuman", "Racing Club", "Belgrano (Cordoba)", "Newells Old Boys", "Barracas Central", "Tigre", "Instituto (Cordoba)", "Sarmiento (Junin)", "Union (Santa Fe)", "Banfield", "Gimnasia De La Plata", "Central Cordoba (Santiago Del Estero)", "Independiente", "Velez Sarsfield", "Huracan", "Colon (Santa Fe)", "Arsenal Sarandi"]
}


def iniciar_juego(liga_seleccionada):
    global clubes, opciones, club_elegido, puntaje_total, vidas, vidas_generales, puntaje_acumulado, ligas_jugadas
    resultado.config(text="")
    
    if not hay_mas_ligas():
        messagebox.showinfo("Fin del Juego", f"Sos la máquina, chabón. Puntaje acumulado: {puntaje_acumulado}")
        ventana.destroy()
        return

    if liga_seleccionada in ligas_jugadas:
        messagebox.showinfo("Liga Jugada", "Ya has jugado esta liga. Selecciona otra.")
        return

    mensaje_label.config(text="")
    clubes = ligas_y_clubes[liga_seleccionada].copy()
    vidas = vidas_generales
    seleccionar_club_random()
    
    for boton in botones_respuesta:
        boton.config(state=tk.NORMAL)

    ligas_jugadas.add(liga_seleccionada)



def seleccionar_club_random():
    global clubes, club_elegido, opciones, ruta_imagenes

    if not clubes:
        mostrar_mensaje_final()
        return

    club_elegido = random.choice(clubes)
    clubes.remove(club_elegido)
    
    if len(clubes) >= 3:
        opciones = [club_elegido] + random.sample(clubes, 3)

    random.shuffle(opciones)

    # Asegurémonos de tener al menos 4 opciones
    opciones += ["" for _ in range(4 - len(opciones))]

    for i, boton in enumerate(botones_respuesta):
        boton.config(text=opciones[i])

    escudo_path = "{}{}.png".format(ruta_imagenes, club_elegido)
    try:
        imagen_escudo = Image.open(escudo_path)
        imagen_escudo = imagen_escudo.resize((300, 300))
        imagen_escudo = ImageTk.PhotoImage(imagen_escudo)
        escudo_label.config(image=imagen_escudo)
        escudo_label.image = imagen_escudo
    except FileNotFoundError:
        print(f"Imagen no encontrada para {club_elegido} en la ruta {escudo_path}")

def verificar_respuesta(respuesta):
    global puntaje_total, vidas, vidas_generales, puntaje_acumulado, opciones, club_elegido
    if vidas > 0:
        if respuesta == club_elegido:
            puntaje_total += 1
            resultado.config(text="¡Correcto! Puntaje: {}".format(puntaje_total), bg="green")
        else:
            vidas -= 1
            vidas_generales -= 1  # Reducir las vidas generales
            if vidas_generales == 0:
                mostrar_puntaje_final()
                for boton in botones_respuesta:
                    boton.config(state=tk.DISABLED)
                opciones = []  # Borramos las opciones al quedarse sin vidas generales
            else:
                resultado.config(text="Incorrecto. La respuesta correcta es: {}".format(club_elegido), bg="red")
                mensaje_label.config(text="Tienes {} vidas restantes.".format(vidas_generales))

        for boton in botones_respuesta:
            boton.config(state=tk.DISABLED)

        ventana.after(1200, ocultar_resultado)

def ocultar_resultado():
    resultado.config(text="")
    if vidas > 0:
        for boton in botones_respuesta:
            boton.config(state=tk.NORMAL)
        seleccionar_club_random()
    else:
        mostrar_puntaje_final()

def mostrar_puntaje_final():
    mensaje = "Juego terminado. Puntaje total: {}".format(puntaje_total)
    messagebox.showinfo("Fin del Juego", mensaje)
    reiniciar_juego()

def reiniciar_juego():
    global puntaje_total, vidas_generales, puntaje_acumulado, ligas_jugadas
    vidas_generales = 3
    puntaje_acumulado += puntaje_total
    puntaje_total = 0
    liga_var.set(liga_var.get())
    mensaje_label.config(text="")
    
    for boton in botones_respuesta:
        boton.config(state=tk.NORMAL)

    reiniciar = messagebox.askquestion("Fin del Juego", "¿Quieres jugar de nuevo?", icon='question')

    if reiniciar == 'yes':
        iniciar_juego(liga_var.get())
    else:
        # Limpiar el conjunto de ligas jugadas
        ligas_jugadas.clear()
        ventana.destroy()

def hay_mas_ligas():
    return len(ligas_y_clubes.keys() - ligas_jugadas) > 0

def mostrar_mensaje_final():
    global puntaje_acumulado
    mensaje_label.config(text="Has visto todos los escudos de esta liga (si deseas puedes elegir otra) . Puntaje total: {}".format(puntaje_total))
    for boton in botones_respuesta:
        boton.config(state=tk.DISABLED)

def mostrar_tutorial():
    tutorial_texto = """
    Bienvenido al Quiz de Fútbol:

    - Selecciona una liga en el menú desplegable.
    
    - Haz clic en 'Comenzar Juego' para iniciar.

    - Se mostrará el escudo de un club, y debes elegir el nombre correcto entre las opciones.

    - Tienes vidas, y perderás una si te equivocas.

    - Puedes ver tu puntaje total y las vidas restantes.

    - Si decides salir o perder todas las vidas, puedes reiniciar el juego.

    ¡Diviértete y buena suerte!
    """

    tutorial_font = ("Arial", 14)  # Cambia el tamaño de la fuente según tus preferencias

    # Crear una ventana emergente personalizada para el tutorial
    ventana_tutorial = tk.Toplevel(ventana)
    ventana_tutorial.title("Tutorial")

    # Crear una etiqueta con el texto del tutorial y aplicar la fuente
    label_tutorial = tk.Label(ventana_tutorial, text=tutorial_texto, font=tutorial_font, padx=20, pady=20)
    label_tutorial.pack()

etiqueta_liga = tk.Label(ventana, text="Selecciona una liga:")
etiqueta_liga.pack()

liga_var = tk.StringVar()
liga_var.set("Premier League")
menu_ligas = tk.OptionMenu(ventana, liga_var, *ligas_y_clubes.keys())
menu_ligas.pack()

boton_comenzar = tk.Button(ventana, text="Comenzar Juego", command=lambda: iniciar_juego(liga_var.get()))
boton_comenzar.pack()

escudo_label = tk.Label(ventana)
escudo_label.pack()

botones_respuesta = []
for i in range(4):
    opcion_boton = tk.Button(ventana, text="", width=40, command=lambda i=i: verificar_respuesta(opciones[i]))
    opcion_boton.pack()
    botones_respuesta.append(opcion_boton)

resultado = tk.Label(ventana, text="")
resultado.pack()

boton_tutorial = tk.Button(ventana, text="Tutorial", command=mostrar_tutorial)
boton_tutorial.pack(side=tk.BOTTOM)

mensaje_label = tk.Label(ventana, text="")
mensaje_label.pack()

ventana.mainloop()