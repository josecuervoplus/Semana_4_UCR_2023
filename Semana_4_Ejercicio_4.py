def secuencia_a_lista_y_tupla(secuencia):
    """
    Esta función recibe una secuencia de números separados por comas
    y devuelve una lista y una tupla con dichos valores.
    """
    # Convertimos la secuencia en una lista de números
    lista_numeros = [int(numero) for numero in secuencia.split(',')]
    
    # Convertimos la lista en una tupla
    tupla_numeros = tuple(lista_numeros)
    
    # Imprimimos la lista y la tupla
    print("Lista:", lista_numeros)
    print("Tupla:", tupla_numeros)
    
    return lista_numeros, tupla_numeros

# Ejemplo 1
secuencia = "1,2,3,4,5,6"
secuencia_a_lista_y_tupla(secuencia)

# Ejemplo 2
secuencia = "10,20,30,40,50"
secuencia_a_lista_y_tupla(secuencia)

# Ejemplo 3
secuencia = "100,200,300,400"
secuencia_a_lista_y_tupla(secuencia)
