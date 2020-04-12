'''

Crear una lista la cual almacene 10 números positivos ingresados
por el usuario, mostrar en pantalla: la suma de todos los
números, el promedio, el número mayor y el número menor.

'''

lista=[]
cantidad=int(input("Ingrese la cantidad de números: "))
mayor=0
menor=0
x=1

while(cantidad>0):
    numero=float(input("Número #" +str(x)+ ":"))
    if numero>0:
        lista.append(numero)
        x=x+1
        cantidad=cantidad-1
        suma=0.0
        for i in range(0,len(lista)):
            suma=suma+lista[i]
            prom=suma/len(lista)

mayor=max(lista)
menor=min(lista)

print("Lista:",lista)
print("Suma de todos los números de la lista: ",suma)
print("Mayor de la lista: ",mayor)
print("Menor de la lista: ",menor)
print("Promedio de la lista: ",prom)