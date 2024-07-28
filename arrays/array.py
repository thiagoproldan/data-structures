# Example of a one-dimensional array (list in Python)
# Exemplo de um array unidimensional (lista em Python)
# Ejemplo de un array unidimensional (lista en Python)
arr = [1, 2, 3, 4, 5]

# Accessing elements
# Acessando elementos
# Accediendo a elementos
print(arr[0]) # Output / Saída / Salida: 1
print(arr[2]) # Output / Saída / Salida: 3

# Modifying elements
# Modificando elementos
arr[1] = 10
print(arr) # Output / Saída / Salida: [1, 10, 3, 4, 5]

# Adding elements
# Adicionando elementos
# Agregando elementos
arr.append(6)
print(arr) # Output / Saída / Salida: [1, 10, 3, 4, 5, 6]

# Removing elements
# Removendo elementos
# Eliminando elementos
arr.remove(10)
print(arr) # Output / Saída / Salida: [1, 3, 4, 5, 6]

# Iterating over the elements
# Iterando sobre os elementos
# Iterando sobre los elementos
for element in arr:
    print(element)

# Checking if an element is in the array
# Verificando se um elemento está no array
# Verificando si un elemento está en el array
print(3 in arr) # Output / Saída / Salida: True

# Finding the length of the array
# Encontrando o tamanho do array
# Encontrando el tamaño del array
print(len(arr)) # Output / Saída / Salida: 5

# Finding the index of an element
# Encontrando o índice de um elemento
# Encontrando el índice de un elemento
print(arr.index(4)) # Output / Saída / Salida: 2
