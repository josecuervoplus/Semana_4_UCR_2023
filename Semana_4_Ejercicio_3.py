def eliminar_elemento(lista, elemento):
    # Crea una nueva lista que almacenará los elementos que no son iguales al elemento dado
    resultado = [item for item in lista if item != elemento]
    # Devuelve la nueva lista sin los elementos dados
    return resultado

# Ejemplo de uso
lista = [20, 30, 40, 20, 5, 100, 5, 20]
elemento = 20
print(eliminar_elemento(lista, elemento)) # Imprime [30, 40, 5, 100, 5]

lista = ["perro", "gato", "sombrero", "gato", "zanahoria"]
elemento = "gato"
print(eliminar_elemento(lista, elemento)) # Imprime [ "perro", "sombrero", "zanahoria"]



# Ejemplo 1
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 1, 2, 1]
valor = 1
resultado = eliminar_elemento(lista, valor)
print(resultado)


# Ejemplo 2
lista = ["manzana", "pera", "banana", "manzana", "kiwi", "manzana"]
valor = "manzana"
resultado = eliminar_elemento(lista, valor)
print(resultado)


