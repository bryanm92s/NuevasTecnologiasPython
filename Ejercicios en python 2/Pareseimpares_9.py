'''5. Realice un algoritmo para generar e imprimir los números pares e impares que se encuentran
entre 0 y 100.'''

pares=0
impares=0

for n in range(0,101):
    
    if n%2==0:
        pares=pares+1
        print("El número: ",n,"Es par")
    else:
        impares = impares + 1
        print("El número: ",n,"Es impar")