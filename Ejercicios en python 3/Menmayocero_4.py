''' 4. Se requiere un algoritmo para determinar, de N cantidades, cu�ntas son menores o iguales a cero y cu�ntas mayores a cero. '''


neg=0
pos=0

numero=input("Ingrese n�mero: (Presione x para terminar: )")
while str(numero) != 'x':
    
    if int(numero) <= 0:
        neg = neg + 1
    if int(numero)>0:
        pos=pos+1

    numero=input("Ingrese n�mero: (Presione x para terminar: )")
    
print("Fin del algoritmo...")
print("Cantidad de n�meros menores e iguales a cero: ",neg)
print("Cantidad de n�meros mayores a cero: ",pos)