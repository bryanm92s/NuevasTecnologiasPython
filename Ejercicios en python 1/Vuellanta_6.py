'''

                            CALCULAR NÚMERO DE VUELTAS DE UNA LLANTA EN 1KM

'''

print ("CALCULAR NÚMERO DE VUELTAS DE UNA LLANTA EN 1KM")
diametro=50
radio=diametro/2
pi=3.1416

#Sabemos que la distancia recorrida en una vuelta por la rueda es 2·pi·R siendo R el radio de la circunferencia.
# Cantidad de centímentros recorridos en una vuelta.
Lc=2*pi*radio

# Convertimos L en metros.
Lm=Lc/100

# Regla de 3

''' 1 vuelta ------- Lm
    x vueltas ------ 1000metros (1km)'''

Vueltasen_1Km= 1000*1/Lm


print ("La rueda recorre en una vuelta: ",Lc, "Centímetros")
print ("La rueda recorre en una vuelta : ",Lm,"Metros")
print ("La llanta da : ",Vueltasen_1Km, " vueltas en 1 km")