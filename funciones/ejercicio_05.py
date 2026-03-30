# PSEUDOC�DIGO - Funci�n con l�gica
# 1. Crear funci�n 'es_mayor_de_edad(edad)'
# 2. SI edad >= 18
#    RETORNAR True
# 3. SINO
#    RETORNAR False
# 4. Llamar la funci�n con 20 y 15

def es_mayor_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False
    

print(es_mayor_de_edad(20))
print(es_mayor_de_edad(15))
