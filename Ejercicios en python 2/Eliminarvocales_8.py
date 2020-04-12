'''

                            Eliminar todas las vocales de una frase dado por el usuario y
                            mostrar el nuevo string en pantalla.

'''

texto = (input("ingrese un texto para eliminar las vocales: "))
texto.lower()

vocales = ('a', 'e', 'i', 'o', 'u')

for letra in vocales:
    texto = texto.replace(letra, "")

#Invierte la cadena
print (texto)
