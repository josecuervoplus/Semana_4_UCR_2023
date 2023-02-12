def contar_caracteres(cadena):
    # Creamos un diccionario vacío para almacenar las apariciones de cada caracter
    contador_caracteres = {}

    # Recorremos cada caracter en la cadena
    for caracter in cadena:
        # Si el caracter ya está en el diccionario, aumentamos su contador en 1
        if caracter in contador_caracteres:
            contador_caracteres[caracter] += 1
        # Si no está en el diccionario, lo agregamos y lo inicializamos en 1
        else:
            contador_caracteres[caracter] = 1

    # Devolvemos el diccionario con las apariciones de cada caracter
    return contador_caracteres

# Llamamos la función y guardamos el resultado en una variable
resultado = contar_caracteres("papaya")

# Imprimimos el resultado en pantalla
print(resultado)

resultado2 = contar_caracteres("Arrivillaga")
resultado3 = contar_caracteres("Otorrinolaringologo")

# Imprimimos el resultado en pantalla
print(resultado)
print(resultado2)
print(resultado3)