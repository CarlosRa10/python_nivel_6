mi_archivo = open('C:/Users/Casa/Desktop/PythonTotal/pythonProject/Día 6/Prueba.txt')
'''una_linea = mi_archivo.readline()
print(mi_archivo) #lo abrio pero no lo leyo
#print(mi_archivo.read())#Lee
print(una_linea.upper())
una_linea = mi_archivo.readline()
print(una_linea.rstrip())
una_linea = mi_archivo.readline()
print(una_linea)


for l in mi_archivo:
    print("Aqui dice: " + l)'''

todas_las_lineas = mi_archivo.readlines()   
print(todas_las_lineas)

todas_las_lineas = todas_las_lineas.pop()
print(todas_las_lineas)
mi_archivo.close()


###EXAMEN###

mi_archivo = open('C:/Users/Casa/Desktop/PythonTotal/pythonProject/Día 6/Prueba.txt')
print(mi_archivo.read())

##############################
mi_archivo = open('C:/Users/Casa/Desktop/PythonTotal/pythonProject/Día 6/Prueba.txt')

una_linea = mi_archivo.readline()
print(una_linea)


mi_archivo.close()

#################
mi_archivo = open('C:/Users/Casa/Desktop/PythonTotal/pythonProject/Día 6/Prueba.txt')
primera_linea = mi_archivo.readline()
segunda_linea = mi_archivo.readline()
print(segunda_linea)