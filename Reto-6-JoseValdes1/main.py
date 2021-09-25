

#funciones - importar
import funciones as f

# 1. Lista enviada por el DPA
#

lista_enviada_DPA=f.lectura()

#Inicio programa
print("============Departamento de prácticas académicas (DPA) ==============")
#solicitud longitud de la fila

cantidad_fila=int(input("Ingrese la cantidad de estudiantes en la fila:\n"))

print("\n")
print("========================Asignación de turnos========================")
#se invoca la funcion asignar turnos y se devuelve la lista de los codigos asignados en cada turno
lista_turnos=f.asignar_turno(cantidad_fila,lista_enviada_DPA)
print("========================Inscripción========================")
#
#Se invoca la funcion inscripcion para incribir a los alumnos
lista_incritos=f.incripcion(lista_turnos) 

#Reporte
print("======================Reporte DPA======================")
#Total inscritos a practicas
if len(lista_incritos)>1:
  print("El total de alumnos inscritos a practicas fueron ",len(lista_incritos),"\n")
else:
  print("El total de alumnos inscritos a practicas fue ",len(lista_incritos),"\n") 

#total inscritos por programa, se realiza cuenta de la cantidad de estudiantes incritos por el tipo de programa
contador_ele=0
contador_sis=0
contador_civil=0

for x in range(len(lista_incritos)):
  if lista_incritos[x][2]==1:
    contador_civil+=1
  elif lista_incritos[x][2]==2:
    contador_sis+=1
  elif lista_incritos[x][2]==3:
    contador_ele+=1



if contador_civil>1:
  print("La cantidad de alumnos inscritos en el programa de Ingeniería civil fueron ",contador_civil,"\n")
else:
  print("La cantidad de alumnos inscritos en el programa de Ingeniería civil fue ",contador_civil,"\n")

if contador_sis>1:
  print("La cantidad de alumnos inscritos en el programa de Ingeniería de sistemas fueron ",contador_sis,"\n")
else:
  print("La cantidad de alumnos inscritos en el programa de Ingeniería de sistemas fue ",contador_sis,"\n")  

if contador_ele>1:
  print("La cantidad de alumnos inscritos en el programa de Ingeniería electrónica fueron ",contador_ele,"\n")
else:
  print("La cantidad de alumnos inscritos en el programa de Ingeniería electrónica fue ",contador_ele,"\n")  

#promedio por programa

print("El promedio de alumnos inscritos en el programa de Ingeniería civil fue ",contador_civil/len(lista_incritos),"\n")

print("El promedio de alumnos inscritos en el programa de Ingeniería de sistemas fue ",contador_sis/len(lista_incritos),"\n")

print("El promedio de alumnos inscritos en el programa de Ingeniería electronica fue ",contador_ele/len(lista_incritos),"\n")

#La lista con todos los incritos se tiene en el sistema con la lista lista_incritos que es una lista con tuplas en cada posicion de cada uno de los alumnos inscritos
#print("\n",lista_incritos,"\n")
#grafica Promedio de inscritos por programa

f.diagrama(["civil","sistemas","electrónica"],[float((contador_civil/len(lista_incritos))),float((contador_sis/len(lista_incritos))),float((contador_ele/len(lista_incritos)))],[contador_civil,contador_sis,contador_ele])


#grafica Total inscritos por tipo de programa

#f.diagrama_barras([contador_civil,contador_sis,contador_ele])