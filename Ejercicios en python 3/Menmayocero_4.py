''' 4. Se requiere un algoritmo para determinar, de N cantidades, cuántas son menores o iguales a cero y cuántas mayores a cero. '''


neg=0
pos=0

numero=input("Ingrese número: (Presione x para terminar: )")
while str(numero) != 'x':
    
    if int(numero) <= 0:
        neg = neg + 1
    if int(numero)>0:
        pos=pos+1

    numero=input("Ingrese número: (Presione x para terminar: )")
    
print("Fin del algoritmo...")
print("Cantidad de números menores e iguales a cero: ",neg)
print("Cantidad de números mayores a cero: ",pos)