'''

                            A partir del diccionario del ejercicio anterior, mostrar en pantalla
                                la materia con mejor promedio.

'''

course = {'C�lculo': 10, 'Dibujo':5, 'F�sica': 4, 'Qu�mica': 5}
total_credits = 0
mejor=-999
materiamejor=""
for materia, nota in course.items():
    print(materia, 'tiene', nota, 'cr�ditos')
    total_credits += nota
    if nota>mejor:
        mejor=nota
        materiamejor=materia
print('N�mero total de cr�ditos del curso:', total_credits)
print('Materia con mejor promedio es:',materiamejor,'con un promedio de:',mejor)