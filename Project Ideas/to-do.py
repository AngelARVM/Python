"""
Aplicacion de lista de tareas:
Manejo de listas
Manejo de TKinter
"""

import tkinter
import random
from tkinter import messagebox

#raiz
root= tkinter.Tk()


#formato ventana
root.configure(bg="white")
root.title("To-do List")
root.geometry("275x235")


#Listas
tareas = []
tareas = ["llamar a mama", "comprar guitarra"]


#funciones

def actualizar():
    limpiar()
    for tarea in tareas:
        lb_tareas.insert("end", tarea)

def limpiar():
    lb_tareas.delete(0, "end")

def agregar_tarea():
    tarea = txt_entrada.get()
    if tarea !="":
        tareas.append(tarea)
        actualizar()
    else:
        messagebox.showwarning("Aviso", "Debes ingresar una tarea.")
    txt_entrada.delete(0, "end")

def a():
    return

def borrar_todo():
    confirmado = messagebox.askyesno("Confirmar borrar todo", "Realmente quieres borrar todas las tareas?")
    global tareas
    if confirmado:
        tareas = []
    actualizar()

def borrar():
    tarea = lb_tareas.get("active")
    if tarea in tareas:
        tareas.remove(tarea)
    else:
        label_display["text"]="Por favor, elija una tarea."
    actualizar()
        

def ordenar_ascendente():
    tareas.sort()
    actualizar()

    
def ordenar_descendente():
    tareas.sort()
    tareas.reverse()
    actualizar()


def elegir_alguno():
    tarea = random.choice(tareas)
    label_display["text"]= tarea

def cantidad_tareas():
    cantidad = len(tareas)
    mensaje = "Cantidad de tareas: %s" %cantidad
    label_display["text"]=mensaje
 
def salir():
    return


#titulo
label_titulo= tkinter.Label(root,text="To-do List", bg="white")
label_titulo.grid(row=0, column=0)


#cuadro texto
label_display= tkinter.Label(root,text="", bg="white")
label_display.grid(row=0, column=1)


#botones
txt_entrada= tkinter.Entry(root, width=15)
txt_entrada.grid(row=1, column=1)

btn_agregar_tarea= tkinter.Button(root, text="Agregar", fg="black", bg="white", command=agregar_tarea)
btn_agregar_tarea.grid(row=1, column=0)

btn_borrar_todo= tkinter.Button(root, text="Borrar todo", fg="black", bg="white", command=borrar_todo)
btn_borrar_todo.grid(row=2, column=0)

btn_borrar= tkinter.Button(root, text="Borrar", fg="black", bg="white", command=borrar)
btn_borrar.grid(row=3, column=0)

btn_ordenar_ascendente= tkinter.Button(root, text="Ordenar (ASC)", fg="black", bg="white", command=ordenar_ascendente)
btn_ordenar_ascendente.grid(row=4, column=0)

btn_ordenar_descendente= tkinter.Button(root, text="Ordenar (DESC)", fg="black", bg="white", command=ordenar_descendente)
btn_ordenar_descendente.grid(row=5, column=0)

btn_elegir_alguno= tkinter.Button(root, text="Elegir alguno", fg="black", bg="white", command=elegir_alguno)
btn_elegir_alguno.grid(row=6, column=0)

btn_cantidad_tareas= tkinter.Button(root, text="Cantida de tareas", fg="black", bg="white", command=cantidad_tareas)
btn_cantidad_tareas.grid(row=7, column=0)

btn_salir= tkinter.Button(root, text="Salir", fg="black", bg="white", command=salir)
btn_salir.grid(row=8, column=0)


lb_tareas = tkinter.Listbox(root)
lb_tareas.grid(row=2, column=1, rowspan=7)


#inicio
actualizar()
root.mainloop()


