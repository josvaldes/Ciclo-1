
from collections import namedtuple
import datetime
import matplotlib.pyplot as plt
import numpy as np


def asignar_turno (cantidad_fila,lista_enviada_DPA):
  lista_estudiantes_fila=[]
  lista_de_turnos={}
  i=0
  turno=0

  while i<cantidad_fila:
    #Solicitud de codigo del estudiante
    estudiante=(input("Digite su codigo de identificacion estudiantil:\n"))
    
    print("\n")

    #Se valida que el codigo del estudiante este postulado a practicas
    if lista_enviada_DPA.get(estudiante)==None:
      print("No se encuentra postulado a practicas\n")
    else:
      if lista_de_turnos.get(estudiante)==None:
        turno+=1
        lista_de_turnos[estudiante]=turno
        lista_estudiantes_fila.append([estudiante,turno])
        print("Su turno es ",turno)
        print("\n") 
      else:
        print("Error, al codigo ingresado ya le fue asignado un turno")
        print("\n")
        i-=1
    
    
    #control del bucle
    i +=1
    
  return lista_estudiantes_fila

def incripcion (lista_turnos):
  i=len(lista_turnos)
  lista_alumnos=[]
  x=0
  Datos_alumnos=namedtuple("Datos_alumnos", ["nombre","edad","inscrito_practica","fecha_y_horas"]) 
  while i>0:
    print("Se solicita acercarse a la ventanilla el turno ",lista_turnos[x][1]," codigo del alumno ",lista_turnos[x][0],"\n")
    nombre=input("Digite su nombre completo:\n")
    edad=int(input("Digite su edad:\n"))
    programa=int(input("Ingrese su programa de estudio:\n 1 - Ingeniería civil\n 2 - Ingeniería de sistemas\n 3 - Ingeniería electrónica\n"))
    fecha=datetime.datetime.now() #Profesor tengo dudas con la fecha que devuele y la que veo en el pc, una diferencia de 5 horas
    Datos_alumnos2=Datos_alumnos(nombre,edad,programa,fecha)
    lista_alumnos.append(Datos_alumnos2)
    print("\n")
    x+=1
    #control del bucle
    i-=1

  return lista_alumnos


def lectura ():
  archivo = open("codigos_estudiantes.txt","r")

  lista_enviada_DPA=archivo.read()

  miDiccionario={}

  for line in lista_enviada_DPA.splitlines():
    valores=line.split(":",1)
    miDiccionario[valores[0].strip()] = valores[1].strip()


  archivo.close()
  
  return miDiccionario 

def diagrama (programas,promedios_instritos,cantidad_inscritos_programa):
  #diagrama de barras, cantidad de alumnos inscritos
  labels = ['Ing Civil', 'Ing Sistemas', 'Ing Electronica']
  men_means = cantidad_inscritos_programa
  
  x = np.arange(len(labels))  # the label locations
  width = 0.35  # the width of the bars

  fig, ax = plt.subplots()
  rects1 = ax.bar(x - width/2, men_means, width, label='Programas')
 
  ax.set_ylabel('Cantidad de Estudiantes inscritos')
  
  ax.set_xticks(x)
  ax.set_xticklabels(labels)
  ax.legend()

  ax.bar_label(rects1, padding=3)
  fig.tight_layout()
  

  #Diagrama de torta promedios de estudiantes incritos de cada facultad
  
  y = np.array(cantidad_inscritos_programa)
  mylabels = ["Ing Civil", "Ing Sistemas", "Ing Electronica"]


  ig1, ax1 = plt.subplots()
  ax1.pie(y,  labels=mylabels, autopct='%1.1f%%',
          shadow=True, startangle=90)
  ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

  plt.show()  	 	

