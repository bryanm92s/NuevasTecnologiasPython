'''5. Realice un algoritmo para generar e imprimir los n�meros pares e impares que se encuentran
entre 0 y 100. Adem�s muestre la multiplicaci�n de todos estos.'''

pares=0
impares=0
multpares=1
multimpares=1
multiplicacion=1




for n in range(1,101):
    
    if n%2==0:
        pares=pares+1
        multpares=multpares*n
        print("El n�mero: ",n,"Es par")
    else:
        impares = impares + 1
        multimpares = multimpares * n
        print("El n�mero: ",n,"Es impar")
    multiplicacion = multiplicacion * n
    
print("Cantidad de n�meros pares entre 1-10: ", pares)
print("Cantidad de n�meros impares entre 1-10: ", impares)
print("La multiplicaci�n de todos los n�meros entre 1-10 es: ", multiplicacion)
print("La multiplicaci�n de los n�meros pares entre 1-10 es: ", multpares)
print("La multiplicaci�n de los n�meros impares entre 1-10 es: ", multimpares)