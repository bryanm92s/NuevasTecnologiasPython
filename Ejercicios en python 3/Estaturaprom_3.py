''' 3. Se requiere un algoritmo para obtener la estatura promedio de un grupo de personas, cuyo
número de miembros se desconoce, el ciclo debe efectuarse siempre y cuando se tenga una
estatura registrada. '''


estatura=0
contador=0
sumest=0
promedio=0


while estatura>=0:
    estatura=int(input("Ingrese estatura: "))
    
    if estatura>=0:
        contador=contador+1
        sumest=sumest+estatura
        promedio=sumest/contador

print("Cantidad de personas ingresadas: ", contador)
print("Suma de las estaturas: ", sumest)
print("Promedio de las estaturas ingresadas es: ",promedio)