"""
Manejo tkinter
Manejo Archivos
Manejo Listas
"""

import tkinter
from tkinter import messagebox

#raiz
root = tkinter.Tk()


#listas
lista = []


#variables
nombre = tkinter.StringVar()
apellido = tkinter.StringVar()
correo = tkinter.StringVar()
telefono = tkinter.StringVar()
eliminar = tkinter.StringVar()
guardar= tkinter.StringVar()
color_fondo = "#c1c1c1"
color_letra = "black"


#Formato ventana
root.title("Agenda")
root.geometry("700x500")
root.configure(bg=color_fondo)


#Funciones
def inciar_archivo():
    archivo = open("agenda.txt", "a")
    archivo.close()


def cargar():
    archivo = open("agenda.txt", "r")
    linea = archivo.readline()
    if linea:
        while linea:
            if linea[-1] == '\n':
                linea = linea[:-1]
            lista.append(linea)
            linea = archivo.readline()
    archivo.close()


def agregar_contacto():
    archivo = open("agenda.txt", "w")
    lista.sort()
    for elemento in lista:
        archivo.write(elemento+"\n")
    archivo.close



def consultar():
    r = tkinter.Text(root, width=60, height=15)
    lista.sort()
    valores = []
    r.insert(tkinter.INSERT, "Nombre \t\tApellido \t\tCorreo \t\tNumero\t\t")
    for elemento in lista:
        arreglo = elemento.split("$")
        valores.append(arreglo[3])
        r.insert(tkinter.INSERT, arreglo[0]+"\t\t"+arreglo[1]+"\t\t"+arreglo[2]+"\t\t"+arreglo[3]+"\t\t")
    r.place(x=20, y=230)
    #spin_telefono=tkinter.Spinbox(root, value=(valores), textvariable= eliminar).place(x=450, y=50)
    if lista==[]:
        spin_telefono = tkinter.Spinbox(root, value=(valores), textvariable=eliminar).place(x=450, y=50)
    r.configure(state=tkinter.DISABLED)


def fun_guardar():
    n = nombre.get()
    ap=apellido.get()
    c = correo.get()
    t = telefono.get()
    lista.append(n+"$"+ap+"$"+c+"$"+t+"$")
    agregar_contacto()
    messagebox.showinfo("Guardado","El contacto ha sido guardado en la agenda")
    nombre.set("")
    apellido.set("")
    correo.set("")
    telefono.set("")
    consultar()

def fun_eliminar():
    eliminado = eliminar.get()
    removido = False
    for elemento in lista:
        arreglo = elemento.split("$")
        if eliminar.get() == arreglo[3]:
            lista.remove(elemento)
            removido = True
    agregar_contacto()
    consultar()
    if removido:
        messagebox.showinfo("Elimiar","El contacto ha sido eliminado "+eliminado)


#Secciones
etiqueta_titulo = tkinter.Label(root, text="Agenda con archivos", bg=color_fondo, fg=color_letra, font=("Arial",13)).place(x=260, y=10)

etiqueta_nombre = tkinter.Label(root, text="Nombre: ", bg=color_fondo, fg=color_letra).place(x=50, y=50)
caja_nombre= tkinter.Entry(root, textvariable=nombre).place(x=110, y=50)

etiqueta_apellido = tkinter.Label(root, text="Apellido: ", bg=color_fondo, fg=color_letra).place(x=50, y=75)
caj_apellido= tkinter.Entry(root, textvariable=apellido).place(x=110, y=75)

etiqueta_correo = tkinter.Label(root, text="Correo: ", bg=color_fondo, fg=color_letra).place(x=50, y=100)
caja_correo= tkinter.Entry(root, textvariable=correo).place(x=110, y=100)

etiqueta_numero = tkinter.Label(root, text="Numero: ", bg=color_fondo, fg=color_letra).place(x=50, y=125)
caja_numero= tkinter.Entry(root, textvariable=telefono).place(x=110, y=125)

etiqueta_eliminar = tkinter.Label(root, text="Telefono: ", bg=color_fondo, fg=color_letra).place(x=350, y=50)
spin_telefono = tkinter.Spinbox(root, textvariable=eliminar).place(x=410, y=50)

boton_guardar= tkinter.Button(root, text="Guardar", command=fun_guardar, bg=color_fondo, fg=color_letra).place(x=140, y=150)

boton_eliminar= tkinter.Button(root, text="Eliminar", command=fun_eliminar, bg=color_fondo, fg=color_letra).place(x=440, y=80)


#Inicio
inciar_archivo()
cargar()
consultar()
root.mainloop()
