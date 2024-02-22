#Crear una lista con 5 elementos y luego aplica los siguientes

colores=["rojo","azul","amarrillo","verde","negro"]
print("Lista de colores: ",colores)
#Imprimir el último elemento
a=len(colores)
a=a-1
print("El ultimo elemento es: ",colores[a])

#Modificar el valor del tercer elemento
colores[2]="violeta"
print("lista modificada: ",colores)

#Agregar dos elementos
colores.append("naranja")
colores.append("blanco")
print("Con 2 elementos",colores)

#Eliminar algún elemento

colores.remove("azul")
print("Sin el elemento azul",colores)

