# 3. Compra online (PSEUDOCODIGO)
# 1. Pedir saldo (numero)
# 2. Pedir precio (numero)
# 3. Si saldo > precio:
#       Imprimir "Compra realizada"
#    Si saldo == precio:
#       Imprimir "Compra realizada"
#       Imprimir "Te quedas a 0"
#    Si saldo < precio:
#       Imprimir "Saldo insuficiente"



saldo = input("Saldo disponible? ")

precio = input("se te cobraran ")

if saldo > precio:
    print("compra realizada")
elif saldo == precio:
    print("compra realizada")
    print("te quedas a 0")
elif saldo < precio:
    print("saldo insuficiente")





