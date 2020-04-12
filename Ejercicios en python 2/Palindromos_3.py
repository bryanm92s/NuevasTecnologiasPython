
'''

Dado una lista de frases ingresadas por el usuario, mostrar en
pantalla todas aquellas que sean pal�ndromo.

'''

#Detectar palindromos en una frase e imprimirlos
# frase="El se�or Uruburu contruy� un radar. Ana, que tiene buen ojo, le dijo que ni con todo el oro del mundo le har�a funcionar porque no ten�a rotor. Uruburu tard� en reconocer su error." 
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

#Funci�n que detecta si una palabra es o no un pal�ndromo
def soyPalindromo(palabra):
  palabra=palabra.lower()
  soy=True #inicialmente suponemos que si es un pal�ndromo
  n=len(palabra)
  if n%2==0: #n�mero par de letras en la palabra
    for i in range(int(n/2)):
      if palabra[i]!=palabra[n-i-1]:
        soy=False
  else:  #n�mero impar de letras
    for i in range(int((n-1)/2)):
      if palabra[i]!=palabra[n-i-1]:
        soy=False
  return soy

#Pasamos todas las palabras de la lista por la funci�n que detecta si son pal�ndromos
#Si se trata de un palindromo lo imprime en pantalla

for palabrita in lista:
  if soyPalindromo(palabrita):
    print("Las palabras pal�ndromas:",palabrita)