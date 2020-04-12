'''

                            CALCULAR LA LONGITUD DE LA SOMBRA DEL SOL

'''
import math
print("CALCULAR LA LONGITUD DE LA SOMBRA DEL SOL")
# Ángulo que forman los rayos del sol.
angulo=math.radians(22)

# Altura
h=20

# Fórmula de la longitud de la sombra
L=h/math.tan(angulo)

print("La longitud de la sombra es: ",L,"metros")