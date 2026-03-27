# 1. Acceso a discoteca (PSEUDOCODIGO)
# 1. Pedir la edad (numero entero)
# 2. Pedir si tiene DNI (s/n) y convertirlo a True/False
# 3. Si edad >= 18 Y tiene DNI:
#       Imprimir "Puedes entrar"
#    Si edad >= 18 Y NO tiene DNI:
#       Imprimir "Te falta identificacion"
#    Si edad < 18:
#       Imprimir "No puedes entrar"

def pedir_edad():
    while True:
        try:
            edad = int(input("Cuantos años tienes: "))
            return edad
        except ValueError:
            print("Ingresa datos correctos")


def pedir_dni():
    while True:
        respuesta = input("¿Tienes DNI? (s/n): ").strip().lower()
        
        if respuesta in ["s", "si", "sí"]:
            return True
        elif respuesta in ["n", "no"]:
            return False
        else:
            print("Por favor escribe 's' o 'n'")
    
    
    
def verificar_acceso(tiene_edad,dni):
    
    if tiene_edad >= 18 and dni:
        return "Puedes entrar"
    elif tiene_edad >= 18 and not dni:
        return "te falta identificacion"
    else:
        return("No puedes entrar")
    
    
    

    
tiene_edad = pedir_edad()
dni = pedir_dni()
resultado = verificar_acceso(tiene_edad,dni)
print(resultado)