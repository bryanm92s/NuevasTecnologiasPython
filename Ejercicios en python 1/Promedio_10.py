'''

                            PROMEDIO DE UN ALUMNO QUE HA CURSADO 5 MATERIAS
'''


notesp=float(input("Por favor ingrese la nota final de la materia ESPAÑOL: "))
notmat=float(input("Por favor ingrese la nota final de la materia MATEMÁTICAS: "))
noteco=float(input("Por favor ingrese la nota final de la materia ECONOMÍA: "))
notpro=float(input("Por favor ingrese la nota final de la materia PROGRAMACIÓN: "))
noting=float(input("Por favor ingrese la nota final de la materia INGLES: "))


suma=notesp+notmat+noteco+notpro+noting
promedio=suma/5

print("El promedio del alumno es: ",promedio)
