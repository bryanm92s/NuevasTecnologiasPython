'''

Crear una lista la cual almacene 10 n�meros positivos ingresados
por el usuario, mostrar en pantalla: la suma de todos los
n�meros, el promedio, el n�mero mayor y el n�mero menor.

'''

lista=[]
cantidad=int(input("Ingrese la cantidad de n�meros: "))
mayor=0
menor=0
x=1

while(cantidad>0):
    numero=float(input("N�mero #" +str(x)+ ":"))
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
print("Suma de todos los n�meros de la lista: ",suma)
print("Mayor de la lista: ",mayor)
print("Menor de la lista: ",menor)
print("Promedio de la lista: ",prom)