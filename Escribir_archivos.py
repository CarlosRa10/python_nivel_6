archivo = open('C:/Users/Carlos Ramirez/Desktop/PythonTotal/pythonProject/Dia 6/python_nivel_6/Prueba1.txt','w')
#No agarra la letras con acento (Día)
archivo.write('Soy una linea mas en una hoja de texto mas')
archivo.write('\nHola\n')
archivo.write('Mundo\n')
archivo.write('''Como
estan\n''')
#archivo.writelines(['Hola', 'mundo','aqui','estoy'])
lista = ['Hola', 'mundo','aqui','estoy']
for i in lista:
    archivo.writelines(i + '\n')
archivo.close()
#print(archivo.read())
#archivo.close()
'''print(archivo.read())
archivo.close()'''

archivo = open('C:/Users/Carlos Ramirez/Desktop/PythonTotal/pythonProject/Dia 6/python_nivel_6/Prueba1.txt','a')
archivo.write('Gracias')
archivo.close()


###EXAMEN###
archivo = open("mi_archivo.txt", "w")
archivo.write("Nuevo texto")
archivo.close()
archivo = open("mi_archivo.txt", "r")
print(archivo.read())




archivo = open("mi_archivo.txt","a")
archivo.write("Nuevo inicio de sesión")
archivo.close()
archivo = open("mi_archivo.txt", "r")
print(archivo.read())




registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
 
registro = open("registro.txt","a")
for item in registro_ultima_sesion:
    registro.writelines(item +'\t')
 
registro.close()
registro = open("registro.txt","r")
print(registro.read())