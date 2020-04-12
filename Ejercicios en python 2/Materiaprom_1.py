'''

                            A partir del diccionario del ejercicio anterior, mostrar en pantalla
                                la materia con mejor promedio.

'''

course = {'Cálculo': 10, 'Dibujo':5, 'Física': 4, 'Química': 5}
total_credits = 0
mejor=-999
materiamejor=""
for materia, nota in course.items():
    print(materia, 'tiene', nota, 'créditos')
    total_credits += nota
    if nota>mejor:
        mejor=nota
        materiamejor=materia
print('Número total de créditos del curso:', total_credits)
print('Materia con mejor promedio es:',materiamejor,'con un promedio de:',mejor)