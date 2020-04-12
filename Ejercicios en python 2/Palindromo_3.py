''' Dado una lista de frases ingresadas por el usuario, mostrar en
pantalla todas aquellas que sean palíndromo.'''



texto = input("Ingrese la palabra que desea evaluar (Presione . para terminar):")
while str(texto) != '.':
    igual, aux = 0, 0
    for ind in reversed(range(0, len(texto))):
        if texto[ind].lower() == texto[aux].lower():
            igual += 1
        aux += 1
    if len(texto) == igual:
        print("La palabra",texto,"es palindromo")
    else:
        print("La palabra",texto,"no es palindromo")
        
    texto = input("Ingrese la palabra que desea evaluar (Presione . para terminar):")