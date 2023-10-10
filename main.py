import tkinter as tk
from PIL import Image, ImageTk
import random

# Variable global para la ventana principal
ventana = tk.Tk()
ventana.title("Quiz de Fútbol")

# Variable global para rastrear si se ha mostrado el mensaje en la liga actual
mensaje_mostrado = False

# Definir las listas de clubes por liga
opciones = []
clubes = []
ligas_y_clubes = {
  "Premier League": ["Arsenal", "Aston Villa", "Bournemouth", "Brentford", "Brighton And Hove Albion", "Burnley", "Chelsea", "Crystal Palace", "Everton", "Fulham", "Liverpool", "Luton", "Manchester City", "Manchester United", "Newcastle United", "Nottingham Forest", "Sheffield United", "Tottenham Hotspur", "West Ham United", "Wolverhampton Wanderers"],
  "Bundes Liga": ["FC Augsburg", "Bayer Leverkusen", "FC Bayern München", "VFL Bochum 1848", "Borussia Dortmund", "Borussia Mönchengladbach", "FC Köln", "SV Darmstadt 98", "Eintracht", "Sport-Club Freiburg", "1. FC Heidenheim 1846", "TSG 1899 Hoffenheim","RB Leipzig", "1. FSV Mainz 05", "VFB Stuttgart", "FC Union Berlin", "SV Werder Bremen", "VFL Wolfsburg"],
  "La liga" : ["Athletic Club", "Atletico Madrid", "CA Osazuna", "Cadiz CF", "Deportivo Alaves", "FC Barcelona", "Getafe CF", "Girona FC", "Granada CF", "Rayo Vallecano", "RC Celta", "Real Betis", "Real Madrid", "Real Sociedad", "Sevilla FC", "UD Almeria", "Valencia CF", "Villareal CF"],
  "Serie A" : ["Atalanta", "Bologna", "Cagliari", "Empoli F.C", "Fiorentina", "Frosinone", "Genoa", "Internazionale", "Juventus", "Lazio", "Lecce", "Milan","Monza","Napoli","Roma","U.S Salernitana 1919","Sassuolo","Torino","Udinese","Verona"],
  "Liga Brasilera" : ["Botafogo","Palmeiras","Grêmio","Flamengo","Bragantino","Fluminense","Atletico PR", "Fortaleza EC", "Atletico MG", "Cuiaba", "Cruzeiro", "Internacional", "São Paulo", "Corinthians", "Bahia", "Goias", "Santos", "Vasco Da Gamma", "America MG", "Coritiba"],
  "Liga Argentina" : ["River Plate", "Talleres (Cordoba)", "San Lorenzo", "Lanus", "Estudiantes De La Plata", "Defensa Y Justicia", "Boca Juniors", "Rosario Central", "Godoy Cruz", "Argentinos Juniors", "Atletico Tucuman", "Racing Club", "Belgrano (Cordoba)", "Newell's Old Boys", "Barracas Central", "Tigre", "Instituto (Cordoba)", "Sarmiento (Junin)", "Union (Santa Fe)", "Banfield", "Gimnasia De La Plata", "Central Cordoba (Santiago Del Estero)", "Independiente", "Velez Sarsfield", "Huracan", "Colon (Santa Fe)", "Arsenal Sarandi", "Platense"]
}

# Funciones
def comenzar_juego():
    selected_liga = liga_var.get()
    if selected_liga:
        global clubes, opciones, club_elegido, mensaje_mostrado
        if mensaje_mostrado:
            mensaje_label.config(text="")  # Borra el mensaje si se mostró anteriormente
        clubes = ligas_y_clubes[selected_liga]
        mensaje_mostrado = False  # Restablecer la variable mensaje_mostrado
        seleccionar_club_random(clubes)


def verificar_respuesta(respuesta):
   global club_elegido  # Hacer que 'club_elegido' sea global
   if respuesta == club_elegido:
       resultado.config(text="¡Correcto!", bg="green")
   else:
       resultado.config(text="Incorrecto. La respuesta correcta es: {}".format(club_elegido), bg="red")
   ventana.after(1500, ocultar_resultado)


def ocultar_resultado():
  resultado.config(text="")
  seleccionar_club_random(clubes)

# Etiqueta para mostrar el mensaje
mensaje_label = tk.Label(ventana, text="")
mensaje_label.pack()

# Función para mostrar el mensaje cuando se hayan mostrado todos los escudos
def mostrar_mensaje_final():
    mensaje_label.config(text="Se han mostrado todos los escudos.")

# Modifica la función seleccionar_club_random()
def seleccionar_club_random(clubes):
    global mensaje_mostrado  # Hacer que 'mensaje_mostrado' sea global
    if not clubes:
        if not mensaje_mostrado:
            mostrar_mensaje_final()
            mensaje_mostrado = True  # Marcar que se ha mostrado el mensaje en esta liga
        return

    global opciones, club_elegido  # Hacer que 'opciones' y 'club_elegido' sean globales
    club_elegido = random.choice(clubes)
    clubes.remove(club_elegido)

    imagen_escudo = Image.open("{}.png".format(club_elegido))
    imagen_escudo = imagen_escudo.resize((300, 300))
    imagen_escudo = ImageTk.PhotoImage(imagen_escudo)
    escudo_label.config(image=imagen_escudo)
    escudo_label.image = imagen_escudo

    opciones = random.sample(clubes, 3)
    opciones.insert(random.randint(0, 3), club_elegido)
    random.shuffle(opciones)

    for i in range(4):
        opcion_botones[i].config(text=opciones[i])

# Función para mostrar el mensaje cuando se hayan mostrado todos los escudos
def mostrar_mensaje_final():
    global mensaje_mostrado
    mensaje_label.config(text="Se han mostrado todos los escudos.")
    mensaje_mostrado = True
    
# Etiqueta para seleccionar la liga
etiqueta_liga = tk.Label(ventana, text="Selecciona una liga:")
etiqueta_liga.pack()


# Variable para almacenar la liga seleccionada
liga_var = tk.StringVar()
liga_var.set("Premier League")  # Valor predeterminado


# Menú desplegable para seleccionar la liga
menu_ligas = tk.OptionMenu(ventana, liga_var, *ligas_y_clubes.keys())
menu_ligas.pack()


# Botón para comenzar el juego
boton_comenzar = tk.Button(ventana, text="Comenzar Juego", command=comenzar_juego)
boton_comenzar.pack()


# Etiqueta para mostrar el escudo del club
escudo_label = tk.Label(ventana)
escudo_label.pack()


# Botones para las opciones
opcion_botones = []
for i in range(4):
  opcion_boton = tk.Button(ventana, text="", width=40, command=lambda i=i: verificar_respuesta(opciones[i]))
  opcion_boton.pack()
  opcion_botones.append(opcion_boton)


# Etiqueta para mostrar el resultado
resultado = tk.Label(ventana, text="")
resultado.pack()


# Etiqueta para mostrar el mensaje "Se han mostrado todos los escudos."
mensaje_label = tk.Label(ventana, text="")
mensaje_label.pack()


# Mainloop
ventana.mainloop()