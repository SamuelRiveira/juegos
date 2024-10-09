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

    color_fondo = "#f3c496"
    color_texto = "#FFFFFF"

    boton1 = tk.Button(root, text="Piedra, Papel, Tijera", bd=0, highlightthickness=0, fg=color_texto, bg=color_fondo, command=juego1)
    canvas1.create_window(320, 255, anchor="nw", window=boton1)

    boton2 = tk.Button(root, text="Adivina el número", bd=0, highlightthickness=0, fg=color_texto, bg=color_fondo, command=juego2)
    canvas1.create_window(320, 370, anchor="nw", window=boton2)

    boton3 = tk.Button(root, text="Traduce la palabra", bd=0, highlightthickness=0, fg=color_texto, bg=color_fondo, command=juego3)
    canvas1.create_window(320, 490, anchor="nw", window=boton3)

    boton4 = tk.Button(root, text="Salir", bd=0, highlightthickness=0, fg=color_texto, bg=color_fondo, command=quit)
    canvas1.create_window(360, 605, anchor="nw", window=boton4)

    root.mainloop()


def juego1():
    root.destroy()
    root2 = tk.Tk()
    root2.resizable(False, False)
    root2.title("Piedra, Papel y Tijera")


def juego2():
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

    root2.mainloop()


def juego3(event):
    def verificar_respuesta(opcion, correcta, puntos, indexOpcion):

        if opcion == correcta:
            print("\nCorrecto")
            puntos += 1
        else:
            print(f"Incorrecto. La respuesta correcta era: {correcta}")

        indexOpcion += 1
        if indexOpcion < 5:
            mostrar_palabra(puntos, indexOpcion)
        else:
            print(f"\nHas obtenido {puntos} puntos")
            print("\nVolviendo al menú")
            root4.quit()

    def mostrar_palabra(puntos, indexOpcion):
        color_fondo = "#FFFFFF"

        palabraAdivinar = random.choice(list(palabras.keys()))
        print(palabraAdivinar)
        correcta = palabras[palabraAdivinar]

        opcion_label1 = ttk.Label(canvas4, text=correcta)
        opcion_label1.pack()
        canvas4.create_window(350, 200, anchor="nw", window=opcion_label1)
        opcion_label1.bind("<Button-1>", lambda event: verificar_respuesta(correcta, correcta, puntos, indexOpcion))


        opcion_label2 = ttk.Label(canvas4, text=random.choice(list(palabras.values())))
        opcion_label2.pack()
        opcion_label2.config(background=color_fondo)
        canvas4.create_window(450, 200, anchor="nw", window=opcion_label2)
        opcion_label2.bind("<Button-1>", lambda event: verificar_respuesta(random.choice(list(palabras.values())), puntos, indexOpcion))

        opcion_label3 = ttk.Label(canvas4, text=random.choice(list(palabras.values())))
        opcion_label3.pack()
        opcion_label3.config(background=color_fondo)
        canvas4.create_window(550, 200, anchor="nw", window=opcion_label3)
        opcion_label2.bind("<Button-1>", lambda event: verificar_respuesta(random.choice(list(palabras.values())), correcta, puntos, indexOpcion))

    puntos = tk.StringVar()
    puntos = 0
    indexOpcion = 0

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
    mostrar_palabra(puntos, indexOpcion)
    root4.mainloop()


if __name__ == "__main__":
    menu()
