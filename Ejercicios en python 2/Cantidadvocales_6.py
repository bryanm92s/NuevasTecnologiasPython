'''

Mostrar en pantalla la cantidad de vocales que existe en una
frase dada por el usuario.

'''

cadena=(input("Ingrese la frase: ")).lower()
vocales=["a","e","i","o","u"]
cont=0
for i in vocales:
    for j in cadena:
        if(i==j):
            cont=cont+1
print("Cantidad de vocales de la frase:",cont)