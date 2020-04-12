
'''
            CANTIDAD DE MESES DURANTE DOS FECHAS

'''

from datetime import datetime, timedelta
formato = "%d/%m/%Y"
continuar="S"


while str(continuar.upper()) !="N":
    fecha_desde = input("Introducir fecha inicial (dd/mm/aaaa): ")
    fecha_final = input("Introducir fecha final (dd/mm/aaaa): ")
    if fecha_desde=="":
        
        break
    if fecha_final=="":
        
        break
    
    fecha_desde = datetime.strptime(fecha_desde, formato)
    fecha_final = datetime.strptime(fecha_final, formato)
    
    
    if fecha_final >= fecha_desde:
      # Se cálcula diferencia en día y se muestra el resultado
      diferencia = fecha_final - fecha_desde
      meses=diferencia.days/30
      anio=diferencia.days/365
      print("Cantidad de días entre las dos fechas:", diferencia.days, "días")
      print("Cantidad de meses entre las dos fechas: ", int(meses), "meses")
      print("Cantidad de años entre las dos fechas: ", int(anio), "años")
      
    else:
        print("La fecha inicial debe ser menor que la fecha final")
    
    continuar = input("Deseas continuar?: \n S:Si \n N:No \n")