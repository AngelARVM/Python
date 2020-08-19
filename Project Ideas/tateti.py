import numpy as np

principal = np.array([[" "," "," "],[" "," "," "],[" "," "," "]])
jugador_ganador = 2

#Dibujo en pantalla
def printed():
    print ("  TA TE TI")
    print(" ")
    print ('  1   2   3')
    print ('1 ',principal[0,0],'|',principal[0,1],'|',principal[0,2])
    print ('   - - - - -')
    print ('2 ',principal[1,0],'|',principal[1,1],'|',principal[1,2])
    print ('   - - - - -')
    print ('3 ',principal[2,0],'|',principal[2,1],'|',principal[2,2])

#Elegir casilla
def juega(jugador):
    print("Donde quiere marcar?")
    fila = int(input("fila:"))
    columna = int(input("columna:"))
    if jugador == 1:
        icono = 'X'
        principal[fila-1,columna-1]=icono
    else:
        icono='O'
        principal[fila-1,columna-1]=icono
    
#Verificar juego terminado
def ganador():
    ico = " "
    if principal[0,0] == principal[0,1] == principal[0,2] != " ":    
      ico = principal[0,0]
    if principal[1,0] == principal[1,1] == principal[1,2] != " ":
      ico = principal[1,0]
    if principal[2,0] == principal[2,1] == principal[2,2] != " ":
      ico = principal[2,0]
    if principal[0,0] == principal[1,0] == principal[2,0] != " ":    
      ico = principal[0,0]
    if principal[0,1] == principal[1,1] == principal[2,1] != " ":
      ico = principal[0,1]
    if principal[0,2] == principal[1,2] == principal[2,2] != " ":
      ico = principal[0,2]
    if principal[0,0] == principal[1,1] == principal[2,2] != " ":
      ico = principal[0,0]
    if principal[0,2] == principal[1,1] == principal[2,0] != " ":
      ico = principal[0,2]
    return ico

#Proceso principal
for i in range (1,10):
    if i%2==0:
        turno = 2
    else:
        turno = 1

    printed()
    print ("turno del jugador ",turno)
    juega(turno)
    ico = ganador()

    if ico == 'X':
        jugador_ganador= 1
        break

    if ico == 'O':
        jugador_ganador= 2
        break
    printed()

printed()
print ("Ganador jugador ", jugador_ganador)
