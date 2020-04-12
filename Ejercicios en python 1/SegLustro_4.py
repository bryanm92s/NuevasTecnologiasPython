'''

                            CALCULAR SEGUNDOS QUE TIENE UN LUSTRO

'''

print ("CALCULAR SEGUNDOS QUE TIENE UN LUSTRO")
segundos=60
minutos=60
horasdia=24
diasmes=30
dias_año=365
años_lustro=5
seg_hora=segundos*minutos
seg_dia=seg_hora*horasdia
seg_mes=seg_dia*diasmes
seg_año=seg_dia*dias_año

lustro=años_lustro*seg_año

print ("Segundos en una hora: ", seg_hora)
print ("Segundos en un día: ", seg_dia)
print ("Segundos en un mes: ", seg_mes)
print ("Segundos en un año: ", seg_año)
print ("Segundos en un lustro: ", lustro)
