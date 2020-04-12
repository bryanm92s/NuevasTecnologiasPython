'''5. Realice un algoritmo para generar e imprimir los números pares e impares que se encuentran
entre 0 y 100. Además muestre la multiplicación de todos estos.'''

pares=0
impares=0
multpares=1
multimpares=1
multiplicacion=1




for n in range(1,101):
    
    if n%2==0:
        pares=pares+1
        multpares=multpares*n
        print("El número: ",n,"Es par")
    else:
        impares = impares + 1
        multimpares = multimpares * n
        print("El número: ",n,"Es impar")
    multiplicacion = multiplicacion * n
    
print("Cantidad de números pares entre 1-10: ", pares)
print("Cantidad de números impares entre 1-10: ", impares)
print("La multiplicación de todos los números entre 1-10 es: ", multiplicacion)
print("La multiplicación de los números pares entre 1-10 es: ", multpares)
print("La multiplicación de los números impares entre 1-10 es: ", multimpares)