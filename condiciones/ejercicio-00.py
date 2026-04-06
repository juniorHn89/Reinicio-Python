def es_par(numero):
    return numero % 2 == 0

numero = int(input("Ingresa el numero: "))

resultado = es_par(numero)





if numero % 2 == 0:
    print("Es par")
else:
    print("Es impar")