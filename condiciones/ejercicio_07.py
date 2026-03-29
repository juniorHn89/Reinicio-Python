# 2. Login basico (PSEUDOCODIGO)
# 1. Preguntar si el usuario es correcto (s/n) y convertirlo a True/False
# 2. Preguntar si la contrasena es correcta (s/n) y convertirlo a True/False
# 3. Si usuario_correcto Y password_correcto:
#       Imprimir "Acceso concedido"
#    Si usuario_correcto Y NO password_correcto:
#       Imprimir "Contrasena incorrecta"
#    Si NO usuario_correcto:
#       Imprimir "Usuario no existe"



def pedir_boleano(mensaje):
        
    while True:
            respuesta = input(mensaje).strip().lower()
            
            if respuesta in ["s","si","sí"]:
                return True
            
            elif respuesta in ["n","no"]:
                return False

            else:
                print("error")



usuario_correcto = pedir_boleano("El usuario es correcto? (s/n) ")
password_correcta = pedir_boleano("La contraseña es correcto? (s/n) ")


if usuario_correcto and password_correcta:
    print("Acceso concedido")
elif usuario_correcto and not password_correcta:
    print("Contraseña incorrecta")
else:
    print("Usuario desconocido")

















