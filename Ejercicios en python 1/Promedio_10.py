'''

                            PROMEDIO DE UN ALUMNO QUE HA CURSADO 5 MATERIAS
'''


notesp=float(input("Por favor ingrese la nota final de la materia ESPA�OL: "))
notmat=float(input("Por favor ingrese la nota final de la materia MATEM�TICAS: "))
noteco=float(input("Por favor ingrese la nota final de la materia ECONOM�A: "))
notpro=float(input("Por favor ingrese la nota final de la materia PROGRAMACI�N: "))
noting=float(input("Por favor ingrese la nota final de la materia INGLES: "))


suma=notesp+notmat+noteco+notpro+noting
promedio=suma/5

print("El promedio del alumno es: ",promedio)
