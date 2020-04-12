'''
Remplazar cada letra de una frase dada por el usuario por la
posición que le corresponde en el abecedario

'''


palabra = (input('Escribe una palabra para codificar: ')).lower()
codificar = []
for caracter in palabra:
    numero = ord(caracter) - 96
    codificar.append(numero)
print ("La palabra:""'",palabra,"'"",codificada es igual a: ",codificar)

