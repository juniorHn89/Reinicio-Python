# PSEUDOC�DIGO - N�mero par o impar
# 1. Pedir al usuario ingresar un n�mero
# 2. Convertir a entero
# 3. SI n�mero % 2 == 0
#    Imprimir 'Es par'
# 4. SINO
#    Imprimir 'Es impar'

num = int(input("Ingresa el numero: "))

if num == 0:
    print("Es cero")
elif num % 2 == 0:
    print("Es par")
else:
    print("Es impar")


