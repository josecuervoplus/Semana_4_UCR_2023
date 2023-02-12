def contar_caracteres(input_string):
    # Inicializamos los contadores de letras, números y caracteres especiales en 0
    letras = 0
    numeros = 0
    caracteres_especiales = 0
    
    # Iteramos sobre cada carácter en la cadena
    for char in input_string:
        # Si el carácter es una letra, aumentamos el contador de letras
        if char.isalpha():
            letras += 1
        # Si el carácter es un número, aumentamos el contador de números
        elif char.isdigit():
            numeros += 1
        # Si no es ni una letra ni un número, asumimos que es un carácter especial y aumentamos el contador de caracteres especiales
        else:
            caracteres_especiales += 1
    
    # Imprimimos los contadores de letras, números y caracteres especiales en pantalla
    print("Letras =", letras)
    print("Números =", numeros)
    print("Caracteres especiales =", caracteres_especiales)


input_string = "P@#yn26at^&i5ve"
contar_caracteres (input_string)

input_string = "Hello, World!"
contar_caracteres (input_string)

input_string = "1234567890"
contar_caracteres (input_string)