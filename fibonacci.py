a0 = 0 #Define el termino a sub cero de la sucesión.
a1 = 1 #Define el termino a sub uno del a sucesión.
n= 15 #Define el termino enésimo hasta el cual se quiere proyectar la sucesion. (Cambiar su valor para proyectar la sucesión hasta un termino distinto)
fibonacci = [f0, f1] #Lista que contendrá la sucesion, definida con los terminos a sub cero y a sub uno.

#Funcion que toma una lista y proyecta la sucesion hasta el termino enésimo.
def fn (lista,termino):
  for i in range(1,termino):
    lista.append(lista[len(lista)-1]+lista[len(lista)-2])
  return 
  
fn(fibonacci, n)
print (fibonacci)
