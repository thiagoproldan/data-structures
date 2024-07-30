# Example of a list / Exemplo de uma lista / Ejemplo de una lista
lst = [1, "dois", 3.0, True]

# Accessing elements / Acessando elementos / Accediendo a elementos
print(lst[0])  # Output / Saída / Salida: 1
print(lst[1])  # Output / Saída / Salida: dois

# Modifying elements / Modificando elementos / Modificando elementos
lst[2] = "três"
print(lst)  # Output / Saída / Salida: [1, 'dois', 'três', True]

# Adding elements / Adicionando elementos / Agregando elementos
lst.append(False)
print(lst)  # Output / Saída / Salida: [1, 'dois', 'três', True, False]

# Removing elements / Removendo elementos / Eliminando elementos
lst.pop(1)
print(lst)  # Output / Saída / Salida: [1, 'três', True, False]

# Iterating over the elements / Iterando sobre os elementos / Iterando sobre los elementos
for element in lst:
    print(element)

# Checking if an element is in the list / Verificando se um elemento está na lista / Verificando si un elemento está en la lista
print("três" in lst)  # Output / Saída / Salida: True

# Finding the length of the list / Encontrando o tamanho da lista / Encontrando el tamaño de la lista
print(len(lst))  # Output / Saída / Salida: 4
