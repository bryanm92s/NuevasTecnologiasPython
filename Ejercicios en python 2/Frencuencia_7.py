'''

                            Mostrar en pantalla la frecuencia de aparici�n de vocales en una
                            frase dada por el usuario.

'''

contador={}
for i in range(1):
   cadena=input("Ingrese la frase: ")
   for caracter in cadena:
       if caracter not in contador:
           contador[caracter]=1
       else:
           contador[caracter]+=1
print("Frecuencia de cada car�cter")
for caracter, cantidad in contador.items():
   print(caracter, ": ", cantidad)
