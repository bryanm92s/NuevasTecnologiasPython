''' 1. Se requiere un algoritmo para obtener la edad promedio de un grupo de N alumnos. Si algún
alumno tiene más de 18 años, se muestra el promedio que se lleva sin contar el alumno de 18
años. EL usuario decide si desea cerrar el programa o vuelve a ejecutarlo. '''


continuar=1
suma=0
cont=0
edad=0
cont18=0
suma18=0
sumanenores=0
contadoremenores=0
promediomenores=0

while continuar==1:
    
    while True:
        edad=int(input("Ingrese edad: "))
        suma = suma + edad
        cont = cont + 1
        if(edad >= 18):
            cont18 = cont18 + 1;
            suma18 = suma18 + edad;
            
            sumanenores = suma - suma18;
            contadoremenores = cont - cont18;
            promediomenores = sumanenores / contadoremenores;
            print("Suma de las edades menores a 18 años: ", sumanenores)
            print("Cantidad de personas encuestadas menores a 18 años: ",contadoremenores)
            print("Promedio de edades de las personas menores a 18 años :",promediomenores)
            
            #print("Cantidad de personas con 18 años o más: ",cont18)
            #print("Suma de las personas con 18 años o más: ", suma18)
            
            continuar=int(input("Desea continuar? \n 1:Si \n 2: No : "))

        break