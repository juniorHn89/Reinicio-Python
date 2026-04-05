# 4. Nivel de videojuego (PSEUDOCODIGO)
# 1. Pedir nivel (numero entero)
# 2. Pedir si tiene llave (s/n) y convertirlo a True/False
# 3. Si nivel >= 10 Y tiene llave:
#       Imprimir "Accedes al nivel secreto"
#    Si nivel >= 10 Y NO tiene llave:
#       Imprimir "Te falta la llave"
#    Si nivel < 10:
#       Imprimir "Nivel insuficiente"


nivel = int(input("Nivel: "))

def tiene_llave():
    
    respuesta = input("Tienes llave?,  (s/n) ").strip().lower()
        
    if respuesta in ["s", "si"]:
        return True
    elif respuesta in ("n", "no"):
        return False
    else:
        print("Por favor escribe s o n")
        return tiene_llave()
        
llave = tiene_llave()
        
if nivel >= 10 and llave:
    print("Accedes al nivel secreto")
elif nivel  >= 10 and not llave:
    print("Te falta la llave")
elif nivel < 10:
    print("Nivel insuficiente")
    



