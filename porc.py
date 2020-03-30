#from datetime import date
from datetime import *


fecha1 = '2001-01-01' #fecha de inicio del siglo
fecha2 = '2100-12-31'  #fecha final

#Fecha dadas
fechada= '2007-07-21' 
fechada2= '2013-09-04'
fechada3= '2018-08-17'

total_dias = (datetime.strptime(fecha2, '%Y-%m-%d').date() - datetime.strptime(fecha1, '%Y-%m-%d').date()).days
print(total_dias)

#número de dia en el que esta
diasres1 = (datetime.strptime(fechada, '%Y-%m-%d').date() - datetime.strptime(fecha1, '%Y-%m-%d').date()).days
diasres2 = (datetime.strptime(fechada2, '%Y-%m-%d').date() - datetime.strptime(fecha1, '%Y-%m-%d').date()).days
diasres3 = (datetime.strptime(fechada3, '%Y-%m-%d').date() - datetime.strptime(fecha1, '%Y-%m-%d').date()).days

#porcentaje
porcentaje1 = diasres1 * 100 / total_dias
porcentaje2 = diasres2 * 100 / total_dias
porcentaje3 = diasres3 * 100 / total_dias


print ("Porcentaje fecha1",fechada,"%.6f" % (porcentaje1),"%")
print ("Porcentaje fecha2",fechada2,"%.6f" % (porcentaje2),"%")
print ("Porcentaje fecha3",fechada3,"%.6f" % (porcentaje3),"%")
