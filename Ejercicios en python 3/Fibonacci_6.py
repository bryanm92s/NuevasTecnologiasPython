'''6. Realice un algoritmo para generar N elementos de la sucesión de Fibonacci (0, 1, 1, 2, 3, 5, 8,
13,...).'''


ant = 0
sig = 1
auxiliar = 0

numero=int(input("Por favor ingrese la cantidad de números a generar: "))
for n in range(0,numero):
    auxiliar = ant;
    ant = sig;
    sig = auxiliar + ant;
    print("Número Fibonacci en la posición #:",n+1, "es:",auxiliar)