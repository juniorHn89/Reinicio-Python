# Haz un programa con funciones que:
# Cree una función analizar_numero(numero)
# Devuelva:
# "par positivo"
# "par negativo"
# "impar positivo"
# "impar negativo"
# "cero" (caso especial 👀)
# Luego imprime el resultado
def analizar_numero(numero):
    # 1️⃣ Revisar si el número es cero → caso especial
    if numero == 0:
        return "cero"
    
    # 2️⃣ Determinar si es par o impar
    if numero % 2 == 0:
        tipo = "par"
    else:
        tipo = "impar"
    
    # 3️⃣ Determinar si es positivo o negativo
    if numero > 0:
        signo = "positivo"
    else:
        signo = "negativo"
    
    # 4️⃣ Combinar resultados y devolverlos
    return tipo + " " + signo

numero = int(input("Ingresa el numero: "))

resultado = analizar_numero(numero)

print(resultado)






