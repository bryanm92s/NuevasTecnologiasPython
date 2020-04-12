
'''

Dado una lista de frases ingresadas por el usuario, mostrar en
pantalla todas aquellas que sean palíndromo.

'''

#Detectar palindromos en una frase e imprimirlos
# frase="El señor Uruburu contruyó un radar. Ana, que tiene buen ojo, le dijo que ni con todo el oro del mundo le haría funcionar porque no tenía rotor. Uruburu tardó en reconocer su error." 
frase = input("Ingrese la palabra y/o frase que desea evaluar: ")
#Primero quitamos todos los puntos y comas. Dejamos solo letrs y espacios.
def limpia(texto):
  limpio=''
  for i in frase:
    if i!="." and i!=",":
      limpio+=i
  return limpio

limpiado=limpia(frase)     
#Creamos una lista con todas las palabras.
lista=limpiado.split()

#Función que detecta si una palabra es o no un palíndromo
def soyPalindromo(palabra):
  palabra=palabra.lower()
  soy=True #inicialmente suponemos que si es un palíndromo
  n=len(palabra)
  if n%2==0: #número par de letras en la palabra
    for i in range(int(n/2)):
      if palabra[i]!=palabra[n-i-1]:
        soy=False
  else:  #número impar de letras
    for i in range(int((n-1)/2)):
      if palabra[i]!=palabra[n-i-1]:
        soy=False
  return soy

#Pasamos todas las palabras de la lista por la función que detecta si son palíndromos
#Si se trata de un palindromo lo imprime en pantalla

for palabrita in lista:
  if soyPalindromo(palabrita):
    print("Las palabras palíndromas:",palabrita)