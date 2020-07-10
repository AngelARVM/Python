"""
Uso de tkinter
Uso de parser
Maquetado por grid
"""

from tkinter import *
import parser


#Ventana
ventana = Tk()
ventana.title("Calculadora")
ventana.resizable(width=0, height=0)




#Entrada
display = Entry(ventana)
display.grid(row=1, columnspan=6, sticky=W+E)




#Botones
Button(ventana, text="1", command=lambda:agregar_numero(1)).grid(row=2, column=0, sticky=W+E)
Button(ventana, text="2", command=lambda:agregar_numero(2)).grid(row=2, column=1, sticky=W+E)
Button(ventana, text="3", command=lambda:agregar_numero(3)).grid(row=2, column=2, sticky=W+E)
Button(ventana, text="4", command=lambda:agregar_numero(4)).grid(row=3, column=0, sticky=W+E)
Button(ventana, text="5", command=lambda:agregar_numero(5)).grid(row=3, column=1, sticky=W+E)
Button(ventana, text="6", command=lambda:agregar_numero(6)).grid(row=3, column=2, sticky=W+E)
Button(ventana, text="7", command=lambda:agregar_numero(7)).grid(row=4, column=0, sticky=W+E)
Button(ventana, text="8", command=lambda:agregar_numero(8)).grid(row=4, column=1, sticky=W+E)
Button(ventana, text="9", command=lambda:agregar_numero(9)).grid(row=4, column=2, sticky=W+E)

Button(ventana, text="AC", command=lambda:limpiar_display()).grid(row=5, column=0, sticky=W+E)
Button(ventana, text="0", command=lambda:agregar_numero(0)).grid(row=5, column=1, sticky=W+E)
Button(ventana, text="Mod", command=lambda:agregar_operacion("%")).grid(row=5, column=2, sticky=W+E)

Button(ventana, text="+", command=lambda:agregar_operacion("+")).grid(row=2, column=3, sticky=W+E)
Button(ventana, text="-", command=lambda:agregar_operacion("-")).grid(row=3, column=3, sticky=W+E)
Button(ventana, text="*", command=lambda:agregar_operacion("*")).grid(row=4, column=3, sticky=W+E)
Button(ventana, text="/", command=lambda:agregar_operacion("/")).grid(row=5, column=3, sticky=W+E)

Button(ventana, text="C", command= lambda:un_display()).grid(row=2, column=4, columnspan=2, sticky=W+E)
Button(ventana, text="exp", command=lambda:agregar_operacion("**")).grid(row=3, column=4, sticky=W+E)
Button(ventana, text="^2", command=lambda:agregar_operacion("**2")).grid(row=3, column=5, sticky=W+E)
Button(ventana, text="(", command=lambda:agregar_operacion("(")).grid(row=4, column=4, sticky=W+E)
Button(ventana, text=")", command=lambda:agregar_operacion(")")).grid(row=4, column=5, sticky=W+E)
Button(ventana, text="=", command=lambda:calcular()).grid(row=5, column=4, columnspan=2, sticky=W+E)


#Funciones
i = 0

def agregar_numero(n):
    global i
    display.insert(i, n)
    i+=1


def agregar_operacion(operador):
    global i
    long_operador = len(operador)
    display.insert(i, operador)
    i+=long_operador

def limpiar_display():
    display.delete(0, END)

def un_display():
    estado_display = display.get()
    if len(estado_display):
        nuevo_estado_display= estado_display[:-1]
        limpiar_display()
        display.insert(0, nuevo_estado_display)
    else:
        limpiar_display
        display.insert(0, "ERROR")


def calcular():
    estado_display = display.get()

    try:
        expresion = parser.expr(estado_display).compile()
        resultado = eval(expresion)
        limpiar_display()
        display.insert(0, resultado)
        print (resultado)
    except:
        limpiar_display()
        display.insert(0, "ERROR")


#Inicio
ventana.mainloop()