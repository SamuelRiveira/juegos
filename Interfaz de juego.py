import os
import sys
import tkinter as tk
from tkinter import ttk, Button
from PIL import Image, ImageTk
import random

def menu():
    global root
    root = tk.Tk()
    root.resizable(False, False)
    root.title("Menú de juegos")
    archi1 = Image.open("imagenesJuegos/menu.png").resize((700, 700))
    archi1_photo = ImageTk.PhotoImage(archi1)
    canvas1 = tk.Canvas(root, width=700, height=700, background="black")
    canvas1.pack(fill="both", expand=True)
    canvas1.create_image(0, 0, image=archi1_photo, anchor="nw")

    archi12 = Image.open("imagenesJuegos/boton_menu_piedra_papel_tijera.png").resize((260, 100))
    archi12_photo = ImageTk.PhotoImage(archi12)
    botonPiedraPapelTijera = canvas1.create_image(230, 220, anchor="nw", image=archi12_photo)
    canvas1.tag_bind(botonPiedraPapelTijera, "<Button-1>", juego1)

    archi13 = Image.open("imagenesJuegos/boton_adivina_el_numero.png").resize((260, 100))
    archi13_photo = ImageTk.PhotoImage(archi13)
    botonAdivinaElNumero = canvas1.create_image(230, 335, anchor="nw", image=archi13_photo)
    canvas1.tag_bind(botonAdivinaElNumero, "<Button-1>", juego2)

    archi14 = Image.open("imagenesJuegos/boton_traduce_la_palabra.png").resize((260, 100))
    archi14_photo = ImageTk.PhotoImage(archi14)
    botonTraducePalabra = canvas1.create_image(230, 450, anchor="nw", image=archi14_photo)
    canvas1.tag_bind(botonTraducePalabra, "<Button-1>", juego3)

    archi15 = Image.open("imagenesJuegos/boton_salir.png").resize((260, 100))
    archi15_photo = ImageTk.PhotoImage(archi15)
    botonSalir = canvas1.create_image(230, 570, anchor="nw", image=archi15_photo)
    canvas1.tag_bind(botonSalir, "<Button-1>", salir)

    root.mainloop()

def salir(event):
    sys.exit()

def juego1(event):

    root.destroy()
    root3 = tk.Tk()
    root3.resizable(False, False)
    root3.title("Piedra, Papel y Tijera")

    archi4 = Image.open("imagenesJuegos/mesa_piedra_papel_tijera.jpeg").resize((850, 700))
    archi4_photo = ImageTk.PhotoImage(archi4)
    canvas3 = tk.Canvas(root3, width=850, height=700, background="white")
    canvas3.pack(fill="both", expand=True)
    canvas3.create_image(0, 0, image=archi4_photo, anchor="nw")

    archi12 = Image.open("imagenesJuegos/mostrarResultado.png").resize((250, 300))
    archi12_photo = ImageTk.PhotoImage(archi12)
    canvas3.create_image(70, 160, anchor="nw", image=archi12_photo)

    color_fondo = "#e3e3e3"
    resultado_label = ttk.Label(canvas3, text="", font = 30)
    resultado_label.pack()
    resultado_label.config(background=color_fondo)
    canvas3.create_window(140, 280, anchor="nw", window=resultado_label)

    tabla = {
        "piedra": {
            "piedra": 2,
            "papel": 1,
            "tijera": 0
        },
        "papel": {
            "piedra": 0,
            "papel": 2,
            "tijera": 1
        },
        "tijera": {
            "piedra": 1,
            "papel": 0,
            "tijera": 2
        }
    }
    imagenJugador = []
    imagenMaquina = []
    def button_action_piedra(event):
        if imagenJugador != []:
            imagenJugador.pop()
        archi5 = Image.open("imagenesJuegos/piedra.png").resize((200, 200))
        archi5_photo = ImageTk.PhotoImage(archi5)
        imagenJugador.append(archi5_photo)
        canvas3.create_image(320, 320, image=archi5_photo, anchor="nw")
        piedraPapelTijera("piedra")
    def button_action_papel(event):
        if imagenJugador != []:
            imagenJugador.pop()
        archi6 = Image.open("imagenesJuegos/papel.png").resize((200, 200))
        archi6_photo = ImageTk.PhotoImage(archi6)
        imagenJugador.append(archi6_photo)
        canvas3.create_image(320, 320, image=archi6_photo, anchor="nw")
        piedraPapelTijera("papel")
    def button_action_tijera(event):
        if imagenJugador != []:
            imagenJugador.pop()
        archi7 = Image.open("imagenesJuegos/tijera.png").resize((200, 200))
        archi7_photo = ImageTk.PhotoImage(archi7)
        imagenJugador.append(archi7_photo)
        canvas3.create_image(320, 320, image=archi7_photo, anchor="nw")
        piedraPapelTijera("tijera")

    archi8 = Image.open("imagenesJuegos/botonPiedra.png").resize((80, 80))
    archi8_photo = ImageTk.PhotoImage(archi8)
    botonPiedra = canvas3.create_image(260, 580, anchor="nw", image=archi8_photo)
    canvas3.tag_bind(botonPiedra, "<Button-1>", button_action_piedra)

    archi9 = Image.open("imagenesJuegos/botonPapel.png").resize((80, 80))
    archi9_photo = ImageTk.PhotoImage(archi9)
    botonPapel = canvas3.create_image(380, 580, anchor="nw", image=archi9_photo)
    canvas3.tag_bind(botonPapel, "<Button-1>", button_action_papel)

    archi10 = Image.open("imagenesJuegos/botonTijera.png").resize((80, 80))
    archi10_photo = ImageTk.PhotoImage(archi10)
    botonTijera = canvas3.create_image(500, 580, anchor="nw", image=archi10_photo)
    canvas3.tag_bind(botonTijera, "<Button-1>", button_action_tijera)

    archi16 = Image.open("imagenesJuegos/boton_salir2.png").resize((150, 50))
    archi16_photo = ImageTk.PhotoImage(archi16)
    botonSalir = canvas3.create_image(670, 590, anchor="nw", image=archi16_photo)
    canvas3.tag_bind(botonSalir, "<Button-1>", salir)

    def jugar(opcionJugador, opcionMaquina):
        return tabla[opcionJugador][opcionMaquina]

    def piedraPapelTijera(opcionJugador):

        opcionMaquina = random.choice(list(tabla.keys()))

        if imagenMaquina != []:
            imagenMaquina.pop()
        imagen = opcionMaquina + ".png"
        image_folder = "imagenesJuegos"
        image_path = os.path.join(image_folder, imagen)
        archi11 = Image.open(image_path).resize((200, 200))
        archi11_rotada = archi11.rotate(180)
        archi11_photo = ImageTk.PhotoImage(archi11_rotada)
        imagenMaquina.append(archi11_photo)
        canvas3.create_image(320, 120, image=archi11_photo, anchor="nw")

        resultadoJuego = jugar(opcionJugador, opcionMaquina)
        if (resultadoJuego == 0):
            resultado_label.config(text= "Ha ganado\nel jugador")
        elif (resultadoJuego == 1):
            resultado_label.config(text= "Ha perdido\nel jugador")
        elif (resultadoJuego == 2):
            resultado_label.config(text= "Hubo un\nempate")

    root3.mainloop()

def juego2(event):
    root.destroy()
    root2 = tk.Tk()
    root2.resizable(False, False)
    root2.title("Adivina el número")

    archi2 = Image.open("imagenesJuegos/adivinarNumero.jpeg").resize((850, 700))
    archi2_photo = ImageTk.PhotoImage(archi2)
    canvas2 = tk.Canvas(root2, width=850, height=700, background="black")
    canvas2.pack(fill="both", expand=True)
    canvas2.create_image(0, 0, image=archi2_photo, anchor="nw")

    intentos = 4
    numeroEscogido = tk.StringVar()


    numeroAleatorio = random.randint(0, 200)
    print(numeroAleatorio)

    def comprobar_numero():
        nonlocal intentos
        try:
            numeroEscogidoValue = int(input_entry.get())
            numeroEscogido.set(numeroEscogidoValue)
        except ValueError:
            resultado_label.config(text="Por favor, ingresa un número válido.")
            return

        if numeroEscogidoValue > numeroAleatorio:
            pista = "menor"
        elif numeroEscogidoValue < numeroAleatorio:
            pista = "mayor"
        else:
            resultado_label.config(text=f"¡Has ganado! El número es el {numeroAleatorio}.")
            comprobar["state"] = tk.DISABLED
            return

        if intentos == 0:
            resultado_label.config(text=f"Has perdido. El número era {numeroAleatorio}.")
            comprobar["state"] = tk.DISABLED
            return
        intentos -= 1

        resultado_label.config(text=f"Pista: {pista}. Te quedan {intentos} intentos.")


    input_entry = tk.Entry(canvas2)
    input_entry.pack()
    canvas2.create_window(350, 160, anchor="nw", window=input_entry)

    archi3 = Image.open("imagenesJuegos/cuadro.jpg").resize((180, 180))
    archi3_photo = ImageTk.PhotoImage(archi3)
    canvas2.create_image(160, 120, image=archi3_photo, anchor="nw")

    color_fondo = "#FFFFFF"

    comprobar = tk.Button(root2, text="Comprobar", bd=0, highlightthickness=0, bg=color_fondo, command=comprobar_numero)
    comprobar.pack()
    canvas2.create_window(203, 210, anchor="nw", window=comprobar)


    resultado_label = ttk.Label(canvas2, text="")
    resultado_label.pack()
    resultado_label.config(background= color_fondo)
    canvas2.create_window(350, 200, anchor="nw", window=resultado_label)

    titulo_label = ttk.Label(canvas2, text="Adivina un número del 0 al 200", font = ("Helvetica", 20))
    titulo_label.pack()
    titulo_label.config(background=color_fondo)
    canvas2.create_window(220, 100, anchor="nw", window=titulo_label)

    archi17 = Image.open("imagenesJuegos/boton_salir2.png").resize((150, 50))
    archi17_photo = ImageTk.PhotoImage(archi17)
    botonSalir = canvas2.create_image(670, 590, anchor="nw", image=archi17_photo)
    canvas2.tag_bind(botonSalir, "<Button-1>", salir)

    root2.mainloop()

def juego3(event):
    def verificar_respuesta(opcion, correcta, puntos, indexOpcion, contador):
        for widget in canvas4.winfo_children():
            widget.destroy()

        if opcion == correcta:
            puntos += 1
            contador += 1
        else:
            contador += 1

        if contador == 5:
            mostrar_resultado(puntos)
        else:
            indexOpcion += 1
            mostrar_palabra(puntos, indexOpcion, contador)

    def mostrar_palabra(puntos, indexOpcion, contador):

        palabraAdivinar = random.choice(list(palabras.keys()))
        correcta = palabras[palabraAdivinar]

        opciones_incorrectas = []

        for key, value in palabras.items():
            if value != correcta:
                opciones_incorrectas.append(value)

        incorrecta1 = random.choice(opciones_incorrectas)
        opciones_incorrectas.remove(incorrecta1)
        incorrecta2 = random.choice(opciones_incorrectas)

        enunciado = ttk.Label(canvas4, text=palabraAdivinar, background="white", font=20)
        canvas4.create_window(135, 120, anchor="nw", window=enunciado)

        opcion_label1 = ttk.Label(canvas4, text=correcta, background="white", font=20)
        canvas4.create_window(550, 70, anchor="nw", window=opcion_label1)
        opcion_label1.bind("<Button-1>", lambda event: verificar_respuesta(correcta, correcta, puntos, indexOpcion, contador))

        opcion_label2 = ttk.Label(canvas4, text=incorrecta1, background="white", font=20)
        canvas4.create_window(550, 120, anchor="nw", window=opcion_label2)
        opcion_label2.bind("<Button-1>", lambda event: verificar_respuesta(incorrecta1, correcta, puntos, indexOpcion, contador))

        opcion_label3 = ttk.Label(canvas4, text=incorrecta2, background="white", font=20)
        canvas4.create_window(550, 170, anchor="nw", window=opcion_label3)
        opcion_label3.bind("<Button-1>", lambda event: verificar_respuesta(incorrecta2, correcta, puntos, indexOpcion, contador))

    def mostrar_resultado(puntos):
        for widget in canvas4.winfo_children():
            widget.destroy()
        enunciado = ttk.Label(canvas4, text=f"Has obtenido {puntos} puntos", background="white", font=20)
        canvas4.create_window(80, 120, anchor="nw", window=enunciado)

    puntos = 0
    indexOpcion = 0
    contador = 0

    root.destroy()
    root4 = tk.Tk()
    root4.resizable(False, False)
    root4.title("Traduce la palabra")

    archi14 = Image.open("imagenesJuegos/charla.jpeg").resize((850, 700))
    archi14_photo = ImageTk.PhotoImage(archi14)
    canvas4 = tk.Canvas(root4, width=850, height=700, background="white")
    canvas4.pack(fill="both", expand=True)
    canvas4.create_image(0, 0, image=archi14_photo, anchor="nw")

    archi15 = Image.open("imagenesJuegos/traducir_palabra.png").resize((200, 50))
    archi15_photo = ImageTk.PhotoImage(archi15)
    canvas4.create_image(300, 250, image=archi15_photo, anchor="nw")

    archi18 = Image.open("imagenesJuegos/boton_salir2.png").resize((150, 50))
    archi18_photo = ImageTk.PhotoImage(archi18)
    botonSalir = canvas4.create_image(670, 590, anchor="nw", image=archi18_photo)
    canvas4.tag_bind(botonSalir, "<Button-1>", salir)

    palabras = {
        "Hello": "Hola",
        "World": "Mundo",
        "Cat": "Gato",
        "Dog": "Perro",
        "Fish": "Pez",
        "Bird": "Pájaro",
        "Programming": "Programación",
        "Language": "Lenguaje",
        "Developer": "Desarrollador",
        "Carpet": "Alfombra",
        "Apple": "Manzana",
        "Orange": "Naranja",
        "Banana": "Plátano",
        "Water": "Agua",
        "Chair": "Silla",
        "Window": "Ventana",
        "Sun": "Sol",
        "Mountain": "Montaña",
        "Friend": "Amigo",
        "Pencil": "Lápiz"
    }

    mostrar_palabra(puntos, indexOpcion, contador)
    root4.mainloop()

if __name__ == "__main__":
    menu()
