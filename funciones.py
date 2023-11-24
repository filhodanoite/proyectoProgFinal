import tkinter as tk
from PIL import Image, ImageTk
import random

# Definir las listas de clubes por liga
ligas_y_clubes = {
    "Premier League": ["Arsenal", "Aston Villa", "Bournemouth", "Brentford", "Brighton And Hove Albion", "Burnley", "Chelsea", "Crystal Palace", "Everton", "Fulham", "Liverpool", "Luton", "Manchester City", "Manchester United", "Newcastle United", "Nottingham Forest", "Sheffield United", "Tottenham Hotspur", "West Ham United", "Wolverhampton Wanderers"],
    "Bundes Liga": ["FC Augsburg", "Bayer Leverkusen", "FC Bayern München", "VFL Bochum 1848", "Borussia Dortmund", "Borussia Mönchengladbach", "FC Köln", "SV Darmstadt 98", "Eintracht", "Sport-Club Freiburg", "1. FC Heidenheim 1846", "TSG 1899 Hoffenheim","RB Leipzig", "1. FSV Mainz 05", "VFB Stuttgart", "FC Union Berlin", "SV Werder Bremen", "VFL Wolfsburg"],
    "La liga" : ["Athletic Club", "Atletico De Madrid", "CA Osazuna", "Cadiz CF", "Deportivo Alaves", "FC Barcelona", "Getafe CF", "Girona FC", "Granada CF", "Rayo Vallecano", "RC Celta", "Real Betis", "Real Madrid", "Real Sociedad", "Sevilla FC", "UD Almeria", "Valencia CF", "Villareal CF"],
    "Serie A" : ["Atalanta", "Bologna", "Cagliari", "Empoli F.C", "Fiorentina", "Frosinone", "Genoa", "Internazionale", "Juventus", "Lazio", "Lecce", "Milan","Monza","Napoli","Roma","U.S Salernitana 1919","Sassuolo","Torino","Udinese","Verona"],
    "Liga Brasilera" : ["Botafogo","Palmeiras","Grêmio","Flamengo","Bragatino","Fluminense","Atletico PR", "Fortaleza EC", "Atletico MG", "Cuiaba", "Cruzeiro", "Internacional", "São Paulo", "Corinthians", "Bahia", "Goias", " Santos", "Vasco Da Gamma", "America MG", "Coritiba"],
    "Liga Argentina" : ["River Plate", "Talleres (Cordoba)", "San Lorenzo", "Lanus", "Estudiantes De La Plata", "Defensa Y Justicia", "Boca Juniors", "Rosario Central", "Godoy Cruz", "Argentino Juniors", "Atletico Tucuman", "Racing Club", "Belgrano (Cordoba)", "Newell's Old Boys", "Barracas Central", "Tigre", "Instituto (Cordoba)", "Sarmiento (Junin)", "Union (Santa Fe)", "Banfield", "Gimnasia De La Plata", "Central Cordoba (Santiago Del Estero)", "Independiente", "Velez Sarsfield", "Huracan", "Colon (Santa Fe)", "Arsenal Sarandi"]
}

# Función para comenzar el juego con una liga seleccionada
def comenzar_juego():
    selected_liga = liga_var.get()
    if selected_liga:
        clubes = ligas_y_clubes[selected_liga]
        seleccionar_club_random(clubes)

# Función para seleccionar un club al azar y mostrar su escudo y opciones
def seleccionar_club_random(clubes):
    club_elegido = random.choice(clubes)
    # Aquí debes cargar y mostrar la imagen del escudo del club elegido
    imagen_escudo = Image.open(r"/home/alcal/Descargas/jortge/Escudos/{}.png".format(club_elegido))
  # Reemplaza con la ubicación de tus imágenes
    imagen_escudo = imagen_escudo.resize((300, 300))  # Ajusta el tamaño de la imagen según sea necesario
    imagen_escudo = ImageTk.PhotoImage(imagen_escudo)
    
    # Mostrar la imagen del escudo
    escudo_label.config(image=imagen_escudo)
    escudo_label.image = imagen_escudo
    
    # Generar cuatro opciones aleatorias
    opciones = random.sample(clubes, 4)
    opciones.append(club_elegido)
    random.shuffle(opciones)
    
    # Actualizar las etiquetas de las opciones
    for i in range(4):
        opcion_labels[i].config(text=opciones[i])

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Quiz de Fútbol")

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

# Etiquetas para mostrar las opciones
opcion_labels = []
for i in range(4):
    opcion_label = tk.Label(ventana, text="", width=20)
    opcion_label.pack()
    opcion_labels.append(opcion_label)

# Mainloop
ventana.mainloop()