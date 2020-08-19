"2520 es el numero mas pequeño que a su ves es divisible por todos los números del 1 al 10.

Escribir un algoritmo que calcule el numero mas pequeño que es divisible por todos los números del 1 al 20. 
 (1,2,3,4,5,6...)"

min = 2520
val = True

divisores = [11,13,14,16,17,18,19,20]

while val:
  for numero in divisores:
    if not (min%numero == 0):
      min+=20
      break
    elif numero == 20:
      val = False

print (min)
