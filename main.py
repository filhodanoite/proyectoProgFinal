import tkinter as tk
from PIL import Image, ImageTk
import random


ventana = tk.Tk()
ventana.title("Quiz de Fútbol")


clubes = []
opciones = []
club_elegido = None
puntaje = 0
vidas = 3  # Inicialmente, el jugador tiene 3 vidas
puntaje_total = 0  # Inicialmente, el puntaje total es 0


ligas_y_clubes = {
  "Premier League": ["Arsenal", "Aston Villa", "Bournemouth", "Brentford", "Brighton And Hove Albion", "Burnley", "Chelsea", "Crystal Palace", "Everton", "Fulham", "Liverpool", "Luton", "Manchester City", "Manchester United", "Newcastle United", "Nottingham Forest", "Sheffield United", "Tottenham Hotspur", "West Ham United", "Wolverhampton Wanderers"],
  "Bundes Liga": ["FC Augsburg", "Bayer Leverkusen", "FC Bayern München", "VFL Bochum 1848", "Borussia Dortmund", "Borussia Mönchengladbach", "FC Köln", "SV Darmstadt 98", "Eintracht", "Sport-Club Freiburg", "1. FC Heidenheim 1846", "TSG 1899 Hoffenheim", "RB Leipzig", "1. FSV Mainz 05", "VFB Stuttgart", "FC Union Berlin", "SV Werder Bremen", "VFL Wolfsburg"],
  "La liga": ["Athletic Club", "Atletico Madrid", "CA Osazuna", "Cadiz CF", "Deportivo Alaves", "FC Barcelona", "Getafe CF", "Girona FC", "Granada CF", "Rayo Vallecano", "RC Celta", "Real Betis", "Real Madrid", "Real Sociedad", "Sevilla FC", "UD Almeria", "Valencia CF", "Villareal CF"],
  "Serie A": ["Atalanta", "Bologna", "Cagliari", "Empoli F.C", "Fiorentina", "Frosinone", "Genoa", "Internazionale", "Juventus", "Lazio", "Lecce", "Milan", "Monza", "Napoli", "Roma", "U.S Salernitana 1919", "Sassuolo", "Torino", "Udinese", "Verona"],
  "Liga Brasilera": ["Botafogo", "Palmeiras", "Grêmio", "Flamengo", "Bragantino", "Fluminense", "Atletico PR", "Fortaleza EC", "Atletico MG", "Cuiaba", "Cruzeiro", "Internacional", "São Paulo", "Corinthians", "Bahia", "Goias", "Santos", "Vasco Da Gamma", "America MG", "Coritiba"],
  "Liga Argentina": ["River Plate", "Talleres (Cordoba)", "San Lorenzo", "Lanus", "Estudiantes De La Plata", "Defensa Y Justicia", "Boca Juniors", "Rosario Central", "Godoy Cruz", "Argentinos Juniors", "Atletico Tucuman", "Racing Club", "Belgrano (Cordoba)", "Newell's Old Boys", "Barracas Central", "Tigre", "Instituto (Cordoba)", "Sarmiento (Junin)", "Union (Santa Fe)", "Banfield", "Gimnasia De La Plata", "Central Cordoba (Santiago Del Estero)", "Independiente", "Velez Sarsfield", "Huracan", "Colon (Santa Fe)", "Arsenal Sarandi", "Platense"]
}


def comenzar_juego():
  global clubes, opciones, club_elegido, puntaje
  liga_seleccionada = liga_var.get()
  if liga_seleccionada in ligas_y_clubes:
      mensaje_label.config(text="")
      clubes = ligas_y_clubes[liga_seleccionada]
      puntaje = 0
      seleccionar_club_random()
  else:
      mensaje_label.config(text="Selecciona una liga válida")


def seleccionar_club_random():
  global club_elegido, opciones
  if not clubes:
      mostrar_mensaje_final()
      return

  if len(clubes) >= 4:
      club_elegido = random.choice(clubes)
      clubes.remove(club_elegido)
      opciones = [club_elegido] + random.sample(clubes, 3)
  else:
      # Maneja el caso en el que no haya suficientes clubes para seleccionar
      mostrar_mensaje_final()

  random.shuffle(opciones)

  for i, boton in enumerate(botones_respuesta):
      boton.config(text=opciones[i])

  escudo_path = "{}.png".format(club_elegido)
  imagen_escudo = Image.open(r"/home/alcal/Escritorio/TrabajoProgramacion/Escudos/{}.png".format(club_elegido))
  imagen_escudo = imagen_escudo.resize((300, 300))
  imagen_escudo = ImageTk.PhotoImage(imagen_escudo)
  escudo_label.config(image=imagen_escudo)
  escudo_label.image = imagen_escudo

def verificar_respuesta(respuesta):
  global puntaje_total, vidas, opciones
  if vidas > 0:
      if respuesta == club_elegido:
          puntaje_total += 1
          resultado.config(text="¡Correcto! Puntaje: {}".format(puntaje_total), bg="green")
      else:
          vidas -= 1
          if vidas == 0:
              mostrar_puntaje_final()
              for boton in botones_respuesta:
                  boton.config(state=tk.DISABLED)
              opciones = []  # Borramos las opciones al quedarse sin vidas
          else:
              resultado.config(text="Incorrecto. La respuesta correcta es: {}".format(club_elegido), bg="red")
              if vidas >= 2:
                  mensaje_label.config(text="Tienes {} vidas restantes.".format(vidas))
              elif vidas == 1:
                  mensaje_label.config(text="Tienes {} vida restante.".format(vidas))
                 
      for boton in botones_respuesta:
          boton.config(state=tk.DISABLED)




      ventana.after(1500, ocultar_resultado)
  ventana.after(1500, ocultar_resultado)


def ocultar_resultado():
   resultado.config(text="")
   if vidas > 0:
       for boton in botones_respuesta:
           boton.config(state=tk.NORMAL)  # Habilita las opciones de respuesta
       seleccionar_club_random()
   else:
       mostrar_puntaje_final()


def mostrar_puntaje_final():
  mensaje_label.config(text="Juego terminado. Puntaje total: {}".format(puntaje_total))
  
def mostrar_mensaje_final():
    mensaje_label.config(text="Has visto todos los escudos en esta liga.")
    for boton in botones_respuesta:
          boton.config(state=tk.DISABLED)


def mostrar_tutorial():
  tutorial_ventana = tk.Toplevel(ventana)
  tutorial_ventana.title("Tutorial")




  tutorial_contenido = """
  **Tutorial del Juego de Fútbol**




  Bienvenido al juego de adivinanza de escudos de fútbol. El objetivo del juego es adivinar a qué club de fútbol pertenece el escudo que se muestra en la pantalla.




  - Selecciona una liga de fútbol en el menú desplegable.
  - Haz clic en el botón 'Comenzar Juego' para iniciar.
  - Observa el escudo del club y elige la respuesta correcta entre las opciones disponibles.
  - Tu puntaje aumentará si la respuesta es correcta, y perderás vidas si la respuesta es incorrecta.
  - El juego terminará cuando te quedes sin vidas o hayas adivinado todos los escudos de la liga seleccionada.
  - Puedes ver tu puntaje total al final del juego.




  ¡Diviértete y demuestra cuánto sabes sobre los clubes de fútbol!




  """
 
  tutorial_texto = tk.Label(tutorial_ventana, text=tutorial_contenido, justify="left")
  tutorial_texto.pack()


etiqueta_liga = tk.Label(ventana, text="Selecciona una liga:")
etiqueta_liga.pack()


liga_var = tk.StringVar()
liga_var.set("Premier League")
menu_ligas = tk.OptionMenu(ventana, liga_var, *ligas_y_clubes.keys())
menu_ligas.pack()


boton_comenzar = tk.Button(ventana, text="Comenzar Juego", command=comenzar_juego)
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


mensaje_label = tk.Label(ventana, text="")
mensaje_label.pack()


boton_ver_tutorial = tk.Button(ventana, text="Ver Tutorial", command=mostrar_tutorial)
boton_ver_tutorial.pack()


ventana.mainloop()

