#Crea una función llamada verificar_calificacion que reciba tres
# parámetros: nota1, nota2 y nota3
#Si el promedio es mayor o igual a 6, entonces la función debe
#retornar un mensaje “Aprobado”, en caso contrario “Reprobado”

def verificar_calificacion(nota1,nota2,nota3):
    promedio=(nota1+nota2+nota3)/3
    
    if promedio>=6:
        return "Aprobado"
    else:
        return "Reprobado"
        

condicion= verificar_calificacion(4,6,8)
print("El alumno esta ",condicion)
 
