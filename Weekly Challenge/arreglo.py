"En un tablero de 20 x 20 4 números han sido marcados con rojo (ver imagen). El producto de estos números es 26 * 63 * 78 * 14 = 1788696.

Cual es el mayor numero que puede conseguirse al multiplicar 4 números adyacentes en una misma dirección? (Arriba, abajo, izquierda, derecha o diagonalmente)

(El arreglo del ejercicio esta contenido en archivo matriz.txt)
"


import numpy as np
import pandas as pd
arreglo=pd.read_csv('matriz.txt', delimiter=',')
arreglo=arreglo.to_numpy()
arreglo = np.int_(arreglo)
filas, columnas =arreglo.shape
mayor, valor, numero1, numero2, numero3, numero4, pos1, pos2, pos3, pos4 = 0,0,0,0,0,0,(0,0),(0,0),(0,0),(0,0)

def abajo():
  global mayor, numero1, numero2, numero3, numero4, pos1, pos2, pos3, pos4
  for i in range (0,filas):
    for j in range (0,columnas):
      if i+3 < filas:
        valor=arreglo[i,j]*arreglo[i+1,j]*arreglo[i+2,j]*arreglo[i+3,j]
        if valor > mayor:
          mayor=valor
          numero1, numero2, numero3, numero4 = arreglo[i,j], arreglo[i+1,j], arreglo[i+2,j],arreglo[i+3,j]
          pos1, pos2, pos3, pos4 = (i+1,j+1), (i+2,j+1), (i+3,j+1), (i+4,j+1)
      if i-3 > 0:
        valor=arreglo[i,j]*arreglo[i-1,j]*arreglo[i-2,j]*arreglo[i-3,j]
        if valor > mayor:
          mayor=valor
          numero1, numero2, numero3, numero4 = arreglo[i,j], arreglo[i-1,j], arreglo[i-2,j],arreglo[i-3,j]
          pos1, pos2, pos3, pos4 = (i-1,j+1), (i-2,j+1), (i-3,j+1), (i-4,j+1)
      if j+3 < columnas:
        valor=arreglo[i,j]*arreglo[i,j+1]*arreglo[i,j+2]*arreglo[i,j+3]
        if valor > mayor:
          mayor=valor
          numero1, numero2, numero3, numero4 = arreglo[i,j], arreglo[i,j+1], arreglo[i,j+2], arreglo[i,j+3]
          pos1, pos2, pos3, pos4 = (i+1,j+1), (i+1,j+2), (i+1,j+3), (i+1,j+4)
      if j-3 > 0:
        valor=arreglo[i,j]*arreglo[i,j-1]*arreglo[i,j-2]*arreglo[i,j-3]
        if valor > mayor:
          mayor=valor
          numero1, numero2, numero3, numero4 = arreglo[i,j], arreglo[i,j-1], arreglo[i,j-2], arreglo[i,j-3]
          pos1, pos2, pos3, pos4 = (i+1,j-1), (i+1,j), (i+1,j-1), (i+1,j-2)
      if i+3<filas and j+3<columnas:
        valor=arreglo[i,j]*arreglo[i+1,j+1]*arreglo[i+2,j+2]*arreglo[i+3,j+3]
        if valor > mayor:
          mayor=valor
          numero1, numero2, numero3, numero4 = arreglo[i,j], arreglo[i+1,j+1], arreglo[i+2,j+2], arreglo[i+3,j+3]
          pos1, pos2, pos3, pos4 = (i+1,j+1), (i+2,j+2), (i+3,j+3), (i+4,j+4)
      if i+3<filas and j-3>0:
        valor=arreglo[i,j]*arreglo[i+1,j-1]*arreglo[i+2,j-2]*arreglo[i+3,j-3]
        if valor > mayor:
          mayor=valor
          numero1, numero2, numero3, numero4 = arreglo[i,j], arreglo[i+1,j-1], arreglo[i+2,j-2], arreglo[i+3,j-3]
          pos1, pos2, pos3, pos4 = (i+1,j+1), (i+2,j), (i+3,j-1), (i+4,j-2)
  
abajo()
print ("Mayor valor: ",mayor)
print ("Valores: ", numero1, numero2, numero3, numero4)
print ("Posiciones: ", pos1, pos2, pos3, pos4)
